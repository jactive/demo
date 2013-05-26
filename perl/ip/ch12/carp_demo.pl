#!/home/cydoo/local/perl/bin/perl -w

use Carp;
use strict;
use 5.10.0;

sub raise_carp {
   carp 'raise carp intentional.';
}

sub raise_warn {
   warn 'raise warn intentional.';
}

sub raise_croak {
   croak 'raise croak intentional.';
}
say "\n", '* ' x 20, ' START ', '* ' x 20;
raise_warn;
say '- ' x 20;
raise_carp;
say '- ' x 20;
raise_croak;
say '- ' x 20;
