#order
import datetime as datetime
from datetime import *
import numpy as np
from models.customer import Customer
from models.product import Product
class Order: 
    def __init__(self, purchased_products: [Product], order_date: date, customer: Customer, status: str):
        self._id = np.random.randint(0, 10000)
        self._purchased_products = purchased_products
        self._order_date = order_date
        self._customer = customer    
        self._status = status if status is not None else "Processing"
        
    @property
    def purchased_products(self): return self._purchased_products
    
    @purchased_products.setter
    def purchased_products(self, purchased_products): self._purchased_products = purchased_products
    
    @property
    def order_date(self): return self._order_date
    
    @order_date.setter
    def order_date(self, order_date): self._order_date = order_date
    
    @property
    def customer(self): return self._customer
    
    @customer.setter
    def customer(self, customer): self._customer = customer
    
    @property
    def status(self): return self._status
    
    @status.setter
    def status(self, status): self._status = status
    
    def __str__(self):
        return str(self._order_date.today().strftime("%d/%m/%Y %H:%M:%S")) + " - " +  self._customer._name + " - " + self._status + " - products: " + str( self._purchased_products);
    