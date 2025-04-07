#!/bin/bash
echo "Running ValidateService hook..."
STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:5000/health)
if [ $STATUS -ne 200 ]; then
  echo "Health check failed!"
  exit 1
else
  echo "Health check passed."
fi
