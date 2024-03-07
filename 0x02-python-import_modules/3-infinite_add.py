#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    sum = 0
elif len(sys.argv) > 1:
    sum = 0
    for n in range(1, len(sys.argv)):
        sum += int((sys.argv[n]))
print(sum)

if "__name__" == "__main__":
    main()
