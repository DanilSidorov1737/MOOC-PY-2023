class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        return f"{self._euros}.{self._cents:02d} eur"

    def __eq__(self, other):
        return self._euros == other._euros and self._cents == other._cents

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if self._euros < other._euros:
            return True
        elif self._euros == other._euros:
            return self._cents < other._cents
        else:
            return False

    def __gt__(self, other):
        if self._euros > other._euros:
            return True
        elif self._euros == other._euros:
            return self._cents > other._cents
        else:
            return False

    def __add__(self, other):
        euros = self._euros + other._euros
        cents = self._cents + other._cents
        if cents >= 100:
            cents -= 100
            euros += 1
        return Money(euros, cents)

    def __sub__(self, other):
        euros = self._euros - other._euros
        cents = self._cents - other._cents
        if cents < 0:
            cents += 100
            euros -= 1
        if euros < 0:
            raise ValueError("a negative result is not allowed")
        return Money(euros, cents)