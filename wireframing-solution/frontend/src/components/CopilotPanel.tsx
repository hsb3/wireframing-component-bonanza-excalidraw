import { useState, useEffect, useRef } from 'react'
import { Client } from '@langchain/langgraph-sdk'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import './CopilotPanel.css'

interface Message {
  role: 'user' | 'assistant' | 'system'
  content: string
  timestamp: Date
  toolCalls?: any[]
}

interface CopilotPanelProps {
  onWireframeGenerated?: (data: any) => void
  excalidrawAPI?: any
}

export default function CopilotPanel({ onWireframeGenerated, excalidrawAPI }: CopilotPanelProps) {
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const [threadId, setThreadId] = useState<string | null>(null)
  const [client, setClient] = useState<Client | null>(null)
  const messagesEndRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    // Initialize LangGraph client
    const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000'
    const lgClient = new Client({ apiUrl })
    setClient(lgClient)

    // Create initial thread
    lgClient.threads.create().then((thread) => {
      setThreadId(thread.thread_id)
    })
  }, [])

  useEffect(() => {
    // Auto-scroll to bottom
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()

    if (!input.trim() || !client || !threadId) return

    const userMessage: Message = {
      role: 'user',
      content: input,
      timestamp: new Date()
    }

    setMessages(prev => [...prev, userMessage])
    setInput('')
    setLoading(true)

    try {
      // Stream response from LangGraph agent
      const streamResponse = client.runs.stream(
        threadId,
        'agent',  // Graph name from langgraph.json
        {
          input: { messages: [{ role: 'user', content: input }] },
          streamMode: 'messages'
        }
      )

      let assistantContent = ''
      let toolCalls: any[] = []

      for await (const chunk of streamResponse) {
        if (chunk.event === 'messages/partial') {
          // Streaming message content
          const message = chunk.data[0]
          if (message.content) {
            assistantContent = message.content
          }
          if (message.tool_calls) {
            toolCalls = message.tool_calls
          }
        } else if (chunk.event === 'messages/complete') {
          // Final message
          const message = chunk.data[0]
          assistantContent = message.content || assistantContent

          const assistantMessage: Message = {
            role: 'assistant',
            content: assistantContent,
            timestamp: new Date(),
            toolCalls
          }

          setMessages(prev => [...prev, assistantMessage])

          // Check if wireframe was generated
          if (toolCalls.some((tc: any) => tc.name === 'compose_wireframe')) {
            // Load the generated wireframe
            // (This would need to fetch the .excalidraw file and update canvas)
            console.log('Wireframe generated!', toolCalls)
          }
        }
      }

    } catch (error) {
      console.error('Error streaming response:', error)
      const errorMessage: Message = {
        role: 'system',
        content: `Error: ${error instanceof Error ? error.message : 'Unknown error'}`,
        timestamp: new Date()
      }
      setMessages(prev => [...prev, errorMessage])
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="copilot-panel">
      {/* Header */}
      <div className="copilot-header">
        <h2>AI Copilot</h2>
        <span className="status-indicator">{loading ? '●' : '○'}</span>
      </div>

      {/* Messages */}
      <div className="messages-container">
        {messages.map((msg, idx) => (
          <div key={idx} className={`message message-${msg.role}`}>
            <div className="message-header">
              <span className="message-role">{msg.role}</span>
              <span className="message-time">
                {msg.timestamp.toLocaleTimeString()}
              </span>
            </div>
            <div className="message-content">
              <ReactMarkdown remarkPlugins={[remarkGfm]}>
                {msg.content}
              </ReactMarkdown>
            </div>
            {msg.toolCalls && msg.toolCalls.length > 0 && (
              <div className="tool-calls">
                {msg.toolCalls.map((tc, i) => (
                  <div key={i} className="tool-call">
                    <code>{tc.name}</code>
                  </div>
                ))}
              </div>
            )}
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <form onSubmit={handleSubmit} className="copilot-input-container">
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
              e.preventDefault()
              handleSubmit(e)
            }
          }}
          placeholder="Describe the wireframe you want to create..."
          className="copilot-input"
          rows={3}
          disabled={loading}
        />
        <button
          type="submit"
          disabled={loading || !input.trim()}
          className="send-button"
        >
          {loading ? 'Generating...' : 'Send'}
        </button>
      </form>
    </div>
  )
}
