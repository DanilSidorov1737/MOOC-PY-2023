# Write your solution here:

class Item:
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight
    
    def name(self):
        return self._name
    
    def weight(self):
        return self._weight
    
    def __str__(self):
        return f"{self._name} ({self._weight} kg)"

class Suitcase:
    def __init__(self, max_weight):
        self._max_weight = max_weight
        self._items = []
    
    def add_item(self, item):
        if self.weight() + item.weight() > self._max_weight:
            print("Suitcase is full, can't add item.")
        else:
            self._items.append(item)
    
    def __str__(self):
        if len(self._items) == 1:
            item_str = "item"
        else:
            item_str = "items"
        return f"{len(self._items)} {item_str} ({self.weight()} kg)"
    
    def print_items(self):
        for item in self._items:
            print(item)
    
    def weight(self):
        return sum(item.weight() for item in self._items)
    
    def heaviest_item(self):
        if len(self._items) == 0:
            return None
        return max(self._items, key=lambda item: item.weight())

class CargoHold:
    def __init__(self, max_weight):
        self._max_weight = max_weight
        self._suitcases = []

    def add_suitcase(self, suitcase):
        if self.weight() + suitcase.weight() > self._max_weight:
            print("Cargo hold is full, can't add suitcase.")
        else:
            self._suitcases.append(suitcase)

    def __str__(self):
        if len(self._suitcases) == 1:
            suitcase_str = "suitcase"
        else:
            suitcase_str = "suitcases"
        return f"{len(self._suitcases)} {suitcase_str}, space for {self.remaining_space()} kg"

    def weight(self):
        return sum(suitcase.weight() for suitcase in self._suitcases)

    def remaining_space(self):
        return self._max_weight - self.weight()

    def print_suitcase_items(self, index):
        if index < 0 or index >= len(self._suitcases):
            print("Invalid suitcase index.")
        else:
            self._suitcases[index].print_items()
