from record import Record
from user_interface import UserInterface
from wallet import Wallet


class WalletInterface:
    """Class responsible for handling user interactions related to wallet management."""

    @staticmethod
    def start(wallet: Wallet) -> None:
        """Start the wallet interface.

        Args:
            wallet (Wallet): The wallet instance to be used for managing records.
        """
        # List of functions
        actions = {
            1: WalletInterface.balance,
            2: WalletInterface.add_record,
            3: WalletInterface.change_record,
            4: WalletInterface.find_records,
            5: WalletInterface.save_data,
            6: WalletInterface.load_data
        }
        while True:
            choice = UserInterface.menu()
            if choice == 0:
                break
            elif choice in actions:
                actions[choice](wallet)
            else:
                print("Invalid choice")

    @staticmethod
    def balance(wallet: Wallet) -> None:
        """Display the balance of the wallet.

        Args:
            wallet (Wallet): The wallet instance.
        """
        income, expenses, balance = wallet.balance()
        print(f"Income: {income}\nExpenses: {expenses}\nBalance: {balance}")

    @staticmethod
    def add_record(wallet: Wallet) -> None:
        """Add a record to the wallet.

        Args:
            wallet (Wallet): The wallet instance.
        """
        record_info = UserInterface.get_record_info()
        record = Record(*record_info)
        wallet.add_record(record)
        print("Record added successfully")

    @staticmethod
    def change_record(wallet: Wallet) -> None:
        """Change a record in the wallet.

        Args:
            wallet (Wallet): The wallet instance.
        """
        new_record_info = UserInterface.get_record_info()
        new_record = Record(*new_record_info)
        wallet.change_record(new_record)
        print("Record changed successfully")

    @staticmethod
    def find_records(wallet: Wallet) -> None:
        """Find records in the wallet based on search filters.

        Args:
            wallet (Wallet): The wallet instance.
        """
        search_filters = UserInterface.get_search_filters()
        records = wallet.find_records(*search_filters)
        print(f"Found {len(records)} records:")
        UserInterface.display_records(records)

    @staticmethod
    def save_data(wallet: Wallet) -> None:
        """Save wallet data to a file.

        Args:
            wallet (Wallet): The wallet instance.
        """
        wallet.save()
        print("Data saved successfully")

    @staticmethod
    def load_data(wallet: Wallet) -> None:
        """Load wallet data from a file.

        Args:
            wallet (Wallet): The wallet instance.
        """
        wallet.load()
        print("Data loaded successfully")
