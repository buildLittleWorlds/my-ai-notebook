#!/bin/bash

# Script to aggregate all markdown files from a Jekyll collection into one file
# Usage: ./aggregate-markdown.sh [collection_name]
# Example: ./aggregate-markdown.sh kits

COLLECTION=$1
OUTPUT_DIR="aggregated-collections"

if [ -z "$COLLECTION" ]; then
    echo "Usage: $0 [collection_name]"
    echo "Available collections:"
    ls -d _*/ | sed 's/^_//' | sed 's/\///'
    exit 1
fi

if [ ! -d "_$COLLECTION" ]; then
    echo "Error: Collection '_$COLLECTION' does not exist"
    echo "Available collections:"
    ls -d _*/ | sed 's/^_//' | sed 's/\///'
    exit 1
fi

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

OUTPUT_FILE="$OUTPUT_DIR/${COLLECTION}-all.md"

echo "Aggregating markdown files from _$COLLECTION/ into $OUTPUT_FILE"

# Start with a header
cat > "$OUTPUT_FILE" << EOF
# All $COLLECTION Files

*This file contains all markdown files from the _$COLLECTION/ collection, aggregated on $(date)*

---

EOF

# Counter for files processed
file_count=0

# Process each markdown file in the collection
for file in "_$COLLECTION"/*.md; do
    if [ -f "$file" ]; then
        filename=$(basename "$file")
        echo "Processing: $filename"
        
        # Add file separator and filename
        cat >> "$OUTPUT_FILE" << EOF

<!-- ============================================================ -->
<!-- File: $filename -->
<!-- ============================================================ -->

EOF
        
        # Add the content of the file
        cat "$file" >> "$OUTPUT_FILE"
        
        # Add spacing after each file
        echo -e "\n\n" >> "$OUTPUT_FILE"
        
        ((file_count++))
    fi
done

echo "Complete! Processed $file_count files into $OUTPUT_FILE"
echo "File size: $(wc -c < "$OUTPUT_FILE") bytes"