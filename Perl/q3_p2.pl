#!/usr/bin/perl
use strict;
use warnings;

#part2
print "Part2\n";
my %revenue =  (Jan => 4840, Feb => 4340, Mar => 3900, Apr => 4330, 
				May => 3090, Jun => 3660, Jul => 3520, Aug => 3280, 
				Sep => 4130, Oct => 3690, Nov => 4260, Dec => 4800);
				
my %month_ref =(Jan => 0, Feb => 1, Mar => 2, Apr => 3, 
				May => 4, Jun => 5, Jul => 6, Aug => 7, 
				Sep => 8, Oct => 9, Nov => 10, Dec => 11);
				
my %rev_month_ref = reverse %month_ref;
				
my @revenue_keys = keys %revenue;

print "Enter the initial month: ";
	my $initial_month = <>;
	chomp $initial_month;
	$initial_month = ucfirst(lc($initial_month));

until (contains($initial_month, [@revenue_keys])) {
	print "Re-enter the initial month: ";
		$initial_month = <>;
		chomp $initial_month;
		$initial_month = ucfirst(lc($initial_month));
}
	
print "Enter the final month: ";
	my $final_month = <>;
    chomp $final_month;
	$final_month = ucfirst(lc($final_month));
	
until (contains($final_month, [@revenue_keys]) && $month_ref{$final_month} >= $month_ref{$initial_month}) {
	print "Re-enter the final month: ";
		$final_month = <>;
		chomp $final_month;
		$final_month = ucfirst(lc($final_month));
}
my $month_start_index = $month_ref{$initial_month};
my $month_end_index = $month_ref{$final_month};

my $cuml_revenue=0;
for(my $i=$month_start_index; $i<=$month_end_index; $i++){
	my $month_key = $rev_month_ref{$i};
	$cuml_revenue += $revenue{$month_key};
}
print "The cumulative revenue is: $cuml_revenue";
print "\n";

sub contains{
	my $str = $_[0];
	my $arr = $_[1];
	
	foreach my $ele (@{$arr}){
		if($ele eq $str){
			return 1;
		}
	}
	return 0;
}