#!/home/cydoo/local/perl/bin/perl -w

use strict;
use 5.10.0;
use FindBin qw($Bin);
use lib "$Bin/lib";

require Shape;
require Circle;

my $shape = Shape->new("Unknow Shape");
say $shape->to_str;
my $circle = Circle->new("Small Circle", 3.1);
say $circle->to_str;
say $circle->get_radius;
