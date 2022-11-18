# References:
# linear_probe.py, Lecture 23: Hash Tables, FIT1008, Julian Garcia, Monash University
# Assessed Prac 3, FIT1008, Monash University

from referential_array import build_array


class HashTable:
    def __init__(self, size):
        self.table_size = size
        self.count = 0
        self._array = build_array(self.table_size)

    # using function from Julian Garcia's linear_probe.py from Lecture 23: Hash Tables, FIT1008, Monash University
    def __getitem__(self, key):
        if not isinstance(key, str):
            raise ValueError("key must be string type")
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
        if not isinstance(key, str):
            raise ValueError("key must be string type")
        index = self._hash(key)
        for _ in range(self.table_size):
            if self._array[index] is None:
                self._array[index] = (key, value)
                self.count += 1
                return
            elif self._array[index][0] == key:
                self._array[index] = (key, value)
                return
            else:
                index = (index + 1) % self.table_size
        raise StopIteration("hash table is full mate")

    def __contains__(self, key):
        if not isinstance(key, str):
            raise ValueError("key must be string type")
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
        a = 101
        h = 0
        for c in key:
            h = (h * a + ord(c)) % self.table_size
        return h

    def __str__(self):
        out_string = ""
        for i in range(len(self._array)):
            if self._array[i] is not None:
                (key, value) = self._array[i]
                out_string += "({}: {}), ".format(key, value)
        return out_string[:-2]
