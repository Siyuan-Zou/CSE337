#!/usr/bin/perl64

#part1
print "Part1\n";
use strict;
use warnings;

my $file = $ARGV[0];

open FILE, "<", $file or die "Can't open input file: $!";

while (my $lines = <FILE>) { # continue reading the rest, one line at a time
   chomp $lines;
   my @line_arr = split(",", $lines);
   my @word_arr = split(" ", $line_arr[0]);
   my $word_count = scalar @word_arr;
   print "$word_count\_$line_arr[1]\n";
}
close FILE;