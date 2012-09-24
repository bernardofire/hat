import os
import sys

def cat(argv):
    try:
        args = argv[1::]
        [os.system("pygmentize -f terminal %s" % arg) for arg in args]
    except KeyboardInterrupt:
        sys.exit(1)
