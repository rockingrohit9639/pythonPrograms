import sys
import argparse

def calc(args):
    if args.o == 'add':
        return args.x + args.y
    elif args.o == 'sub':
        return args.x - args.y
    elif args.o == 'mul':
        return args.x * args.y
    elif args.o == 'div':
        return args.x / args.y
    else:
        return "Something went wrong."


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x',
                        type=float,
                        default=1.0,
                        help="Enter number 1. Contact Rohit for more"
                        )
    parser.add_argument('--y',
                        type=float,
                        default=2.0,
                        help="Enter number 2. Contact Rohit for more"
                        )
    parser.add_argument('--o',
                        type=str,
                        default='add',
                        help="Enter operation. Contact Rohit for more"
                        )
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
