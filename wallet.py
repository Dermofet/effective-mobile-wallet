import datetime
from typing import List, Tuple
from record import Record
from recorder import Recorder

class Wallet:
    """Class representing a financial wallet."""
    
    def __init__(self, filepath: str):
        """Initialize the Wallet object.
        
        Args:
            filepath (str): The path to the file where records are stored.
        """
        self.recorder = Recorder(filepath)
        self.records = self.recorder.read()

    def add_record(self, record: Record) -> None:
        """Add a record to the wallet.
        
        Args:
            record (Record): The record to be added to the wallet.
        """
        self.records.append(record)

    def change_record(self, new_record: Record) -> None:
        """Change a record in the wallet.
        
        Args:
            new_record (Record): The new record to replace the existing one.
        
        Raises:
            Exception: If the record to be changed is not found.
        """
        index = self.find_record_index(new_record.date, new_record.category, new_record.amount)
        if index is not None:
            self.records[index] = new_record
        else:
            raise Exception("Record not found")

    def find_records(self, category: str = None, date: datetime.date = None, amount: float = None) -> List[Record]:
        """Find records in the wallet based on filters.
        
        Args:
            category (str, optional): The category of the records to find. Defaults to None.
            date (datetime.date, optional): The date of the records to find. Defaults to None.
            amount (float, optional): The amount of the records to find. Defaults to None.
        
        Returns:
            List[Record]: A list of records that match the specified filters.
        """
        results = []
        for record in self.records:
            if (category is None or record.category == category) and \
               (date is None or record.date == date) and \
               (amount is None or record.amount == amount):
                results.append(record)
        return results

    def find_record_index(self, date: datetime.date, category: str, amount: float) -> int:
        """Find the index of a record in the wallet.
        
        Args:
            date (datetime.date): The date of the record.
            category (str): The category of the record.
            amount (float): The amount of the record.
        
        Returns:
            int: The index of the record in the wallet, or None if not found.
        """
        for i, record in enumerate(self.records):
            if record.date == date and record.category == category and record.amount == amount:
                return i
        return None

    def balance(self) -> Tuple[float, float, float]:
        """Calculate the balance of the wallet.
        
        Returns:
            Tuple[float, float, float]: A tuple containing income, expenses, and balance.
        """
        income = sum(record.amount for record in self.records if record.category == "Доход")
        expenses = sum(record.amount for record in self.records if record.category == "Расход")
        balance = income - expenses
        return income, expenses, balance

    def save(self) -> None:
        """Save wallet records to a file."""
        self.records = sorted(self.records, key=lambda record: record.date)
        self.recorder.write(self.records)

    def load(self) -> None:
        """Load wallet records from a file."""
        self.records = self.recorder.read()
