#!/bin/bash

# SEO Audit Script
# Analyzes blog posts for missing SEO elements
# Usage: ./scripts/seo-audit.sh

echo "=========================================="
echo "SEO Audit for rshankar.com Blog Posts"
echo "=========================================="
echo ""

POSTS_DIR="_posts"
TOTAL_POSTS=$(ls -1 ${POSTS_DIR}/*.md 2>/dev/null | wc -l)

echo "📊 Total Posts: $TOTAL_POSTS"
echo ""

# Check for missing descriptions
echo "🔍 Checking Meta Descriptions..."
MISSING_DESC=$(grep -L "^description:" ${POSTS_DIR}/*.md 2>/dev/null | wc -l)
WITH_DESC=$((TOTAL_POSTS - MISSING_DESC))
DESC_PERCENT=$((WITH_DESC * 100 / TOTAL_POSTS))
echo "   ✅ Posts with descriptions: $WITH_DESC ($DESC_PERCENT%)"
echo "   ❌ Posts missing descriptions: $MISSING_DESC"
echo ""

# Check for missing images
echo "🖼️  Checking Featured Images..."
MISSING_IMG=$(grep -L "^image:\|^og_image:" ${POSTS_DIR}/*.md 2>/dev/null | wc -l)
WITH_IMG=$((TOTAL_POSTS - MISSING_IMG))
IMG_PERCENT=$((WITH_IMG * 100 / TOTAL_POSTS))
echo "   ✅ Posts with images: $WITH_IMG ($IMG_PERCENT%)"
echo "   ❌ Posts missing images: $MISSING_IMG"
echo ""

# Check for missing permalinks
echo "🔗 Checking Permalinks..."
MISSING_PERM=$(grep -L "^permalink:" ${POSTS_DIR}/*.md 2>/dev/null | wc -l)
WITH_PERM=$((TOTAL_POSTS - MISSING_PERM))
PERM_PERCENT=$((WITH_PERM * 100 / TOTAL_POSTS))
echo "   ✅ Posts with permalinks: $WITH_PERM ($PERM_PERCENT%)"
echo "   ❌ Posts missing permalinks: $MISSING_PERM"
echo ""

# Check for excerpt separators
echo "✂️  Checking Excerpt Separators..."
MISSING_EXC=$(grep -L "<!--more-->" ${POSTS_DIR}/*.md 2>/dev/null | wc -l)
WITH_EXC=$((TOTAL_POSTS - MISSING_EXC))
EXC_PERCENT=$((WITH_EXC * 100 / TOTAL_POSTS))
echo "   ✅ Posts with excerpt separator: $WITH_EXC ($EXC_PERCENT%)"
echo "   ❌ Posts missing excerpt separator: $MISSING_EXC"
echo ""

# Check for tags
echo "🏷️  Checking Tags..."
MISSING_TAGS=$(grep -L "^tags:" ${POSTS_DIR}/*.md 2>/dev/null | wc -l)
WITH_TAGS=$((TOTAL_POSTS - MISSING_TAGS))
TAGS_PERCENT=$((WITH_TAGS * 100 / TOTAL_POSTS))
echo "   ✅ Posts with tags: $WITH_TAGS ($TAGS_PERCENT%)"
echo "   ❌ Posts missing tags: $MISSING_TAGS"
echo ""

# Check for categories
echo "📁 Checking Categories..."
MISSING_CATS=$(grep -L "^categories:" ${POSTS_DIR}/*.md 2>/dev/null | wc -l)
WITH_CATS=$((TOTAL_POSTS - MISSING_CATS))
CATS_PERCENT=$((WITH_CATS * 100 / TOTAL_POSTS))
echo "   ✅ Posts with categories: $WITH_CATS ($CATS_PERCENT%)"
echo "   ❌ Posts missing categories: $MISSING_CATS"
echo ""

# Calculate overall SEO score
TOTAL_CHECKS=$((WITH_DESC + WITH_IMG + WITH_PERM + WITH_EXC + WITH_TAGS + WITH_CATS))
MAX_CHECKS=$((TOTAL_POSTS * 6))
OVERALL_SCORE=$((TOTAL_CHECKS * 100 / MAX_CHECKS))

echo "=========================================="
echo "📈 Overall SEO Score: $OVERALL_SCORE%"
echo "=========================================="
echo ""

# Categorize score
if [ $OVERALL_SCORE -ge 80 ]; then
    echo "🟢 Excellent! Your posts have strong SEO coverage."
elif [ $OVERALL_SCORE -ge 60 ]; then
    echo "🟡 Good progress! Keep improving your SEO coverage."
elif [ $OVERALL_SCORE -ge 40 ]; then
    echo "🟠 Fair. Significant SEO improvements needed."
else
    echo "🔴 Needs Attention. Most posts missing critical SEO elements."
fi
echo ""

# Priority recommendations
echo "=========================================="
echo "🎯 Priority Actions:"
echo "=========================================="
echo ""

if [ $MISSING_DESC -gt 0 ]; then
    echo "1. Add meta descriptions to $MISSING_DESC posts"
    echo "   Priority: 🔴 HIGH"
    echo "   Impact: Improves search result click-through rates"
    echo ""
fi

if [ $MISSING_IMG -gt 0 ]; then
    echo "2. Add featured images to $MISSING_IMG posts"
    echo "   Priority: 🟡 MEDIUM"
    echo "   Impact: Better social media sharing"
    echo ""
fi

if [ $MISSING_PERM -gt 0 ]; then
    echo "3. Add permalinks to $MISSING_PERM posts"
    echo "   Priority: 🟡 MEDIUM"
    echo "   Impact: Better URLs for SEO"
    echo ""
fi

if [ $MISSING_EXC -gt 0 ]; then
    echo "4. Add excerpt separators to $MISSING_EXC posts"
    echo "   Priority: 🟢 LOW"
    echo "   Impact: Better post previews"
    echo ""
fi

# Show sample posts needing work
echo "=========================================="
echo "📝 Sample Posts Needing SEO Work:"
echo "=========================================="
echo ""
echo "Posts missing descriptions (showing 5):"
grep -L "^description:" ${POSTS_DIR}/*.md 2>/dev/null | head -5 | while read file; do
    filename=$(basename "$file")
    echo "   - $filename"
done
echo ""

echo "Posts missing images (showing 5):"
grep -L "^image:\|^og_image:" ${POSTS_DIR}/*.md 2>/dev/null | head -5 | while read file; do
    filename=$(basename "$file")
    echo "   - $filename"
done
echo ""

# Time estimates
echo "=========================================="
echo "⏱️  Time Estimates:"
echo "=========================================="
echo ""
echo "Quick Fix (description + permalink):"
echo "   ~$((MISSING_DESC * 5 / 60)) hours for descriptions"
echo ""
echo "Standard Fix (+ images + tags):"
echo "   ~$((MISSING_DESC * 10 / 60)) hours total"
echo ""
echo "Complete Optimization:"
echo "   ~$((MISSING_DESC * 30 / 60)) hours for full SEO"
echo ""

# Show recent posts status (2024-2025)
echo "=========================================="
echo "🆕 Recent Posts Status (2024-2025):"
echo "=========================================="
echo ""

RECENT_POSTS=$(ls ${POSTS_DIR}/2024-*.md ${POSTS_DIR}/2025-*.md 2>/dev/null | wc -l)
RECENT_WITH_DESC=$(grep -l "^description:" ${POSTS_DIR}/2024-*.md ${POSTS_DIR}/2025-*.md 2>/dev/null | wc -l)
RECENT_WITH_IMG=$(grep -l "^image:\|^og_image:" ${POSTS_DIR}/2024-*.md ${POSTS_DIR}/2025-*.md 2>/dev/null | wc -l)

if [ $RECENT_POSTS -gt 0 ]; then
    RECENT_DESC_PERCENT=$((RECENT_WITH_DESC * 100 / RECENT_POSTS))
    RECENT_IMG_PERCENT=$((RECENT_WITH_IMG * 100 / RECENT_POSTS))

    echo "Total recent posts: $RECENT_POSTS"
    echo "With descriptions: $RECENT_WITH_DESC ($RECENT_DESC_PERCENT%)"
    echo "With images: $RECENT_WITH_IMG ($RECENT_IMG_PERCENT%)"
else
    echo "No posts from 2024-2025 found."
fi
echo ""

echo "=========================================="
echo "📚 Next Steps:"
echo "=========================================="
echo ""
echo "1. Review: QUICK-SEO-FIX.md for batch update strategy"
echo "2. Use: _templates/new-post-template.md for new posts"
echo "3. Reference: SEO-GUIDELINES.md for complete documentation"
echo ""
echo "Run this script regularly to track your progress!"
echo ""
