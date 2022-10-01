import requests

from partitiontypes.util.PartitionId import PartitionId

class Crawler():
    def __init__(self) -> None:
        pass

    def get(self):
        response = requests.get("https://www.win.tue.nl/~aeb/partitions/partition_types-1.html")
        
        ids = []
        lines = response.text.split("\n")

        for line in lines:
            if("<DT>" in line or "<dt>" in line):
                result = line.replace("<DT><B>", "").replace("</B><DD>", "").split(" ")
                ids.append(PartitionId(result[0].upper(), " ".join(result[i] for i in range(1, len(result)))))

        return ids