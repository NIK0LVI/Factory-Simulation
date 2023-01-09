import json

from stuff.auxiliary import countdown_timer
from warehouse import Warehouse
from stuff.email_notifs import EmailNotifications
from stuff.exceptions import ExceptionLackingResources, ExceptionOverflow, ExceptionNoSuchProduct


class Icecream:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self):
        name = input("Please enter product name: \n")
        self.name = name
        return self.name

    def get_icecream_recipe(self):
        """Returns the icecream recipe from the json file in dict format."""
        with open("recipes.json", "r") as file:
            data = json.load(file)
            word = self.set_name()
            if word in data:
                return data[word]
            else:
                raise ExceptionNoSuchProduct

    # @staticmethod
    # def add_new_recipe():
    #     """This method adds a new recipe to the json file. Redundant. """
    #     key = input("What product are we adding? \n")
    #     ingredient_cocoa = input("Enter amount of cocoa: \n")
    #     ingredient_milk = input("Enter amount of milk: \n")
    #     ingredient_sugar = input("Enter amount of sugar: \n")
    #     ingredient_fat = input("Enter amount of fat: \n")
    #
    #     new_entry = {key: {"cocoa_powder": ingredient_cocoa,
    #                        "milk_powder": ingredient_milk,
    #                        "sugar": ingredient_sugar,
    #                        "milk_fat": ingredient_fat}
    #                  }
    #
    #     with open("recipes.json", "r") as file:
    #         data = json.load(file)
    #
    #     data.update(new_entry)
    #
    #     with open("recipes.json", "w") as file:
    #         json.dump(data, file)

    def start_production(self):
        storage = Warehouse("")
        notification = EmailNotifications()

        """Function that updates the warehouse details upon starting production. """
        with open("recipes.json", "r") as file:
            recipe_data = json.load(file)
            word = self.set_name()
            if word in recipe_data:
                recipe = recipe_data[word]

                """After confirming that product exists, starts production simulation limited to bulk of 5. """
                product = 0
                while product < 5:
                    with open("warehouse_details.json", "r+") as file_data:
                        warehouse_data = json.load(file_data)
                        stockpile_data = warehouse_data["stockpile"]
                        freezer_data = warehouse_data["freezer"]

                        """Semi-flexible dict comprehension for calculating resource allocation according to recipe (
                        kg/g)."""
                        stockpile_result = {
                            "stockpile": {item: float(stockpile_data[item]) - recipe.get(item, 0) / 1000 for item in
                                          stockpile_data.keys()},
                            "freezer": {item: int(freezer_data[item]) + 1 for item in freezer_data.keys()}
                        }
                        """Checks the results for lacking resources. """
                        for item in stockpile_result["stockpile"].keys():
                            if stockpile_result["stockpile"][item] <= 0:
                                notification.send_lacking_resources()
                                raise ExceptionLackingResources

                        """Checks the results for exceeding product stock. """
                        for item in stockpile_result["freezer"].keys():
                            if stockpile_result["freezer"][item] >= 1000:
                                raise ExceptionOverflow

                        """Calls the timer before writing into file. """
                        countdown_timer()

                        """Updates the warehouse file. """
                        file_data.seek(0)
                        json.dump(stockpile_result, file_data, indent=4)
                        file_data.truncate()

                        """Creates a current stockpile report. """
                        storage.return_warehouse_stockpile_as_file()

                        """Creates a current freezer report. """
                        storage.return_warehouse_freezer_as_file()

                        product += 1

                """Sends an email notification of completed production. """
                notification.send_production_completed_notification()
            else:
                raise ExceptionNoSuchProduct

    def production_count(self):
        """Second bonus function. Asks for specific ingredient, retrieves information using existing functions."""
        ingredient = input("Ingredient name (case-sensitive): \n")
        material = Warehouse("").return_raw_component(ingredient)
        product_recipe = self.get_icecream_recipe()

        """Calculates possible production results based on recipe and stockpile info, from a given ingredient."""
        production_result = {ingredient: product_recipe[ingredient] / (material / 1000) for _ in product_recipe.keys()}

        for key, value in production_result.items():
            print(f"It is possible to produce {round(value)} units with current stocks of {key} ingredient. ")
