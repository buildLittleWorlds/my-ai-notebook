#!/bin/bash

echo "Running all aggregating scripts..."
echo "=================================="

# Run the structural files aggregator (from root directory)
echo "1. Running structural files aggregator..."
./aggregate-structural-files.sh

# Run the blog posts aggregator (from _posts directory)
echo "2. Running blog posts aggregator..."
cd _posts && ./aggregate-blog-posts.sh && cd ..

# Run the romantic kit aggregator (from _romantic directory)  
echo "3. Running romantic kit aggregator..."
cd _romantic && ./aggregate-romantic-kit.sh && cd ..

# Run the AI hermeneutics aggregator (from _ai_hermeneutics directory)
echo "4. Running AI hermeneutics aggregator..."
cd _ai_hermeneutics && ./aggregate-ai-hermeneutics.sh && cd ..

# Run the archive aggregator (from _archive directory)
echo "5. Running archive aggregator..."
cd _archive && ./aggregate-archive.sh && cd ..

# Run the debate aggregator (from _debate directory)
echo "6. Running debate aggregator..."
cd _debate && ./aggregate-archivists-debate.sh && cd ..

echo "=================================="
echo "All aggregating scripts completed!"
echo "Output files are in aggregated-md-files/"
echo ""
echo "Generated files:"
ls -la aggregated-md-files/