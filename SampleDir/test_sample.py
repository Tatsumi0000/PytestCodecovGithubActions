from SampleDir.sample import Sample


def test_add():
    sample = Sample()
    assert (sample.add(x=1, y=10) == 11)


def test_sub():
    sample = Sample()
    assert (sample.sub(x=10, y=10) == 0)
