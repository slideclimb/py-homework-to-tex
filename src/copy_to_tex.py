import os
import sys
import re
from pathlib import Path
from subprocess import call
from definitions import ROOT_DIR


def is_line_comment(next):
    return '#' in next


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
    # parts = False
    # figures = []
    #
    # lines = py.readlines()
    # pyconsole = False
    # for line in lines:
    #     # The first part begins.
    #     if '# part a' in line:
    #         # The first part also has to include the '\begin{parts}'.
    #         tex.write(pyend + begin_parts + '\\part\n')
    #         parts = True
    #         pyconsole = False
    #         if not is_line_comment(lines[lines.index(line) + 1]):
    #             tex.write(pybegin)
    #             figures = []
    #             pyconsole = True
    #     # A new part begins.
    #     elif re.match('# part [a-z]', line):
    #         tex.write(pyend)
    #         # Print all the figures from this part.
    #         for fig in figures:
    #             fig_print(tex, fig)
    #         # Start a new part.
    #         tex.write('\\part\n')
    #         pyconsole = False
    #         if not is_line_comment(lines[lines.index(line) + 1]):
    #             tex.write(pybegin)
    #             figures = []
    #             pyconsole = True
    #     # There is a comment which can be printed as tex.
    #     elif '#' in line and not pyconsole:
    #         # Assume that this always comes when a pyconsole environment has already been closed.
    #         tex.write(line[2:])
    #         # If the next line is not a comment, start a pyconsole environment.
    #         if not is_line_comment(lines[lines.index(line) + 1]):
    #             tex.write(pybegin)
    #             figures = []
    #             pyconsole = True
    #     # We are in python mode and print everything.
    #     else:
    #         # If the first line of the file is python, we have to start a pyconsole
    #         # environment.
    #         if lines.index(line) == 0:
    #             tex.write(pybegin)
    #             pyconsole = True
    #         # If line saves figure, add its name to the figures list so it can be
    #         # printed.
    #         if line.__contains__('filename='):
    #             figures.append(line.split("'")[1])
    #         tex.write(line)
    #
    # tex.write(pyend)
    # if parts:
    #     tex.write(end_parts)
    return tex


if __name__ == '__main__':
    SET = 'test-set'

    dirname = os.path.dirname(__file__)
    parent = Path(dirname).parent

    pybegin = '\\begin{pyconsole}\n'
    pyend = '\\end{pyconsole}\n\n'
    begin_parts = '\\begin{parts}\n'
    end_parts = '\\end{parts}\n'

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
