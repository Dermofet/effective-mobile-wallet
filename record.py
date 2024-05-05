from dataclasses import dataclass
import datetime

@dataclass
class Record:
    """Represents a financial record.

    Attributes:
        date (datetime.date): The date of the record.
        category (str): The category of the record (e.g., "Доход", "Расход").
        amount (float): The amount of money involved in the record.
        comment (str): Additional comment or description for the record.
    """
    date: datetime.date
    category: str
    amount: float
    comment: str
