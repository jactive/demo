package Circle;

use base qw(Shape);

sub new {
	my ($clazz, $name, $radius) = @_;
	my $self = $clazz->SUPER::new($name);
	$self->{radius} = $radius;
	$self;
}

sub get_radius {
	$_[0]->{radius};
}

1;
