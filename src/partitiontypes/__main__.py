import os
import sys
import json
import argparse

from partitiontypes.Controller import Controller

from partitiontypes.util.Crawler import Crawler

def main(args_=None):
    """The main routine."""
    if args_ is None:
        args_ = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--update", "-u", required=True, action="store_true", help="Updates the partition types")
    args = parser.parse_args()

    c = Controller()

    c.printHeader()

    if(args.update):
        crawler = Crawler()
        ids = crawler.get()

        print("")
        print("Update successful!")
        print("Number of IDs: " + str(len(ids)))
        print("")
        
        j = json.dumps([id.__dict__ for id in ids], indent=4)

        path = os.path.join(os.path.dirname(__file__), "data", "partitiontypes.json")
        with open(path, "w") as outfile:
            outfile.write(j)

    c.printExecutionTime()

if __name__ == "__main__":
    sys.exit(main())
