package Shape;

sub new {
	my ($clazz, $name) = @_;
	bless {name => $name}, $clazz;
}

sub to_str {
  "[Shape Name] $_[0]->{name}"
}

1;
