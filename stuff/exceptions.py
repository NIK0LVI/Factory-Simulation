class Exceptions(Exception):
    def __init__(self, message):
        super().__init__(message)


class ExceptionNoSuchProduct(Exceptions):
    def __init__(self):
        super().__init__("We do not manufacture such a product. ")


class ExceptionLackingResources(Exceptions):
    def __init__(self):
        super().__init__("Production resources insufficient.")


class ExceptionOverflow(Exceptions):
    def __init__(self):
        super().__init__("Stock limits exceeded. ")


class ExceptionNoSuchComponent(Exceptions):
    def __init__(self):
        super().__init__("No such component in stock. ")
