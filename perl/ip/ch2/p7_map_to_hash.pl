#!/usr/bin/perl

my @a = (1, 3, 4, 12, 14, 64);
my %m = map {
   my @d = split //, $_;
   if ($d[-1] == 4) {
      print @d.join(","), "\n";
      @d;
   } else {
      ();
   }
} @a;

print "= " x 8, "\n";
print %m, "\n";
