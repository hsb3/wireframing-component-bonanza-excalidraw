#!/bin/bash
# GitHub Fork & PR Helper for Excalidraw Library Submission
set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}================================================${NC}"
echo -e "${BLUE}   Excalidraw Library Submission Helper${NC}"
echo -e "${BLUE}================================================${NC}"
echo ""

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo -e "${YELLOW}⚠️  GitHub CLI (gh) not found.${NC}"
    echo ""
    echo "Installing gh CLI..."
    echo "Run: brew install gh"
    echo "Then: gh auth login"
    echo ""
    exit 1
fi

# Check if user is authenticated
if ! gh auth status &> /dev/null; then
    echo -e "${YELLOW}⚠️  Not authenticated with GitHub${NC}"
    echo "Run: gh auth login"
    exit 1
fi

echo -e "${GREEN}✓${NC} GitHub CLI authenticated"

# Step 1: Fork the repository
echo ""
echo -e "${BLUE}Step 1: Forking excalidraw-libraries...${NC}"

if gh repo view excalidraw/excalidraw-libraries &> /dev/null; then
    echo "Repository exists, checking for fork..."

    # Check if fork already exists
    GITHUB_USER=$(gh api user -q .login)
    if gh repo view "$GITHUB_USER/excalidraw-libraries" &> /dev/null; then
        echo -e "${GREEN}✓${NC} Fork already exists at $GITHUB_USER/excalidraw-libraries"
    else
        echo "Creating fork..."
        gh repo fork excalidraw/excalidraw-libraries --clone=false
        echo -e "${GREEN}✓${NC} Fork created"
    fi
else
    echo -e "${RED}❌ Could not access excalidraw/excalidraw-libraries${NC}"
    exit 1
fi

# Step 2: Clone fork if not already cloned
echo ""
echo -e "${BLUE}Step 2: Cloning your fork...${NC}"

REPO_DIR="excalidraw-libraries"
if [ -d "$REPO_DIR" ]; then
    echo -e "${GREEN}✓${NC} Repository already cloned"
    cd "$REPO_DIR"
    git fetch origin
else
    gh repo clone "$GITHUB_USER/excalidraw-libraries"
    cd "$REPO_DIR"
    echo -e "${GREEN}✓${NC} Repository cloned"
fi

# Step 3: Create branch
echo ""
echo -e "${BLUE}Step 3: Creating feature branch...${NC}"

BRANCH_NAME="add-shadcn-wireframe-kits"
git checkout main
git pull origin main

if git show-ref --verify --quiet "refs/heads/$BRANCH_NAME"; then
    echo -e "${YELLOW}Branch $BRANCH_NAME already exists, using it${NC}"
    git checkout "$BRANCH_NAME"
else
    git checkout -b "$BRANCH_NAME"
    echo -e "${GREEN}✓${NC} Created branch: $BRANCH_NAME"
fi

# Step 4: Copy library files
echo ""
echo -e "${BLUE}Step 4: Copying library files...${NC}"

USER_DIR="libraries/$GITHUB_USER"
mkdir -p "$USER_DIR"

cp ../submission/shadcn-wireframe-*.excalidrawlib "$USER_DIR/"
cp ../submission/shadcn-wireframe-*.png "$USER_DIR/"

echo -e "${GREEN}✓${NC} Copied 3 library files"
echo -e "${GREEN}✓${NC} Copied 3 preview images"

# Step 5: Update libraries.json
echo ""
echo -e "${BLUE}Step 5: Updating libraries.json...${NC}"

# Create a Python script to update libraries.json
cat > update_libraries.py << 'PYTHON_SCRIPT'
import json
from pathlib import Path

# Read existing libraries.json
with open('libraries.json', 'r') as f:
    data = json.load(f)

# Get GitHub username from environment
import os
github_user = os.environ.get('GITHUB_USER', 'hsb3')

# New library entries
new_libraries = [
    {
        "name": "shadcn Wireframe Kit (Default)",
        "description": "Hand-drawn grayscale wireframes for SaaS and AI apps. Includes frames, UI components, forms, charts, dashboards, and chat interfaces.",
        "author": "Henry Burden",
        "github": github_user,
        "source": "https://github.com/hsb3/wireframing-component-bonanza-excalidraw",
        "license": "MIT",
        "tags": ["wireframe", "ui", "saas", "dashboard", "forms", "mockup", "grayscale", "ai", "chat"],
        "id": f"{github_user}/shadcn-wireframe-default"
    },
    {
        "name": "shadcn Wireframe Kit (Carbon)",
        "description": "Enterprise wireframes based on IBM Carbon Design System. Dark theme with clean lines and monospace font for corporate applications.",
        "author": "Henry Burden",
        "github": github_user,
        "source": "https://github.com/hsb3/wireframing-component-bonanza-excalidraw",
        "license": "MIT",
        "tags": ["wireframe", "enterprise", "carbon", "dark-mode", "corporate", "dashboard", "data", "clean"],
        "id": f"{github_user}/shadcn-wireframe-carbon"
    },
    {
        "name": "shadcn Wireframe Kit (Warm)",
        "description": "Hand-drawn wireframes with warm color palette. Friendly, approachable style with earthy tones for consumer-facing applications.",
        "author": "Henry Burden",
        "github": github_user,
        "source": "https://github.com/hsb3/wireframing-component-bonanza-excalidraw",
        "license": "MIT",
        "tags": ["wireframe", "warm", "friendly", "consumer", "ui", "sketchy", "color"],
        "id": f"{github_user}/shadcn-wireframe-warm"
    }
]

# Check if libraries already exist
existing_ids = {lib.get('id') for lib in data.get('libraries', [])}
new_entries = [lib for lib in new_libraries if lib['id'] not in existing_ids]

if new_entries:
    if 'libraries' not in data:
        data['libraries'] = []
    data['libraries'].extend(new_entries)
    print(f"Added {len(new_entries)} new libraries")
else:
    print("Libraries already exist in libraries.json")

# Write back
with open('libraries.json', 'w') as f:
    json.dump(data, f, indent=2)
    f.write('\n')  # Add trailing newline

print("✓ libraries.json updated")
PYTHON_SCRIPT

GITHUB_USER="$GITHUB_USER" python3 update_libraries.py
rm update_libraries.py

echo -e "${GREEN}✓${NC} Updated libraries.json"

# Step 6: Commit changes
echo ""
echo -e "${BLUE}Step 6: Committing changes...${NC}"

git add "$USER_DIR/"
git add libraries.json

if git diff --cached --quiet; then
    echo -e "${YELLOW}No changes to commit (already committed?)${NC}"
else
    git commit -m "Add shadcn Wireframe Kits (Default, Carbon, Warm)

Three comprehensive wireframe libraries with 154 components each:

- shadcn Wireframe Kit (Default): Hand-drawn grayscale
- shadcn Wireframe Kit (Carbon): IBM Carbon Design System
- shadcn Wireframe Kit (Warm): Warm color palette

Each library includes:
- Device frames and layouts
- UI primitives (buttons, icons, badges)
- Form components
- Data visualization
- SaaS patterns
- AI/chat interfaces

Source: https://github.com/hsb3/wireframing-component-bonanza-excalidraw
License: MIT"

    echo -e "${GREEN}✓${NC} Changes committed"
fi

# Step 7: Push branch
echo ""
echo -e "${BLUE}Step 7: Pushing to your fork...${NC}"

git push -u origin "$BRANCH_NAME"
echo -e "${GREEN}✓${NC} Pushed to origin/$BRANCH_NAME"

# Step 8: Create pull request
echo ""
echo -e "${BLUE}Step 8: Creating pull request...${NC}"

PR_TITLE="Add shadcn Wireframe Kits (Default, Carbon, Warm)"
PR_BODY="# shadcn Wireframe Kits

Three comprehensive wireframe libraries with 154 components each, designed for SaaS and AI application mockups.

## Libraries Included

### 1. shadcn Wireframe Kit (Default)
- **Style**: Hand-drawn, sketchy grayscale
- **Use case**: Low-fidelity mockups, quick prototyping
- **Components**: 154 (frames, UI primitives, forms, charts, dashboards, chat UIs)

### 2. shadcn Wireframe Kit (Carbon)
- **Style**: IBM Carbon Design System (dark theme)
- **Use case**: Enterprise applications, data dashboards
- **Components**: 154 (same structure, clean aesthetic)

### 3. shadcn Wireframe Kit (Warm)
- **Style**: Warm color palette, friendly aesthetic
- **Use case**: Consumer-facing apps, approachable design
- **Components**: 154 (same structure, earthy tones)

## Component Hierarchy

- **Level 0**: Device frames + Layout primitives
- **Level 1**: Atoms (Typography, Icons, Buttons, Badges)
- **Level 2**: Form inputs
- **Level 3**: Modules (Cards, Nav, Charts) + App shells
- **Level 4**: SaaS patterns (Dashboards, Data tables)
- **Level 5**: AI components (Chat interfaces)

## Quality Checklist

- [x] Minimum 3 related items (154 per library)
- [x] Useful beyond personal use case
- [x] English-only content
- [x] Multi-element items properly grouped
- [x] Original work
- [x] Preview images included
- [x] Source repository provided
- [x] Open source (MIT License)

## Source

Repository: https://github.com/hsb3/wireframing-component-bonanza-excalidraw
License: MIT"

# Check if PR already exists
if gh pr view "$BRANCH_NAME" &> /dev/null; then
    echo -e "${YELLOW}Pull request already exists:${NC}"
    gh pr view "$BRANCH_NAME" --web
else
    gh pr create \
        --title "$PR_TITLE" \
        --body "$PR_BODY" \
        --base main \
        --head "$GITHUB_USER:$BRANCH_NAME" \
        --repo excalidraw/excalidraw-libraries

    echo -e "${GREEN}✓${NC} Pull request created!"
fi

# Step 9: Summary
echo ""
echo -e "${BLUE}================================================${NC}"
echo -e "${GREEN}✅ SUBMISSION COMPLETE!${NC}"
echo -e "${BLUE}================================================${NC}"
echo ""
echo "Your pull request has been submitted to excalidraw-libraries."
echo ""
echo "Next steps:"
echo "  1. View PR: gh pr view --web"
echo "  2. Monitor for feedback"
echo "  3. Respond to any requested changes"
echo ""
echo "Thank you for contributing to Excalidraw! 🎉"
echo ""

cd ..
