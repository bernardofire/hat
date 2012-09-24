import os
import sys

def cat(argv):
    try:
        sys.exit(os.system("pygmentize -f terminal %s" % argv[1]))
    except KeyboardInterrupt:
        sys.exit(1)
