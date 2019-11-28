[![Build Status](https://travis-ci.com/slideclimb/py-homework-to-tex.svg?branch=master)](https://travis-ci.com/slideclimb/py-homework-to-tex)

Python template project specifically for handing in python homework in latex. 

## Before you start
Make sure you have Python, MiKTeX (or texlive), SumatraPDF, and Pycharm with the TeXiFy IDEA plugin installed. If you don't, install what's missing and reboot (if you're only missing TeXiFy, install that and restart PyCharm).

You can use this template project or create a fresh Python project yourself.
In that case, make sure you

- copy the `definitions.py` and `src/copy_to_tex.py`
- create a folder `src/pytex`
- install the `pygments` package in your virtual environment (in PyCharm open the Terminal and type `pip install pygments`)
- place your tex files in the `src` folder

See the `main.tex` file for examples on how to include the python in your tex. Note that we are using the `exam` class to be able to use the `questions` environment.

## Creating the run configurations
We will create three run configurations.

1. Compiling the tex file. 
    - Open your tex file in PyCharm, and hit <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>F10</kbd>. This should create a configuration to compile this tex file. 
    - Click on the run configurations drop down (next to the green play button) and select 'edit run configurations'
    - Give this run configuration a more useful name, e.g., `[tex] main` so you know it's just compiling you tex.
    
2. Compiling the tex file when it contains Python.
    - In a command prompt, run `where pythontex` (or `which pythontex` if you're on linux).
    - Open the edit run configurations dialog.
    - Create a new run configuration that looks like the previous configuration (1/`[tex] main`).
    - At the bottom of this configuration, in the before launch section, add the following
        1. "run another configuration" and select the `[tex] main` configuration.
        2. "run external tool" with the following settings:
            - Program: The path to `pythontex`, which is the output of `where pythontex`
            - Arguments: `main.tex`, this will feed the tex file we're compiling to pythontex (don't forget to change this when changing the tex file).
            - Working directory: The directory of the tex file. In this project that is the `src` folder.
            
3. Copying the Python files to tex and compiling the latex.
    - Open the `src/copy_to_tex.py` file and hit <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>F10</kbd> to create a run configuration that will just copy the python to latex.
    - Go to the run configurations dialog, and copy the run configuration that compiled tex including pythontex.
    - In the before launch section of this copied configuration, add the `copy_to_tex.py` configuration.
    
## About these run configurations
Usually you will only need run config 2. The only case you need run config 3 is when you have altered your python files and you need to generate the latex from these files. After generating these once, you can alter the tex files and compile your altered version with run config 2. 

## What does `copy_to_tex.py` do?
This python script copies all the python files in the root directory to the `src/pytex/` folder, surrounding the code by `\begin{pyconsole} ... \end{pyconsole}`, so we can input it in our tex file.
It also includes parts of the questions, i.e., when we have a line comment in the py file that is of the form `# part a`, it inputs `\part` in the generated tex file.
