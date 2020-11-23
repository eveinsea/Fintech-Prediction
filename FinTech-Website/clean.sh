#!/bin/bash
echo "Clean pyc and log file"
find . -name "*.log" -type f -print -exec /bin/rm -rf {} \;
find . -name "*.pyc" -type f -print -exec /bin/rm -rf {} \;
