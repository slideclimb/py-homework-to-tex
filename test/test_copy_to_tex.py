from copy_to_tex import transform_to_tex


def test_copy_comments(datadir):
    input_file = datadir / "input/comments.py"
    output_file = datadir / "output/comments.tex"
    assert transform_to_tex(input_file).read_text() == output_file.read_text()
