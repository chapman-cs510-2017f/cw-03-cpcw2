#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Name: Chelsea Parlett & Chris Watkins
# Student ID: 2298930 & 1450263
# Email: parlett@chapman.edu & watki115@mail.chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 3
###

from sequences import fibonacci
def main(local_argv):
    #print("the arg is ", local_argv)
    try:
        local_argv = int(local_argv)
    except:
        print("Not a num")
    print(fibonacci(local_argv)[-1])
    return(fibonacci(local_argv)[-1])
    


if __name__ == "__main__":
    # This block only executes if the script is run as a standalone
    # program from the command line. It is not run when imported as
    # a module.
    
    # It is convention to call a single function here if possible
    # This function should be defined above and house all code to be
    # executed. Note that sys.argv will contain all commandline options.
    # The getopt module may also be helpful for more ambitious programs.
    import sys
    #print("the arg is ", sys.argv)
    main(sys.argv[1])



