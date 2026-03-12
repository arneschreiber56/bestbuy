class Product:
    """ Represents a product with a name, price, quantity, and active state.
    Tracks total quantity across all product instances.
    """
    total = 0

    def __init__(self, name, price, quantity):
        """
        Initialize a new product with name, price, and quantity.
        Raises exceptions for invalid price or quantity values.
        """
        self.name = name
        # Price validation
        if not isinstance(price, (int, float)):
            raise Exception("Price needs to be integer or float")
        elif price < 0:
            raise Exception("Sorry, price can not be negative")
        else:
            self.price = price
        # Quantity validation
        if not isinstance(quantity, int):
            raise Exception("Quantity needs to be integer")
        elif quantity < 0:
            raise Exception("Sorry, quantity can not be negative")
        else:
            self.quantity = quantity

        # Without exceptions, product can be active
        self.active = True


    def get_quantity(self):
        """
        Return the current quantity of the product.
        """
        return self.quantity


    def set_quantity(self, quantity):
        """
        Set a new quantity for the product and update the global total.
        Deactivates the product if quantity becomes zero.
        """
        if quantity < 0:
            raise Exception("Error processing quantity!")
        else:
            Product.total = Product.total - self.quantity + quantity
            if quantity == 0:
                self.active = False
                self.quantity = quantity
            else:
                self.quantity = quantity


    def is_active(self):
        """
        Return whether the product is currently active.
        """
        return self.active


    def activate(self):
        """
        Mark the product as active.
        """
        self.active = True


    def deactivate(self):
        """
        Mark the product as inactive.
        """
        self.active = False


    def show(self):
        """
        Print product information including name, price, and quantity.
        """
        print(f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        """
        Reduce the product quantity by the given amount and return the total price.
        Raises an exception if the requested quantity is invalid.
        """
        if not isinstance(quantity, int):
            raise Exception("Error processing quantity!")

        quantity_left = self.quantity - quantity

        if quantity_left >= 0:
            self.set_quantity(quantity_left)
            return float(self.price * quantity)
        else:
            raise Exception("Error while making order! "
                            "Quantity larger than what exists")





