#!/bin/bash
echo Enter a sentence please.
read sentence
tr -cd 'k' <<<"$sentence" | wc -c 
