import os
import json

from partitiontypes.util.PartitionId import PartitionId

class PartitionTypes():
    def __init__(self) -> None:
        path = os.path.join(os.path.dirname(__file__), "data", "partitiontypes.json")
        outfile = open(path, "r", encoding="utf8")
        dictList = json.load(outfile)
        outfile.close()

        self.partitionIds = [PartitionId(d["id"], d["description"]) for d in dictList]
        self.length = len(self.partitionIds)

    def getIds(self, id):
        matches = []

        for partitionId in self.partitionIds:
            if(partitionId.id == id):
                matches.append(partitionId)

        return matches
