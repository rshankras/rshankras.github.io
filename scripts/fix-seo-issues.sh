#!/bin/bash

# SEO Issues Diagnostic Script
# Based on Ahrefs report findings

echo "========================================="
echo "SEO Issues Diagnostic Report"
echo "========================================="
echo ""

# 1. Find posts with meta descriptions that are too short (< 120 chars)
echo "1. Meta Descriptions Too Short (< 120 characters)"
echo "-------------------------------------------------"
short_desc_count=0
for file in _posts/*.md _pages/**/*.md; do
    if [ -f "$file" ]; then
        desc=$(grep "^description:" "$file" | sed 's/description: *"\?\(.*\)"\?/\1/' | tr -d '"')
        if [ ! -z "$desc" ]; then
            length=${#desc}
            if [ $length -lt 120 ]; then
                echo "$file: $length chars - \"${desc:0:80}...\""
                ((short_desc_count++))
            fi
        fi
    fi
done
echo "Total: $short_desc_count pages"
echo ""

# 2. Find posts with meta descriptions that are too long (> 155 chars)
echo "2. Meta Descriptions Too Long (> 155 characters)"
echo "-------------------------------------------------"
long_desc_count=0
for file in _posts/*.md _pages/**/*.md; do
    if [ -f "$file" ]; then
        desc=$(grep "^description:" "$file" | sed 's/description: *"\?\(.*\)"\?/\1/' | tr -d '"')
        if [ ! -z "$desc" ]; then
            length=${#desc}
            if [ $length -gt 155 ]; then
                echo "$file: $length chars - \"${desc:0:80}...\""
                ((long_desc_count++))
            fi
        fi
    fi
done
echo "Total: $long_desc_count pages"
echo ""

# 3. Find posts with titles that are too long (> 60 chars)
echo "3. Titles Too Long (> 60 characters)"
echo "-------------------------------------"
long_title_count=0
for file in _posts/*.md _pages/**/*.md; do
    if [ -f "$file" ]; then
        title=$(grep "^title:" "$file" | sed 's/title: *"\?\(.*\)"\?/\1/' | tr -d '"')
        if [ ! -z "$title" ]; then
            length=${#title}
            if [ $length -gt 60 ]; then
                echo "$file: $length chars - \"${title:0:60}...\""
                ((long_title_count++))
            fi
        fi
    fi
done
echo "Total: $long_title_count pages"
echo ""

# 4. Find posts missing descriptions
echo "4. Posts Missing Descriptions"
echo "------------------------------"
missing_desc_count=0
for file in _posts/*.md _pages/**/*.md; do
    if [ -f "$file" ]; then
        if ! grep -q "^description:" "$file"; then
            echo "$file"
            ((missing_desc_count++))
        fi
    fi
done
echo "Total: $missing_desc_count pages"
echo ""

# 5. Find posts missing permalinks
echo "5. Posts Missing Permalinks"
echo "----------------------------"
missing_permalink_count=0
for file in _posts/*.md _pages/**/*.md; do
    if [ -f "$file" ]; then
        if ! grep -q "^permalink:" "$file"; then
            echo "$file"
            ((missing_permalink_count++))
        fi
    fi
done
echo "Total: $missing_permalink_count pages"
echo ""

# Summary
echo "========================================="
echo "SUMMARY"
echo "========================================="
echo "Short descriptions (< 120 chars): $short_desc_count"
echo "Long descriptions (> 155 chars): $long_desc_count"
echo "Long titles (> 60 chars): $long_title_count"
echo "Missing descriptions: $missing_desc_count"
echo "Missing permalinks: $missing_permalink_count"
echo ""
echo "Next Steps:"
echo "1. ✅ Duplicate meta descriptions - FIXED (removed from head/custom.html)"
echo "2. Review short/long descriptions and update as needed"
echo "3. Review long titles and shorten to 50-60 characters"
echo "4. Add descriptions to posts missing them"
echo "5. Add permalinks to posts missing them"
echo ""
