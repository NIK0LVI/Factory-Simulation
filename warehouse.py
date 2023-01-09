import json
import datetime
import os
from stuff.exceptions import ExceptionNoSuchComponent


class Warehouse:
    def __init__(self, item_name):
        self.item_name = item_name

    def get_name(self):
        return self.item_name

    def set_name(self, item_name):
        self.item_name = item_name
        return self.item_name

    @staticmethod
    def return_raw_component(item_name):
        """Returns the stock of a specific raw component. """
        with open("warehouse_details.json", "r") as file:
            data = json.load(file)
            word = item_name
            if word in data["stockpile"]:
                return data["stockpile"][word]
            else:
                raise ExceptionNoSuchComponent

    def import_raw_component(self):
        """Simulates procuring production components. """
        with open("warehouse_details.json", "r+") as file_data:
            word = input("Which resource is lacking? \n")
            quantity = int(input("How many kilograms do you wish to procure? \n"))
            warehouse_data = json.load(file_data)
            stockpile_data = warehouse_data["stockpile"]
            freezer_data = warehouse_data["freezer"]

            """Semi-flexible dict comprehension for adding quantity to stock, leaving the rest intact. """
            if word in warehouse_data["stockpile"]:
                stockpile_result = {
                    "stockpile": {item: float(stockpile_data[item]) + quantity for item in stockpile_data.keys()},
                    "freezer": {item: int(freezer_data[item]) for item in freezer_data.keys()}
                }

                """Updates the warehouse file. """
                file_data.seek(0)
                json.dump(stockpile_result, file_data, indent=4)
                file_data.truncate()

                """Creates a current stockpile report. """
                self.return_warehouse_stockpile_as_file()

                """Creates a current freezer report. """
                self.return_warehouse_freezer_as_file()

                print("Component procured successfully! ")

            else:
                raise ExceptionNoSuchComponent

    @staticmethod
    def return_warehouse_stockpile_on_screen():
        """Returns the stockpile inventory, on screen, as a list. """
        stockpile_list = []
        with open("warehouse_details.json", "r") as file:
            data = json.load(file)
            for item in data["stockpile"]:
                stockpile_list.append(str(item) + ": " + str(data["stockpile"][item]))
            return stockpile_list

    def return_warehouse_stockpile_as_file(self):
        """Returns the stockpile inventory as a .txt file, reusing the stockpile function. """
        lst = self.return_warehouse_stockpile_on_screen()
        current_datetime = datetime.datetime.today().date()
        current_directory = os.getcwd()
        with open(current_directory + "/Stockpile Status " + str(current_datetime) + ".txt", "w+") as file:
            for item in lst:
                file.write(item + "\n")

    @staticmethod
    def return_warehouse_freezer_on_screen():
        """Returns the freezer inventory, on screen, as a list. """
        freezer_list = []
        with open("warehouse_details.json", "r") as file:
            data = json.load(file)
            for item in data["freezer"]:
                freezer_list.append(str(item) + ": " + str(data["freezer"][item]))
            return freezer_list

    def return_warehouse_freezer_as_file(self):
        """Returns the stockpile inventory as a .txt file, reusing the freezer function. """
        lst = self.return_warehouse_freezer_on_screen()
        current_datetime = datetime.datetime.today().date()
        current_directory = os.getcwd()
        with open(current_directory + "/Freezer Status " + str(current_datetime) + ".txt", "w+") as file:
            for item in lst:
                file.write(item + "\n")

    @staticmethod
    def return_specific_item_stock_on_screen():
        """First bonus. Returns status of items upon specific inquiry, returns a list on screen. """
        lst = []
        request_lst = list(input("What items are we searching for? \n").split())
        with open("warehouse_details.json", "r") as file:
            data = json.load(file)
            for items in request_lst:
                lst.append(items + ": " + str(data["freezer"][items]))
            return lst

    def return_specific_item_stock_as_file(self):
        """First bonus. Returns inquiry as a .txt file. """
        lst = self.return_specific_item_stock_on_screen()
        current_datetime = datetime.datetime.today().date()
        current_directory = os.getcwd()
        print(lst)
        with open(current_directory + "/Inquiry " + str(current_datetime) + ".txt", "w+") as file:
            for item in lst:
                file.write(item + "\n")

    # @staticmethod
    # def check_resource_status():
    #     """Resource check function, redundant. """
    #     with open("warehouse_details.json", "r") as file:
    #         data = json.load(file)
    #         for item in data["stockpile"]:
    #             if data["stockpile"][item] <= 20:
    #                 print(item, data["stockpile"][item], "You need more shit. ")
    #
    #             else:
    #                 print(item, data["stockpile"][item], "It do be fine.")
    #
    # @staticmethod
    # def check_products_status():
    #     """Products check function, redundant. """
    #     with open("warehouse_details.json", "r") as file:
    #         data = json.load(file)
    #         for item in data["freezer"]:
    #             if data["freezer"][item] <= 200:
    #                 print(item, data["freezer"][item], "Make more shit. ")
    #                 notif = EmailNotifications()
    #                 notif.send_attention_notification()
    #             else:
    #                 print(item, data["freezer"][item], "You do be making fine. ")
