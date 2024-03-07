#!/usr/bin/python3
from hidden_4 import *
for element in dir():
    if not element.startswith("_"):
        print(element)
if "__name__" == "__main__":
    main()
