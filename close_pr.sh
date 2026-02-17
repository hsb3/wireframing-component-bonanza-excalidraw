#!/bin/bash
# Close PR #2431 with explanation

set -e

echo "Closing PR #2431 to excalidraw-libraries..."
echo ""
echo "This will:"
echo "1. Add a comment explaining why we're closing"
echo "2. Close the PR"
echo "3. NOT delete the branch (keep for reference)"
echo ""
read -p "Proceed? (y/N) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    echo "Cancelled."
    exit 1
fi

# Add comment
gh pr comment 2431 --repo excalidraw/excalidraw-libraries \
  --body-file pr_close_message.txt

# Close PR
gh pr close 2431 --repo excalidraw/excalidraw-libraries

echo ""
echo "✅ PR #2431 closed successfully"
echo ""
echo "Next steps:"
echo "1. Complete SUBMISSION_CHECKLIST.md"
echo "2. Regenerate all themes"
echo "3. Validate thoroughly"
echo "4. Resubmit when ready"
