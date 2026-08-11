import os
import sys

print("PWD =", os.getcwd())
print("PATH =", sys.path)

from app.calculator import add

def test_add():
    assert add(10,20)==30