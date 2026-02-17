import sys
from excalidraw_gen.core.themes import get_theme

def main(theme_name='default', output_file='output/shadcn-saas-kit.excalidrawlib', preview_file='output/shadcn-saas-kit-preview.excalidraw',
         generate_preview=True, columns=3, spacing=60):
    """
    Generate Excalidraw library with specified theme.

    Args:
        theme_name: Theme to use ('default', 'carbon', 'warm')
        output_file: Output filename for library
        preview_file: Output filename for preview
        generate_preview: Whether to generate preview document
        columns: Number of columns in preview grid
        spacing: Spacing between items in preview
    """
    # Load selected theme and inject it into sys.modules
    # This ensures all component imports get the right theme
    selected_theme = get_theme(theme_name)

    import types
    theme_module = types.ModuleType('theme')
    theme_module.Theme = selected_theme
    sys.modules['theme'] = theme_module
    sys.modules['excalidraw_gen.core.themes.default'] = theme_module

    # Import components AFTER setting theme
    from excalidraw_gen.components import (
        add_frames,
        add_primitives,
        add_base_ui,
        add_modules,
        add_shells,
        add_organisms,
        add_saas_blocks,
        add_templates,
        add_ai_patterns
    )
    from excalidraw_gen.builder import ExcalidrawBuilder

    print(f"🎨 Using theme: {theme_name}")
    print("Initializing Excalidraw Builder...")
    builder = ExcalidrawBuilder(theme=selected_theme)

    print("Adding Level 0: Frames & Layout...")
    add_frames(builder)

    print("Adding Level 1: Primitives...")
    add_primitives(builder)

    print("Adding Level 2: Base UI...")
    add_base_ui(builder)

    print("Adding Level 3: Modules...")
    add_modules(builder)

    print("Adding Level 3: Shells...")
    add_shells(builder)

    print("Adding Level 3: Organisms...")
    add_organisms(builder)

    print("Adding Level 4: SaaS Patterns...")
    add_saas_blocks(builder)

    print("Adding Level 4: Templates...")
    add_templates(builder)

    print("Adding Level 5: AI Patterns...")
    add_ai_patterns(builder)

    builder.save(output_file)
    print(f"\n✅ Library saved to {output_file}")

    # Generate preview document
    if generate_preview:
        print("\nGenerating preview document...")
        builder.save_preview(preview_file, columns=columns, spacing=spacing)
        print(f"✅ Preview document saved to {preview_file}")
    else:
        print("\n⏭️  Skipping preview generation (--no-preview)")

    return builder

if __name__ == "__main__":
    main()
