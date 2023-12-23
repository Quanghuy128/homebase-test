class RealEstate:    
    def __init__(self, title, price, area, location, owner, contact_number):
        self._title = title
        self._price = price
        self._area = area
        self._location = location
        self._owner = owner
        self._contact_number = contact_number
        
    def as_dict(self):
        return {'title': self._title, 'price': self._price, 'location': self._location, 
        'area': self._area, 'owner': self._owner, 'contact_number': self._contact_number}
    
    def __str__(self):
        return self._title + " - " + self._price + " - " + self._area + " - " + self._location + " - " + self._owner + " - " + self._contact_number