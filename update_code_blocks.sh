#!/bin/bash

# Function to process a single file
process_file() {
    local file="$1"
    echo "Processing $file..."
    
    # Create a temporary file
    temp_file=$(mktemp)
    
    # Use awk to process the file
    awk '
    BEGIN { in_code_block = 0 }
    {
        if ($0 ~ /\[code language="swift"\]/) {
            print "```swift"
            in_code_block = 1
        } else if ($0 ~ /\[\/code\]/) {
            print "```"
            in_code_block = 0
        } else {
            print $0
        }
    }' "$file" > "$temp_file"
    
    # Replace original file with processed file
    mv "$temp_file" "$file"
}

# Process all markdown files in _posts directory
for file in _posts/*.md; do
    if grep -q '\[code language="swift"\]' "$file"; then
        process_file "$file"
    fi
done
