from copy_to_tex import transform_to_tex


def get_input_output_tex(test_name, datadir):
    return open(str(datadir / ("input/" + test_name + ".py")), 'r'), \
           open(str(datadir / (test_name + "_test.tex")), 'w+'), \
           open(str(datadir / ("output/" + test_name + ".tex")), 'r')


def close_and_read(file):
    file.close()  # Needed to commit the write action.
    contents = open(file.name).read()
    file.close()
    return contents


def test_parts(datadir):
    py, tex, output = get_input_output_tex("parts", datadir)
    assert close_and_read(transform_to_tex(py, tex)) == output.read()


def test_comments(datadir):
    py, tex, output = get_input_output_tex("comments", datadir)
    assert close_and_read(transform_to_tex(py, tex)) == output.read()


def test_comments_part_a(datadir):
    py, tex, output = get_input_output_tex("comments_part_a", datadir)
    assert close_and_read(transform_to_tex(py, tex)) == output.read()


def test_comment_in_part(datadir):
    py, tex, output = get_input_output_tex("comment_in_part", datadir)
    assert close_and_read(transform_to_tex(py, tex)) == output.read()


def test_comment_escapes(datadir):
    py, tex, output = get_input_output_tex("comment_escapes", datadir)
    assert close_and_read(transform_to_tex(py, tex, "INPUT", "SCRIPT",
                                           "OUTPUT")) == output.read()

# TODO add test for figures
