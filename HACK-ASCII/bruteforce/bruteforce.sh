#!/usr/bin/env bash

puzzle_id="`cat ../puzzleid.txt`"

for line in {1..500}; do
  echo "Trying line ${line}..."

  response="`curl "http://4841434b.com/check?guess_line=$line&puzzle_id=$puzzle_id" | tee "response${line}.html" | grep "Wrong"`"

  if [ -z "$response" ]; then
    cat "response${line}.html"
    echo "line: $line"
    exit 0
  else
    echo "Nope. Sleeping..."
    sleep 4
  fi
done

exit 1
