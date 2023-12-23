#product.py
import numpy as np
import sys as sys
class Product:
    def __init__(self, name, description, price, quantity_in_stock, type):
        self._id = np.random.randint(0, 1000)
        self._name = name
        self._description = description
        self._price = price
        self._quantity_in_stock = quantity_in_stock
        self._type = type
        
    @property
    def id(self):
        return self._id
    
    @id.setter
    def name(self, id):
        self._id = id;
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name;
        
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description;
        
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price;

    @property
    def quantity_in_stock(self):
        return self._quantity_in_stock

    @quantity_in_stock.setter
    def quantity_in_stock(self, value):
        if value >= 0:
            self._quantity_in_stock = value
        else:
            print("Error: Quantity cannot be negative.")

    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        self._type = type;
    
    def __str__(self) -> str:
        return str(self.id) + " - " + self.name + " - " + self.description + " - " + str(self.price) + " - " + str(self.quantity_in_stock) + " - " + self.type;
    
    #def toString(self): return "{self.name} - {self.description} - {self.price} - {self.quantity_in_stock} - {self.type}".format();
    
    #toString = lambda: "{self.name} - {self.description} - {self.price} - {self.quantity_in_stock} - {self.type}".format();