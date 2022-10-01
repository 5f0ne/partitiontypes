import os
import sys
import json
import argparse

from partitiontypes.Controller import Controller
from partitiontypes.PartitionTypes import PartitionTypes

from partitiontypes.util.Crawler import Crawler

def main(args_=None):
    """The main routine."""
    if args_ is None:
        args_ = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--value", "-v", type=str, help="The id to be investigated as one byte hex")
    parser.add_argument("--update", "-u", action="store_true", help="Updates the partition types")
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

    if(args.value != None):
        p = PartitionTypes()
        ids = p.getIds(args.value)
        
        print("")
        print("Candidates for " + args.value.upper() + ":")
        print("")
        for id in ids:
            print("---> ID: " + id.id + "   Type: " + id.description)
    
    if(not args.update and args.value == None):
        print("")
        print("No hash value provided!")    
        print("")

    c.printExecutionTime()

if __name__ == "__main__":
    sys.exit(main())
