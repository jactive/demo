use strict;
use warnings;

my $a = [ qw (a b c) ];
print join("  ", @$a), "\n";
$a = \qw(a b c);
print $$a, "\n";

my @b = (7, 8, 9);
print @b, " g\n";
print @{*b}, " d\n";
