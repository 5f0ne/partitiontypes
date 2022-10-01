# Description

Provides values to identify the partition type within a master boot record.

# Installation

`pip install partitiontypes`

# Usage

**From command line:**

`python -m partitiontypes  --update`

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--update | -u | Bool | - | Updates the current list of partition ids |

**Programmatically:**

```python
from partitiontypes.PartitionTypes import PartitionTypes

p = PartitionTypes()

result = p.getIds("07")

# Result:
# [
#     PartitionId(id=07, description= OS/2 IFS (e.g., HPFS)), 
#     PartitionId(id=07, description= Windows NT NTFS), 
#     PartitionId(id=07, description= exFAT), 
#     PartitionId(id=07, description= Advanced Unix), 
#     PartitionId(id=07, description= QNX2.x pre-1988)
# ]
```


# Example

The package includes a list of IDs per default. If you want to have the newest version use the following command:

`python -m partitiontypes --update`

```
################################################################################

Partition Types by 5f0
Provides values to identify the partition type within a master boot record      

Current working directory: /path/to/partitiontypes

 Datetime: 01/01/1970 16:17:18

################################################################################

Update successful!
Number of IDs: 273

################################################################################

Execution Time: 0.583953 sec
```

# Credits

The IDs are based on the list of [Prof. Dr. Brouwer](https://www.win.tue.nl/~aeb/). Thank you for your permission to use it.

You can find the original [here](https://www.win.tue.nl/%7Eaeb/partitions/partition_types-1.html).


# License

MIT