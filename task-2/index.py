from models.product import *
from models.order import *
from models.inventory import *
pro = Product("Laptop 1", "This is Laptop", 100000, 100, "Electronic")
pro2 = Product("Laptop 2", "This is Laptop 2", 555555, 22, "Electronic")

inventory = Inventory()
inventory.add_product(pro)
inventory.add_product(pro2)
inventory.get_products()

customer = Customer("Huy", "TpHCM", "0124566712")

inventory.create_transaction(pro._id, 2, "Buy", customer);
inventory.get_products();
inventory.create_transaction(pro._id, 5, "Sell", customer);
inventory.get_products();

inventory.get_orders()