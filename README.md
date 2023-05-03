# Heart Generator
This is a simple code to draw a heart. You can send this to your crush and steal their heart.

## How to run
This uses NumPy library. Install it by
```
pip install numpy
```
or by any other way that is suitable in your environment. This program uses the standard module Turtle, which depends on tkinter, tkinter may not work because Tcl/Tk is not installed, which often happens if you are using pyenv.

If you have Python installed on your computer, go to the directory you have cloned this code on Terminal and run
```
python main.py
```

## How to make it into a package
```
pyinstaller main.py --onefile --noconsole
```
after installing `pyinstaller` library.
