#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sequences import fibonacci
def main(local_argv):
    print(fibonacci(local_argv[0])[-1])
if __name__ == "__main__":
    # This block only executes if the script is run as a standalone
    # program from the command line. It is not run when imported as
    # a module.
    
    # It is convention to call a single function here if possible
    # This function should be defined above and house all code to be
    # executed. Note that sys.argv will contain all commandline options.
    # The getopt module may also be helpful for more ambitious programs.
    import sys
    main(sys.argv[0])

