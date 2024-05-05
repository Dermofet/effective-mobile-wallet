import datetime
from typing import List, Tuple
from record import Record

class UserInterface:
    """Class responsible for interacting with the user through the command line interface."""

    @staticmethod
    def menu() -> int:
        """Display the menu and prompt the user for choice.

        Returns:
            int: The choice made by the user.
        """
        print("\n1. Balance\n2. Add record\n3. Change record\n4. Find record\n5. Save data\n6. Load data\n0. Exit")
        return int(input("Your choice: "))

    @staticmethod
    def get_record_info() -> Tuple[datetime.date, str, float, str]:
        """Prompt the user to input record information.

        Returns:
            Tuple[datetime.date, str, float, str]: A tuple containing date, category, amount, and comment.
        """
        date = input("Date (YYYY-MM-DD): ").strip()
        category = input("Category: ").strip()
        amount = float(input("Amount: ").strip())
        comment = input("Comment: ").strip()
        return datetime.date.fromisoformat(date), category, amount, comment

    @staticmethod
    def get_search_filters() -> Tuple[datetime.date, str, float]:
        """Prompt the user to input search filters.

        Returns:
            Tuple[datetime.date, str, float]: A tuple containing date, category, and amount filters.
        """
        date = input("Date (YYYY-MM-DD): ").strip()
        category = input("Category: ").strip()
        amount = float(input("Amount: ").strip())
        return datetime.date.fromisoformat(date), category, amount

    @staticmethod
    def display_records(records: List[Record]) -> None:
        """Display a list of records.

        Args:
            records (List[Record]): The list of records to be displayed.
        """
        for record in records:
            print(f"{record.date} {record.category} {record.amount} {record.comment}")
