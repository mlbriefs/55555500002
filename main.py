import argparse
from sys import argv

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--price", type=int, required=True)
    parser.add_argument("--water", type=float, required=True)
    parser.add_argument("--food", type=str, required=True)
    parser.add_argument("--drink", type=str, required=True)
    parser.add_argument("--size", type=str, required=True)
    parser.add_argument("--place", type=str, required=True)
    parser.add_argument("--why", type=str, required=True)
    parser.add_argument("--bigger", type=int, required=True)
    parser.add_argument("--kingcrab", type=str, required=True)

    args = parser.parse_args(argv[1:])
    def printarg(name, arg):
        print(f"Argument {name} has type {type(arg)} and evaluates to {arg}")
    printarg("price", args.price)
    printarg("water", args.water)
    printarg("food", args.food)
    printarg("drink", args.drink)
    printarg("size", args.size)
    printarg("place", args.place)
    printarg("why", args.why)
    printarg("bigger", args.bigger)
    printarg("kingcrab", args.kingcrab)
    
    # To get a true boolean from a checkbox, do: args.size == "true"
