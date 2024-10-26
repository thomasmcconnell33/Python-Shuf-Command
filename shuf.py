#!/usr/local/cs/bin/python3
import random, sys
import argparse

class randline:
    def __init__(self, filename):
        f = open(filename, 'r')
        self.lines = f.readlines()
        f.close()

    def chooseline(self):
        return random.choice(self.lines)

    def shuffle_list(self):
        newlist = random.sample(self.lines, len(self.lines))
        return newlist
def main():
    version_msg = "%prog 2.0"
    usage_msg = """%prog [OPTION]... FILE

Output randomly selected lines from FILE."""

    parser = argparse.ArgumentParser(description="Write a random permutation of the input lines to standard output.")
    group = parser.add_mutually_exclusive_group()
    
    parser.add_argument("-n", "--head-count",
                      action="store", dest="numlines",
                      help="output NUMLINES lines (default 1)")
    group.add_argument("-e", "--echo",
                        action="store", nargs="*",
                        help="treat each ARG as an input line")
    group.add_argument("-i", "--input-range",
                        action="store", dest="numrange",
                        help="range of numbers")
    parser.add_argument("-r", "--repeat",
                        action="store_true")
    #group.add_argument("inputfile", nargs="?",
     #                    help="input file name")
    
    args, rest = parser.parse_known_args()
    if args.numlines is not None:
        numlines = int(args.numlines)
    if args.numlines is not None and numlines < 0:
        print(f"shuf: invalid line count: '{numlines}'")
        sys.exit(1)
    for i in rest:
        if i.startswith('-'):
            print(f"Error: Invalid argument '{i}'.")
            sys.exit(1)
    #print(args.echo)
    if args.echo is not None:
        
        combinedlist = args.echo + rest

        random.shuffle(combinedlist)
        if args.numlines is None:
            length = len(combinedlist)
        else:
            length = min(len(combinedlist), numlines)
        if args.repeat:
            if args.numlines is None:
                while True:
                    print(random.choice(combinedlist))
            for index in range(numlines):
                print(random.choice(combinedlist))
        else:
            for index in range(length):
                print(combinedlist[index])
    elif args.numrange is not None:
        start, end = map(int, args.numrange.split('-'))
        integer_list = list(range(start, end+1))
        random.shuffle(integer_list)

        if args.numlines is None:
            length = len(integer_list)
        else:
            length = min(len(integer_list), numlines)

        if args.repeat:
            if args.numlines is None:
                while True:
                    print(random.choice(integer_list))
            for index in range(numlines):
                print(random.choice(integer_list))
        else:
            for index in range(length):
                print(integer_list[index])
    else:
        if (len(rest) != 1):
            print("shuf: extra operand")
            print("Try 'shuf --help' for more information.")
            sys.exit(1)
        input_file = rest[0]
        if args.numlines is None:
            with open(input_file, 'r') as file:
                lines = file.readlines()
                numlines = len(lines)
        else:
            numlines = int(args.numlines)

        try:
            generator = randline(input_file)
            if not args.repeat:
                shuffled_list = generator.shuffle_list()
                for index in range(numlines):
                    print(shuffled_list[index], end='')
   
            else:
                if args.numlines is None:
                    while True:
                        sys.stdout.write(generator.chooseline())
                for index in range(numlines):
                    sys.stdout.write(generator.chooseline())
        except IOError as err:
            parser.error("I/O error({0}): {1}".
                     format(err.errno, err.strerror))


if __name__ == "__main__":
    main()

