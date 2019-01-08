#!/usr/bin/perl

#Part1
use strict;
use warnings;

print "Part1\n";

print "Enter String 1: \n";
	my $string1= <>;
    chomp $string1;
	
print "Enter String 2: \n";
	my $string2= <>;
    chomp $string2;

sub Replace_all {
	my $str1 = $_[0];
	my $str2 = $_[1];
	
	open INPUT, "< q2.in" or die "Can't open input file: $!";
	open OUTPUT, "> q2p1.out" or die "Can't open input file: $!";
	while (my $lines = <INPUT>) {
		chomp $lines;
		$lines =~ s/$str1/$str2/g;
		print OUTPUT "$lines\n";
	}
	close INPUT;
	close OUTPUT;
}
Replace_all($string1, $string2);
print "\n";

#Part2
print "Part2\n";

#assuming user inputs a number K, that is K>=1
print "Enter K: ";
	my $numK= <>;
    chomp $numK;

sub Remove_K {
	my $k = $_[0];
	
	open INPUT, "< q2.in" or die "Can't open input file: $!";
	open OUTPUT, "> q2p2.out" or die "Can't open input file: $!";
	my $remove_counter = 0;
	while (my $lines = <INPUT>) {
		chomp $lines;
		my @line_arr = split(" ", $lines);
		my $length = scalar @line_arr;
		if($length == $k){
			$remove_counter++;
		}else{
			print OUTPUT "$lines\n";
		}
	}
	
	if($remove_counter == 0){
		open OUTPUT, "> q2p2.out" or die "Can't open input file: $!";
		print OUTPUT "Oooh Nooo!\n";
	}
	close INPUT;
	close OUTPUT;
}
Remove_K($numK);
print "\n";