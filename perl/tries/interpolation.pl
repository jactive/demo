#use strict;
use warnings;

my $f = sub {
  "haha\n";
};
print qq|${\&$f()} \n|;
print qq|@{[ &$f() ]} \n|;
