#!/home/cydoo/local/perl/bin/perl -w

use strict;
use 5.10.0;
{
  package FirstClazz;

  sub new {
    my ($clazz, $name, $desc) = @_;
    my $self = { name => $name, desc => $desc };
    bless $self, $clazz;
  }

  sub name {
    $_[0]->{name};
  }

  sub desc {
    my $self = shift;
    $self->{desc};
  }

  sub introduce {
    my $self = shift;
    "Hello, this is " . $self->name .
    ". Here is my short description: " . $self->desc;
  }
}

{
  package SimpleClazz;
  sub new {
    my ($clazz, $name) = @_;
    # The first argument of bless must be a reference,
    # otherwise, it raise the exception: Can't bless
    # non-reference value
    bless \$name, $clazz;
  }

  sub sayhi {
    my $self = shift;
    "Hi, I am " . $$self;
  }
}

my $first_object = FirstClazz->new('Cuper', 'I am the first perl object.');
say $first_object->introduce;

my $simple_object = SimpleClazz->new('Sam');
say $simple_object->sayhi;
