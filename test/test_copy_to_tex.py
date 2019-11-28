from copy_to_tex import transform_to_tex


def get_input_output_tex(test_name, datadir):
    return open(datadir / ("input/" + test_name + ".py"), 'r'), \
           open(datadir / (test_name + "_test.tex"), 'w+'), \
           open(datadir / ("output/" + test_name + ".tex"), 'r')


def test_comments(datadir):
    py, tex, output = get_input_output_tex("comments", datadir)
    assert transform_to_tex(py, tex).read() == output.read()


def test_comments_part_a(datadir):
    py, tex, output = get_input_output_tex("comments_part_a", datadir)
    assert transform_to_tex(py, tex).read() == output.read()


def test_comment_in_part(datadir):
    py, tex, output = get_input_output_tex("comment_in_part", datadir)
    assert transform_to_tex(py, tex).read() == output.read()


def test_comment_escapes(datadir):
    py, tex, output = get_input_output_tex("comment_escapes", datadir)
    assert transform_to_tex(py, tex, "INPUT", "SCRIPT", "OUTPUT").read() == output.read()



