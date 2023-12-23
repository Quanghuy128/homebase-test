import numpy as np
class Customer:
    def __init__(self, name, address, phone_number) -> None:
        self._id = np.random.randint(0, 10000)
        self._name = name
        self._address = address
        self._phone_number = phone_number
        
    