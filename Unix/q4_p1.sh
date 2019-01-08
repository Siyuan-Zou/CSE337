#!/bin/bash
cd "$1"
echo 'Current Shell is: '$SHELL
printf 'Current directory is: ' && pwd
echo 'Home directory is: '$HOME
echo ' '
echo '—5 most recently modified non-empty subdirectories—'
find . -mindepth 1 -maxdepth 1 -not -empty -type d | head -n 5
echo ' '
echo '—Files in last 45 minutes'
find . -maxdepth 1 -type f -mmin -45 -size +1000M
echo ' '
echo '======================================================================'
