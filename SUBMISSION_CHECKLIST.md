# Library Submission Checklist

Use this checklist before submitting libraries to [excalidraw-libraries](https://github.com/excalidraw/excalidraw-libraries).

## 📋 Pre-Submission Quality Standards

### ✅ Component Quality

- [ ] **Visibility on white canvas** - All components have sufficient contrast
  - Borders: Minimum Zinc-300 (#d4d4d8) or darker
  - Backgrounds: Use Zinc-50 (#fafafa) instead of pure white
  - Test by importing into Excalidraw on default white canvas

- [ ] **Proper scaling** - All components are proportionate to each other
  - Device frames scaled to ~1/5 actual size (Desktop: 288x180, not 1440x900)
  - Buttons, inputs, and cards use consistent height (~40px)
  - Text is readable (14-18px for body, 12px for labels)

- [ ] **Grouping** - Multi-element items are properly grouped
  - Each library item acts as a single unit when inserted
  - Exception: Templates or layouts where ungrouped makes more sense

- [ ] **Naming conventions** - Items are searchable and descriptive
  - Use hierarchical names: `Category/Subcategory/Component/Variant`
  - Examples: `A/Button/Primary`, `B/Form/Input/Text`, `C/Shell/App/3Pane`
  - Avoid generic names like "Button 1" or "Box"

### ✅ Excalidraw Official Guidelines

From [excalidraw-libraries README](https://github.com/excalidraw/excalidraw-libraries):

- [ ] **1. General usefulness** - Library is useful to others, not just personal use case
- [ ] **2. No trivial items** - Don't submit items easy to create directly (single arrows, squares)
- [ ] **3. Original content** - Don't copy/paste from other libraries without significant changes
- [ ] **4. English only** - All text/labels, descriptions, and titles in English
- [ ] **5. Standalone items** - Each item should be usable on its own
- [ ] **6. Minimum 3 items** - Library should have at least 3 related items in a single category
- [ ] **7. Multi-element grouping** - Items with multiple elements should be grouped (see #3)

### ✅ Theme Consistency

- [ ] **All themes generated** - Default, Carbon, Warm variants all created
- [ ] **Preview images created** - PNG screenshots for each theme (see `PREVIEW_IMAGES_GUIDE.md`)
- [ ] **Theme contrast validated** - Each theme tested on both light and dark Excalidraw canvas
- [ ] **Color token usage** - No hardcoded colors, all use theme constants

## 📦 File Preparation

### ✅ Library Files

- [ ] **Generated from source** - Run `uv run excalidraw-generate --theme <theme>`
- [ ] **File naming convention**:
  ```
  shadcn-wireframe-default.excalidrawlib
  shadcn-wireframe-carbon.excalidrawlib
  shadcn-wireframe-warm.excalidrawlib
  ```
- [ ] **File size reasonable** - Each library < 2MB (current: ~750KB ✓)
- [ ] **Copied to submission folder** - Files in `submission/` directory

### ✅ Preview Images

- [ ] **PNG format** - One preview per theme
- [ ] **High resolution** - At least 1200px width for clarity
- [ ] **Clean layout** - Grid or organized showcase of components
- [ ] **File naming**:
  ```
  shadcn-wireframe-default.png
  shadcn-wireframe-carbon.png
  shadcn-wireframe-warm.png
  ```
- [ ] **White background** - Matches Excalidraw's default canvas color
- [ ] **Copied to submission folder** - PNGs in `submission/` directory

### ✅ Metadata

- [ ] **libraries.json entries** - Created in `submission/libraries-json-entries.json`
- [ ] **Titles descriptive** - Clear, concise library names
- [ ] **Descriptions helpful** - 1-2 sentences explaining what's included and use case
- [ ] **Author info correct** - GitHub username (hsb3)

Example entry:
```json
{
  "name": "shadcn-wireframe-default",
  "description": "Hand-drawn wireframe components for SaaS & AI apps. 154 components from atoms to full page templates.",
  "authors": ["hsb3"],
  "source": "https://github.com/hsb3/wireframing-component-bonanza-excalidraw"
}
```

## 🔍 Validation Steps

### ✅ Automated Validation

- [ ] **Run validator** - `python validate_libraries.py`
- [ ] **All items have names** - No unnamed library items
- [ ] **No duplicate IDs** - Each element has unique ID
- [ ] **Valid JSON structure** - Library files parse correctly

### ✅ Manual Testing

- [ ] **Import test** - Import library into Excalidraw using "Load" button
- [ ] **Search test** - Search for components by category (e.g., "button", "input", "card")
- [ ] **Insertion test** - Insert 5-10 random components, verify they:
  - Appear at correct scale
  - Have visible borders/backgrounds
  - Are properly grouped (if multi-element)
  - Can be moved/resized as single unit

- [ ] **Cross-theme test** - Repeat import/insertion test for all 3 themes

## 🚀 Submission Workflow

### ✅ Repository Setup

- [ ] **Main repo clean** - Uncommitted changes committed or stashed
  ```bash
  git status  # Should show clean working tree
  ```

- [ ] **Fork updated** - excalidraw-libraries fork synced with upstream
  ```bash
  cd excalidraw-libraries-fork
  git fetch upstream
  git checkout main
  git merge upstream/main
  git push origin main
  ```

### ✅ Branch & Files

- [ ] **Create feature branch** - Descriptive name
  ```bash
  cd excalidraw-libraries-fork
  git checkout -b add-shadcn-wireframe-kits
  ```

- [ ] **Copy library files** - To fork's `libraries/` directory
  ```bash
  cp submission/*.excalidrawlib excalidraw-libraries-fork/libraries/
  ```

- [ ] **Copy preview images** - To fork's `public/` directory
  ```bash
  cp submission/*.png excalidraw-libraries-fork/public/
  ```

- [ ] **Update libraries.json** - Add entries from `submission/libraries-json-entries.json`

### ✅ Commit & PR

- [ ] **Atomic commits** - One commit per library or logical grouping
  ```bash
  git add libraries/shadcn-wireframe-*.excalidrawlib
  git add public/shadcn-wireframe-*.png
  git add libraries.json
  git commit -m "Add shadcn Wireframe Kits (Default, Carbon, Warm)"
  ```

- [ ] **Push to fork**
  ```bash
  git push origin add-shadcn-wireframe-kits
  ```

- [ ] **Create PR** - Via GitHub CLI or web interface
  ```bash
  gh pr create --repo excalidraw/excalidraw-libraries \
    --title "Add shadcn Wireframe Kits (Default, Carbon, Warm)" \
    --body "See submission/README.md for details"
  ```

### ✅ PR Description

Include in PR description:
- [ ] **What's included** - Number of components, theme variants
- [ ] **Use case** - Who would use these (SaaS designers, wireframers, etc.)
- [ ] **Preview images** - Link or embed PNG previews
- [ ] **Source repo** - Link to development repository
- [ ] **Checklist confirmation** - "All submission guidelines followed ✓"

## 📝 Post-Submission

### ✅ After PR Created

- [ ] **Monitor for feedback** - Check GitHub notifications daily
- [ ] **Respond to review comments** - Address requested changes promptly
- [ ] **Update PR** - Push fixes to same branch, PR auto-updates

### ✅ If Changes Requested

- [ ] **Update source code** - Make changes in main development repo
- [ ] **Regenerate libraries** - Run generation scripts with fixes
- [ ] **Update fork** - Copy new files to excalidraw-libraries-fork
- [ ] **Force push if needed** - `git push --force-with-lease origin branch-name`

### ✅ After PR Merged

- [ ] **Verify on libraries.excalidraw.com** - Library appears in public catalog (may take time)
- [ ] **Delete branch** - Clean up fork
  ```bash
  git checkout main
  git branch -d add-shadcn-wireframe-kits
  git push origin --delete add-shadcn-wireframe-kits
  ```
- [ ] **Tag release** - Tag version in main development repo
  ```bash
  git tag -a v1.0.0 -m "Initial public release"
  git push origin v1.0.0
  ```

## 🛠️ Quick Commands Reference

```bash
# Generate all themes
uv run excalidraw-generate --theme default
uv run excalidraw-generate --theme carbon
uv run excalidraw-generate --theme warm

# Validate libraries
python validate_libraries.py

# Generate preview images (if script exists)
python generate_preview_images.py

# Copy to submission folder
cp output/*.excalidrawlib submission/
cp output/*.png submission/

# Run submission helper (if using automation)
./submit_to_excalidraw.sh
```

## ✋ When NOT to Submit

**Close/revoke PR and wait if:**
- [ ] Components barely visible on white canvas
- [ ] Scale inconsistencies between components
- [ ] Missing theme variants
- [ ] No preview images
- [ ] Library has < 3 useful items
- [ ] You discover bugs after submission

**It's better to withdraw and resubmit than to get negative feedback on quality issues.**

---

## Current Status

**Last submission:** PR #2431 (PREMATURE - needs to be closed)

**Next submission readiness:**
- [ ] Visibility improvements applied ✓
- [ ] Frame scales fixed ✓
- [ ] All themes regenerated
- [ ] Preview images updated
- [ ] Validation passed
- [ ] This checklist completed

**Target submission date:** _After completing all checklist items_
