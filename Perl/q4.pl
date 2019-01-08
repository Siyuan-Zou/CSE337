#!/usr/bin/perl
use strict;
use warnings;
use Cwd;
my $dir = getcwd;

use Cwd 'abs_path';

my $directory = './features';
mkdir $directory unless -d $directory;

#Creates the N-files
print "Files have been created!\n";
for(my $i=0; $i<=9; $i++){
	open NFILE, ">>", "$directory/$i-features.txt" or die "Can't open input file: $!";
	my $abs_path = abs_path("$directory/$i-features.txt");
	print "$abs_path\n";
	close NFILE;
}

#Read from features.txt and add to specify file
my $input = $ARGV[0];

open INPUT, "<", $input or die "Can't open input file: $!";

while (my $lines = <INPUT>) { # continue reading the rest, one line at a time
   chomp $lines;
   my @line_arr = split(",", $lines);
   my $i = $line_arr[1];
   open FILE, ">>", "$directory/$i-features.txt" or die "Can't open input file: $!";
   print FILE "$line_arr[0]\n";
   close FILE;
}
close INPUT;