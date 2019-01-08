#!/bin/bash
for var in "$@"; do
    echo "$var"
done | sort | awk '
  BEGIN {
    c = 0;
  }
  $1 ~ /^[0-9]*(\.[0-9]*)?$/ {
    a[c++] = $1;
  }
  END {
    if( (c % 2) == 1 ) {
      median = a[ int(c/2) ];
    } else {
      median = ( a[c/2] + a[c/2-1] ) / 2;
    }
    OFS="\t";
    print median, a[0], a[c-1];
  }
'
