# Dual Repository Workflow Guide

This project manages two separate GitHub repositories with different purposes:

1. **Development Repo** (wireframing-component-bonanza-excalidraw) - Component library source code
2. **Submission Fork** (excalidraw-libraries) - Fork for submitting to public catalog

## 🏗️ Current Structure

```
shadcn-excalidraw/                           # Main development repo
├── src/excalidraw_gen/                      # Python source code
│   ├── core/themes/                         # Theme definitions
│   ├── components/                          # Component generators
│   └── builder/                             # Library builder
├── output/                                  # Generated libraries (local)
├── submission/                              # Staging area for public submission
└── excalidraw-libraries-fork/               # ⚠️ NESTED fork repo
    └── libraries/                           # Public catalog files
```

### ⚠️ Issues with Current Structure

**Problem: Nested Git Repository**
- `excalidraw-libraries-fork/` is a separate git repo nested inside main repo
- This creates confusion with `.gitignore`, commits, and branches
- Risk of accidentally committing fork contents to main repo

**Problem: File Duplication**
- Library files in `output/`, `submission/`, and `fork/libraries/`
- Multiple copies = hard to know which is "source of truth"
- Easy to submit wrong/outdated version

**Problem: Unclear Workflow**
- Not obvious when to use main repo vs fork
- Manual copying between directories is error-prone

## ✅ Recommended Structure

### Option A: Separate Directories (Recommended)

```
~/Projects/
├── shadcn-excalidraw/                    # Development repo
│   ├── src/                              # Source code
│   ├── output/                           # Generated files
│   └── .git/                             # Main repo git
│
└── excalidraw-libraries/                 # Fork (sibling, not nested)
    ├── libraries/                        # Public catalog
    ├── public/                           # Preview images
    └── .git/                             # Fork git
```

**Benefits:**
- Clean separation of concerns
- No nested git repos
- Clear which repo you're working in
- Easier to manage with git

**Migration:**
```bash
# Move fork out of main repo
cd ~/Desktop
mv shadcn-excalidraw/excalidraw-libraries-fork ./excalidraw-libraries

# Update .gitignore in main repo to prevent re-adding
echo "excalidraw-libraries-fork/" >> shadcn-excalidraw/.gitignore
```

### Option B: Keep Current Structure (Not Recommended)

If you must keep the nested structure:

1. **Add to main repo's `.gitignore`:**
   ```
   excalidraw-libraries-fork/
   ```

2. **Use clear commit discipline:**
   - Always check `git status` before committing
   - Never run `git add .` from root
   - Commit main repo and fork separately

## 🔄 Workflow Steps

### 1. Development (Main Repo)

**Location:** `~/Desktop/shadcn-excalidraw/`

```bash
# Make changes to source code
vim src/excalidraw_gen/components/level1_primitives.py

# Regenerate libraries
uv run excalidraw-generate --theme default
uv run excalidraw-generate --theme carbon
uv run excalidraw-generate --theme warm

# Validate
python validate_libraries.py

# Commit changes
git add src/
git commit -m "feat: add new button variants"
git push origin main
```

**Files to commit in main repo:**
- ✅ Source code (`src/`)
- ✅ Documentation (`*.md`)
- ✅ Scripts (`scripts/`, `*.py`)
- ✅ Config (`pyproject.toml`, `Makefile`)
- ❌ Generated libraries (`output/`)
- ❌ Fork contents (`excalidraw-libraries-fork/`)

### 2. Staging for Submission

**Location:** `~/Desktop/shadcn-excalidraw/submission/`

```bash
# Copy generated files to submission staging area
cp output/shadcn-saas-kit.excalidrawlib submission/shadcn-wireframe-default.excalidrawlib
cp output/carbon.excalidrawlib submission/shadcn-wireframe-carbon.excalidrawlib
cp output/warm.excalidrawlib submission/shadcn-wireframe-warm.excalidrawlib

# Generate preview images
python generate_preview_images.py

# Copy preview images
cp output/*.png submission/

# Review before proceeding
ls -lh submission/
```

**Purpose of `submission/` folder:**
- Staging area for files ready to submit
- Final validation before copying to fork
- Keeps a clean snapshot of "what was submitted"
- Should be committed to main repo for historical record

### 3. Submission (Fork Repo)

**Location:** `~/Desktop/excalidraw-libraries/` (or `~/Desktop/shadcn-excalidraw/excalidraw-libraries-fork/`)

```bash
cd excalidraw-libraries-fork/  # Or ~/Desktop/excalidraw-libraries/

# Sync with upstream first
git fetch upstream
git checkout main
git merge upstream/main
git push origin main

# Create feature branch
git checkout -b add-shadcn-wireframe-v2

# Copy files from submission staging
cp ../submission/shadcn-wireframe-*.excalidrawlib libraries/
cp ../submission/shadcn-wireframe-*.png public/

# Update libraries.json
# (manually edit or use script)

# Commit
git add libraries/ public/ libraries.json
git commit -m "Add shadcn Wireframe Kits (Default, Carbon, Warm)"

# Push to fork
git push origin add-shadcn-wireframe-v2

# Create PR
gh pr create --repo excalidraw/excalidraw-libraries \
  --title "Add shadcn Wireframe Kits v2" \
  --body "Updated submission with improved visibility and scaling"
```

**Files to commit in fork:**
- ✅ Library files (`libraries/*.excalidrawlib`)
- ✅ Preview images (`public/*.png`)
- ✅ Metadata (`libraries.json`, `authors.json`)
- ❌ Unrelated fork files (keep only your additions)

## 🤖 Automation

### Script: `scripts/prepare_submission.sh`

Create this helper script to automate the workflow:

```bash
#!/bin/bash
# Prepare libraries for submission to excalidraw-libraries

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "🎨 Generating all themes..."
cd "$PROJECT_ROOT"
uv run excalidraw-generate --theme default
uv run excalidraw-generate --theme carbon
uv run excalidraw-generate --theme warm

echo "📸 Generating preview images..."
python generate_preview_images.py

echo "📦 Copying to submission folder..."
cp output/shadcn-saas-kit.excalidrawlib submission/shadcn-wireframe-default.excalidrawlib
cp output/carbon.excalidrawlib submission/shadcn-wireframe-carbon.excalidrawlib
cp output/warm.excalidrawlib submission/shadcn-wireframe-warm.excalidrawlib
cp output/*.png submission/

echo "✅ Submission folder ready!"
echo ""
echo "Next steps:"
echo "1. Review files in submission/"
echo "2. Run validation: python validate_libraries.py"
echo "3. Copy to fork: cp submission/* excalidraw-libraries-fork/libraries/"
echo "4. Commit and create PR in fork"
```

Make it executable:
```bash
chmod +x scripts/prepare_submission.sh
```

### Makefile Targets

Add to `Makefile`:

```makefile
.PHONY: generate validate prepare-submit

# Generate all themes
generate:
	uv run excalidraw-generate --theme default
	uv run excalidraw-generate --theme carbon
	uv run excalidraw-generate --theme warm

# Validate generated libraries
validate:
	python validate_libraries.py

# Prepare for submission
prepare-submit: generate validate
	./scripts/prepare_submission.sh

# Full workflow: generate, validate, prepare
submit-ready: prepare-submit
	@echo "✅ Libraries ready for submission!"
	@echo "Review submission/ folder and follow SUBMISSION_CHECKLIST.md"
```

Usage:
```bash
make submit-ready
```

## 📂 .gitignore Configuration

### Main Repo `.gitignore`

```gitignore
# Virtual environment
.venv/
__pycache__/
*.pyc

# Generated files (don't commit to main repo)
output/
*.excalidrawlib
*.excalidraw

# Keep submission/ folder but ignore generated files
submission/*.excalidrawlib
submission/*.png

# Nested fork (if keeping nested structure)
excalidraw-libraries-fork/

# OS files
.DS_Store
```

**Rationale:**
- Don't commit binary library files to main repo (they're generated)
- Keep submission/*.md documentation
- Ignore fork to prevent accidental commits

### Fork `.gitignore`

The fork should use the original excalidraw-libraries `.gitignore` (don't modify).

## 🔍 Validation Checklist

Before each submission, verify:

- [ ] **Git status clean in main repo**
  ```bash
  cd ~/Desktop/shadcn-excalidraw
  git status  # Should show "working tree clean"
  ```

- [ ] **Fork synced with upstream**
  ```bash
  cd excalidraw-libraries-fork
  git fetch upstream
  git status  # Should show "up to date with upstream/main"
  ```

- [ ] **Working on correct branch**
  ```bash
  git branch  # Main repo: on main
  cd excalidraw-libraries-fork
  git branch  # Fork: on feature branch (not main)
  ```

- [ ] **No uncommitted changes mixed between repos**
  ```bash
  # Check both repos separately
  git status  # in each repo
  ```

## 🚨 Common Mistakes to Avoid

### ❌ Committing generated files to main repo
```bash
# DON'T DO THIS in main repo:
git add output/
git commit -m "add generated files"
```

**Why:** Generated files should be regenerated from source, not versioned.

### ❌ Working on main branch in fork
```bash
# DON'T DO THIS in fork:
git checkout main
# make changes
git commit
```

**Why:** All PR submissions should be on feature branches.

### ❌ Pushing fork changes to main repo
```bash
# DON'T DO THIS:
cd excalidraw-libraries-fork
git remote add wrong-origin https://github.com/hsb3/wireframing-component-bonanza-excalidraw.git
git push wrong-origin
```

**Why:** Fork changes should only go to excalidraw-libraries, not main repo.

### ❌ Submitting outdated files
```bash
# DON'T DO THIS:
cp old-file-from-last-week.excalidrawlib excalidraw-libraries-fork/libraries/
```

**Why:** Always regenerate and validate before submission.

## 📋 Quick Reference

| Task | Repo | Command |
|------|------|---------|
| Edit source code | Main | `vim src/excalidraw_gen/components/...` |
| Generate libraries | Main | `uv run excalidraw-generate --theme default` |
| Run tests | Main | `pytest` |
| Commit source changes | Main | `git commit -m "feat: ..."` |
| Sync fork with upstream | Fork | `git fetch upstream && git merge upstream/main` |
| Create PR branch | Fork | `git checkout -b add-feature` |
| Copy submission files | Fork | `cp ../submission/*.excalidrawlib libraries/` |
| Submit PR | Fork | `gh pr create --repo excalidraw/excalidraw-libraries` |

## 🎯 Summary

**Development Workflow:**
1. Edit code in main repo
2. Generate libraries to `output/`
3. Copy validated files to `submission/`
4. Copy from `submission/` to fork
5. Submit PR from fork to excalidraw-libraries

**Key Principle:**
> Main repo owns **source code**.
> Fork repo owns **submission to public catalog**.
> Never mix the two.

---

**Current Action Items:**

1. ✅ Keep nested structure OR move fork out (decide which)
2. ✅ Update .gitignore to prevent accidents
3. ✅ Create automation scripts
4. ✅ Document workflow clearly
5. ⚠️ Close premature PR #2431
6. ✅ Follow SUBMISSION_CHECKLIST.md for next submission
