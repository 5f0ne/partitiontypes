class PartitionId():
    def __init__(self, id, description) -> None:
        self.id = id
        self.description = description

    def __repr__(self) -> str:
        return f"PartitionId(id={self.id}, description={self.description})"