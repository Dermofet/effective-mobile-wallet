import datetime
from typing import List
from record import Record

class Recorder:
    """Class responsible for reading and writing records to a file."""
    
    def __init__(self, filepath: str):
        """Initialize the Recorder object.
        
        Args:
            filepath (str): The path to the file where records are stored.
        """
        self.filepath = filepath

    def write(self, records: List[Record]) -> None:
        """Write a list of records to the file.
        
        Args:
            records (List[Record]): List of records to be written to the file.
        """
        with open(self.filepath, "w", encoding="utf-8") as f:
            for record in records:
                f.write(f"{record.date},{record.category},{record.amount},{record.comment}\n")

    def read(self) -> List[Record]:
        """Read records from the file.
        
        Returns:
            List[Record]: List of records read from the file.
        """
        records = []
        with open(self.filepath, "r", encoding="utf-8") as f:
            for line in f:
                date, category, amount, comment = line.strip().split(",")
                record = Record(datetime.date.fromisoformat(date), category, float(amount), comment)
                records.append(record)
        return records
