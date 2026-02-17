.PHONY: help generate clean install

help:
	@echo "Excalidraw Wireframe Library Generator"
	@echo ""
	@echo "Commands:"
	@echo "  make generate        Generate default theme"
	@echo "  make carbon          Generate IBM Carbon theme"
	@echo "  make warm            Generate warm theme"
	@echo "  make all             Generate all three themes"
	@echo "  make clean           Remove generated files"
	@echo "  make install         Install with uv"

generate:
	PYTHONPATH=src python -m excalidraw_gen

carbon:
	PYTHONPATH=src python -m excalidraw_gen --theme carbon --output output/carbon.excalidrawlib --preview output/carbon-preview.excalidraw

warm:
	PYTHONPATH=src python -m excalidraw_gen --theme warm --output output/warm.excalidrawlib --preview output/warm-preview.excalidraw

all:
	@echo "Generating all themes..."
	@make generate
	@make carbon
	@make warm
	@echo "✅ All themes generated in output/"

clean:
	rm -rf output/*.excalidrawlib output/*.excalidraw

install:
	uv pip install -e .
