import sys

from icecream import Icecream
from warehouse import Warehouse

product = Icecream("")
storage = Warehouse("")


def main():
    while True:
        print("""
        Welcome to Willy Wanker icecream factory, 
        Willy Wonka sister company! 
        =========================================
        1. Query warehouse resources
        2. Query warehouse products
        3. Simulate production
        4. Order supplies
        5. Query specific products (first bonus)
        6. Query production (second bonus) 
        7. Exit
        =========================================
        Unholy administrative tool of limited
        resources, Willy Wanker Inc.
        """)

        selection = input("Select your option by entering the corresponding number: \n")

        match selection:
            case "1":
                print("File created upon exiting the program. ")
                storage.return_warehouse_stockpile_as_file()
                print(*storage.return_warehouse_stockpile_on_screen(), sep="\n")

            case "2":
                print("File created upon exiting the program. ")
                storage.return_warehouse_freezer_as_file()
                print(*storage.return_warehouse_freezer_on_screen(), sep="\n")

            case "3":
                print("Base warehouse file updated upon exiting the program. ")
                product.start_production()

            case "4":
                print("Base warehouse file updated upon exiting the program. ")
                storage.import_raw_component()

            case "5":
                print("Use space ' ', as a separator. ")
                storage.return_specific_item_stock_as_file()

            case "6":
                product.production_count()

            case "7":
                return sys.exit()
            case _:
                print("No habla that input. ")
