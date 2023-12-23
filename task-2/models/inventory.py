from models.order import Order
from models.product import Product
from models.customer import Customer
import datetime as datetime
class Inventory:
    def __init__(self) -> None:
        self._orders = [Order]
        self._products = [Product]
        
    def add_product(self, product: Product):
        self._products.append(product);
        
    def update_stock_quantity(self, product_id: int, quantity: int, type:str) -> None:
        try:
            result = next(x for x in self._products if x.id == product_id)
        except StopIteration:
            print(f"Product with id {product_id} not found.")
            return
        if type == "Buy":
            result._quantity_in_stock -= quantity
        else:
            result._quantity_in_stock += quantity

    def get_products(self) -> None: 
        for x in self._products:
            print(x)
    
    def get_orders(self) -> None: 
        for x in self._orders:
            print(x)
    
    def add_order(self, products: [Product], customer: Customer, type: str) -> None:
        order = Order(products, datetime.datetime.now(), customer, type);
        self._orders.append(order);
    
    def create_transaction(self, product_id: int, quantity: int, order_type: str, customer: Customer) -> None:
        self.update_stock_quantity(product_id, quantity, order_type);
        self.add_order(product_id, customer, order_type);