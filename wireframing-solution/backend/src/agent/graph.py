"""
LangGraph Deep Agent for Wireframe Generation
Uses component library to compose Excalidraw wireframes
"""
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import create_deep_agent
from langchain_anthropic import ChatAnthropic
from langchain_core.tools import tool
from pathlib import Path
import json

# Load component registry
REGISTRY_PATH = Path(__file__).parent.parent / 'data' / 'component-registry.json'
with open(REGISTRY_PATH) as f:
    COMPONENT_REGISTRY = json.load(f)

# Load catalog for LLM context
CATALOG_PATH = Path(__file__).parent.parent / 'data' / 'component-catalog.txt'
with open(CATALOG_PATH) as f:
    COMPONENT_CATALOG = f.read()


@tool
def search_components(
    query: str,
    theme: str = "mork",
    limit: int = 10
) -> list[dict]:
    """
    Search for UI components by name, category, or tags.

    Args:
        query: Search query (e.g., "login", "button", "table")
        theme: Theme to search (mork, abc123-dark, bronzer)
        limit: Maximum results to return

    Returns:
        List of matching components with metadata
    """
    query_lower = query.lower()
    results = []

    for comp in COMPONENT_REGISTRY['components']:
        # Filter by theme
        if comp['theme'] != theme:
            continue

        # Search in name, tags, category, description
        if (query_lower in comp['name'].lower() or
            query_lower in comp.get('description', '').lower() or
            query_lower in comp.get('category', '').lower() or
            any(query_lower in tag for tag in comp.get('tags', []))):

            results.append({
                'id': comp['id'],
                'name': comp['name'],
                'description': comp['description'],
                'dimensions': comp['dimensions'],
                'category': comp['category'],
                'tags': comp['tags'][:5]  # Top 5 tags
            })

        if len(results) >= limit:
            break

    return results


@tool
def get_component(component_id: str) -> dict:
    """
    Get full details for a specific component.

    Args:
        component_id: Component ID from search results

    Returns:
        Complete component metadata including element data
    """
    for comp in COMPONENT_REGISTRY['components']:
        if comp['id'] == component_id:
            return comp

    return {"error": f"Component {component_id} not found"}


@tool
def compose_wireframe(
    name: str,
    theme: str,
    components: list[dict],
    canvas_size: dict = None
) -> dict:
    """
    Compose a wireframe from components.

    Args:
        name: Wireframe name (for filename)
        theme: Theme to use (mork, abc123-dark, bronzer)
        components: List of {component_id, x, y, customizations}
        canvas_size: Optional {width, height} for canvas

    Returns:
        {file_path, element_count, dimensions}
    """
    from ..tools.composer import WireframeComposer

    composer = WireframeComposer(COMPONENT_REGISTRY)
    result = composer.compose(name, theme, components, canvas_size)

    return {
        'file_path': str(result['file']),
        'element_count': result['element_count'],
        'dimensions': result['dimensions'],
        'component_count': len(components)
    }


@tool
def list_categories(theme: str = "mork") -> dict:
    """
    List available component categories.

    Args:
        theme: Theme to filter by

    Returns:
        Categories with component counts
    """
    categories = {}

    for comp in COMPONENT_REGISTRY['components']:
        if comp['theme'] != theme:
            continue

        cat = comp.get('category', 'Other')
        if cat not in categories:
            categories[cat] = {
                'name': cat,
                'count': 0,
                'examples': []
            }

        categories[cat]['count'] += 1
        if len(categories[cat]['examples']) < 3:
            categories[cat]['examples'].append(comp['name'])

    return {
        'theme': theme,
        'categories': list(categories.values()),
        'total': sum(c['count'] for c in categories.values())
    }


# Define agent state
class AgentState(TypedDict):
    messages: Annotated[list, "The messages in the conversation"]


# Create the agent
llm = ChatAnthropic(
    model="claude-sonnet-4-5-20250929",
    temperature=0
)

# System message with component catalog
SYSTEM_MESSAGE = f"""You are a wireframe design assistant. You help users create UI mockups using a library of 154 pre-built components.

{COMPONENT_CATALOG[:2000]}

... (see component-catalog.txt for full list)

Available tools:
- search_components(query, theme) - Find components by keyword
- get_component(id) - Get component details
- list_categories(theme) - Browse component categories
- compose_wireframe(name, theme, components) - Create wireframe file

Workflow:
1. When user describes a screen, search for relevant components
2. Plan layout with component positions
3. Use compose_wireframe to generate the .excalidraw file
4. Always prefer using existing components over suggesting to draw from scratch

Example:
User: "Create a login screen"
You:
1. search_components("login email password button", theme="mork")
2. Find: B/Form/Input/Text (×2), Button: Primary
3. compose_wireframe with components at appropriate positions
4. Return: "Login screen created at output/login.excalidraw"
"""

# Create deep agent
graph = create_deep_agent(
    llm,
    tools=[search_components, get_component, compose_wireframe, list_categories],
    system_message=SYSTEM_MESSAGE
)
