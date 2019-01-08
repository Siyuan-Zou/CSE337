#!/usr/bin/perl

#Part1
use strict;
use warnings;

print "Part1\n";

print "Enter Country Name: \n";
	my $country_name = <>;
    chomp $country_name;

my $country_count = 0;

open INPUT, "< collections.csv" or die "Can't open input file: $!";
my $description = <INPUT>;

my @art;

while (my $lines = <INPUT>) { # continue reading the rest, one line at a time
   chomp $lines;
   my $line_arr = [split(",", $lines)];
   push @art, $line_arr;
}

foreach my $sub_arr (@art){
	if (@{$sub_arr}[2] eq $country_name){
			$country_count++;
	}
}
print "Part1 output:\n";
print "Country Count: $country_count\n\n";
close INPUT;

#Part2
print "Part2\n";

my $smallest_year = @{$art[0]}[3];
my $biggest_year = @{$art[0]}[3];
my $id_of_biggest_year=@{$art[0]}[0];
my $id_of_smallest_year=@{$art[0]}[0];

foreach my $sub_arr (@art){
	if (@{$sub_arr}[3] < $smallest_year){
		$smallest_year = @{$sub_arr}[3];
		$id_of_smallest_year = @{$sub_arr}[0];
	}
	if (@{$sub_arr}[3] > $biggest_year){
		$biggest_year = @{$sub_arr}[3];
		$id_of_biggest_year = @{$sub_arr}[0];
	}
}
print "Part2 output:\n";
print "$id_of_smallest_year\n";
print "$id_of_biggest_year\n\n";

#Part3
print "Part3\n";

open INPUT1, "< collections.csv" or die "Can't open input file: $!";
my $description1 = <INPUT1>;
open INPUT2, "< m1.csv" or die "Can't open input file: $!";
my $description2 = <INPUT2>;
open INPUT3, "< m2.csv" or die "Can't open input file: $!";
my $description3 = <INPUT3>;

my @exhibition;
while (my $lines = <INPUT1>) { # continue reading the rest, one line at a time
   chomp $lines;
   push @exhibition, $lines;
}
while (my $lines = <INPUT2>) { # continue reading the rest, one line at a time
   chomp $lines;
   push @exhibition, $lines;
}
while (my $lines = <INPUT3>) { # continue reading the rest, one line at a time
   chomp $lines;
   push @exhibition, $lines;
}
@exhibition = sort @exhibition;

open OUTPUT, ">  exhibition.csv" or die "Can't open output file: $!";
print OUTPUT $description1;
foreach my $elements (@exhibition){
	print OUTPUT "$elements\n";
}
