import os
import sys
import re
from pathlib import Path
from subprocess import call
from definitions import ROOT_DIR

SET = 'test-set'

dirname = os.path.dirname(__file__)
parent = Path(dirname).parent

pybegin = '\\begin{pyconsole}\n'
pyend = '\\end{pyconsole}\n'
begin_parts = '\\begin{parts}\n'
end_parts = '\\end{parts}\n'
tex_part = "\\part\n"


def fig_print(tex, figure):
    print(figure)
    tex.write("\\begin{figure}[h!]\n"
              + "\\centering\n"
              + "\\includegraphics[width=0.5\\textwidth]{"
              + figure[7:]
              + "}\n"
              + "\\caption{" + figure[19:-4] + "}"
              + "\\end{figure}\n")


def transform_to_tex(py, tex, *comment_escapes):
    """
    Writes the contents of a Python file to a LaTeX file.

    :param py: The Python file to read from.
    :param tex: The TeX file to write to.
    :param comment_escapes: List of comments that should be printed as Python comment.
    :return:
    """
    lines = py.readlines()
    parts = False
    pytex = False
    comment_escapes = [it + '\n' for it in comment_escapes]

    for line in lines:
        # Line begins a new part.
        if re.match(r'# part [a-z]\s*', line):
            if pytex:
                tex.write(pyend)
                pytex = False
            if not parts:
                tex.write(begin_parts)
                parts = True
            tex.write(tex_part)

        # Line is a comment that should be printed as regular tex.
        elif line.startswith("# "):
            if line[2:] in comment_escapes:
                if not pytex:
                    tex.write(pybegin)
                    pytex = True
                tex.write(line)
            else:
                # End the pytex environment if necesarry.
                if pytex:
                    tex.write(pyend)
                    pytex = False
                # Write the text of the comment to the tex file.
                tex.write(line[2:])

        # Line is a comment that should be printed as Python comment.
        elif line[2:] in comment_escapes:
            if not pytex:
                tex.write(pybegin)
                pytex = True
            tex.write(line)

        # Line is a Python line.
        elif not line.startswith("# ") and line != '\n':
            if not pytex:
                tex.write(pybegin)
                pytex = True
            tex.write(line)

    if pytex:
        tex.write(pyend)
    if parts:
        tex.write(end_parts)

    return tex


if __name__ == '__main__':
    # Create the directory to store the tex files if it doesn't exist.
    if not os.path.isdir(dirname + '/pytex'):
        os.mkdir(dirname + '/pytex')

    # Transform all python files to tex files we can include.
    for file in os.listdir(parent.__str__() + '/' + SET + '/'):
        if file.__str__()[-3:] == ".py":
            print(file)
            # Run all the python files so they generate the figures.
            # call(["python", ROOT_DIR + '/' + SET + '-py/' + file])
            pyfile = open(parent.__str__() + '/' + SET + '/' + file, 'r')
            texfile = open('pytex/' + file[0:-3] + '.tex', 'w+')
            print(transform_to_tex(pyfile, texfile))
            texfile.close()
            pyfile.close()
