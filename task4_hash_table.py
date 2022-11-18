# References:
# linear_probe.py, Lecture 23: Hash Tables, FIT1008, Julian Garcia, Monash University
# Assessed Prac 3, FIT1008, Monash University

from referential_array import build_array


class HashTable:
    def __init__(self, size=9857, base=101):
        self.base = base
        self.table_size = size
        self.count = 0
        self._array = build_array(self.table_size)
        self.collisions = 0
        self.total_probe_length = 0

    # using function from Julian Garcia's linear_probe.py from Lecture 23: Hash Tables, FIT1008, Monash University
    def __getitem__(self, key):
        index = self._hash(key)
        for _ in range(self.table_size):
            if self._array[index] is None:
                raise KeyError("nothing here")
            elif self._array[index][0] == key:
                return self._array[index][1]
            else:
                index = (index + 1) % self.table_size
        raise KeyError("nothing here")

    # using function from Julian Garcia's linear_probe.py from Lecture 23: Hash Tables, FIT1008, Monash University
    def __setitem__(self, key, value):
        if self.count > self.table_size * (2/3):
            self._rehash()
        index = self._hash(key)
        for i in range(self.table_size):
            if self._array[index] is None:
                self._array[index] = (key, value)
                self.count += 1
                return
            elif self._array[index][0] == key:
                self._array[index] = (key, value)
                return
            else:
                if i == 0:
                    self.collisions += 1
                index = (index + (i+1)**2) % self.table_size
                self.total_probe_length += 1

    def __contains__(self, key):
        index = self._hash(key)
        for _ in range(self.table_size):
            if self._array[index] is None:
                return False
            elif self._array[index][0] == key:
                return True
            else:
                index = (index + 1) % self.table_size

    # using function from Assessed Prac 3: FIT1008, hash_value(self, key), Monash University
    def _hash(self, key):
        h = 0
        for c in key:
            h = (h * self.base + ord(c)) % self.table_size
        return h

    def __str__(self):
        out_string = ""
        for i in range(len(self._array)):
            if self._array[i] is not None:
                (key, value) = self._array[i]
                out_string += "({}: {}), ".format(key, value)
        return out_string[:-2]

    def _rehash(self):
        self.table_size = 2 * self.table_size
        temp_array = build_array(self.table_size)
        for i in range(len(self._array)):
            if self._array[i] is not None:
                (key, value) = self._array[i]
                index = self._hash(key)
                j = 0
                hashed = False
                while j < self.table_size and not hashed:
                    if temp_array[index] is None:
                        temp_array[index] = (key, value)
                        hashed = True
                    elif temp_array[index][0] == key:
                        temp_array[index] = (key, value)
                        hashed = True
                    else:
                        index = (index + 1) % self.table_size
        self._array = temp_array
