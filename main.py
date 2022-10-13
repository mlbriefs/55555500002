import argparse
from sys import argv

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--price", type=int, required=True)
    parser.add_argument("--water", type=float, required=True)
    parser.add_argument("--food", type=str, required=True)
    parser.add_argument("--drink", type=str, required=True)
    parser.add_argument("--size", type=bool, required=True)
    parser.add_argument("--place", type=str, required=True)
    parser.add_argument("--why", type=str, required=True)
    parser.add_argument("--bigger", type=int, required=True)
    parser.add_argument("--kingcrab", type=bool, required=True)

    args = parser.parse_args(argv[1:])
    def printarg(name, arg):
        print(f"Argument {name} has type {type(arg)} and evaluates to {arg}")
    printarg(args.price)
    printarg(args.water)
    printarg(args.food)
    printarg(args.drink)
    printarg(args.size)
    printarg(args.place)
    printarg(args.why)
    printarg(args.bigger)
    printarg(args.kingcrab)
