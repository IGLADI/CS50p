class Jar:
    def __init__(self, capacity=12):
        if capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError("Capacity must be positive")
        self._cookies = 0

    def __str__(self):
        return "🍪" * self._cookies

    def deposit(self, n):
        if n + self._cookies > self.capacity:
            raise ValueError("Too many cookies")
        else:
            self._cookies += n

    def withdraw(self, n):
        if n > self._cookies:
            raise ValueError("Not enough cookies")
        else:
            self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies
