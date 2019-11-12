from SampleDir.sample import Sample


def test_add():
    sample = Sample()
    assert (sample.add(x=1, y=10) == 11)
