import os

from wallet import Wallet
from wallet_interface import WalletInterface

def get_filepath() -> str:
    """Prompt user to input file path and ensure the existence of the file.

    Returns:
        str: The file path provided by the user.
    """
    filepath = input("Input file path: ")

    # If the file doesn't exist, create it
    if not os.path.exists(filepath):
        f = open(filepath, "w")
        f.close()
    return filepath

def main() -> None:
    filepath = get_filepath()
    wallet = Wallet(filepath)
    WalletInterface.start(wallet)

if __name__ == "__main__":
    main()
