from arrays import Array

class HashMap:
    # Defines constants to represent the status of each table entry
    UNUSED = None
    EMPTY = _MapEntry(None,None)

    # creates an empty map instance
    def __init__(self):
        self._table = Array(7)
        self._count = 0
        # max number of keys that can be stored in the table before exceeding the load factor
        self._maxCount = len(self._table) - len(self._table) // 3

    # returns the number of entries in the map
    def __len__(self):
        return self._count

    #determines if the map contains the given key.
    def __contains__(self,key):
        slot = self._findSlot(key,False)
        return slot is not None

    #adds a new entry to the map if the key does not exist. Otherwise,
    # new value replaces the current value associated with the key
    def add(self,key,value):
        if key in self:
            slot = self._findSlot(key,False)
            self._table[slot].value = value
            return False
        else:
            slot = self._findSlot(key,True)
            self._table[slot] = _MapEntry(key,value)
            self._count += 1
            if self._count == self._maxCount:
                self._rehash()
            return True

    # returns the value associated with the key
    def valueOf(self,key):
        slot = self._findSlot(key,False)
        assert slot is not None, "Invalid map key"
        return self._table[slot].value

    # finds the slot containing the key or where the key can be added.
    # forInsert indicates if the search is for an insertion, which locates
    # the slot into which the new key can be added

    def _findSlot(self,key,forInsert):
        slot = self._hash1(key)
        step = self._hash2(key)

        # Probe for the key
        M = len(self._table)
        while self._table[slot] is not UNUSED:
            if forInsert and (self._table[slot] is UNUSED or self._table[slot] is EMPTY):
                return slot
            elif not forInsert and (self._table[slot] is not EMPTY and self._table[slot].key == key):
                return slot
            else:
                slot = (slot + step ) % M

    #rebuilds the hash table
    def _rehash(self):
        origTable = self._table
        newSize = len(self._table) * 2 + 1
        self._table = Array(newSize)

        # Modify the size attributes
        self._count = 0
        self._maxCount = newSize - newSize//3

        for entry in origTable:
            if entry is not UNUSED and entry is not EMPTY:
                slot = self._findSlot(key,True)
                self._table[slot] = entry
                self._count += 1

    # main hash function for mapping keys to table entries
    def _hash1(self,key):
        return abs(hash(key)) % len(self._table)

    # the second hash function used with double hashing probes
    def _hash2(self,key):
        return 1 + abs(hash(key)) % (len(self._table) - 2)

# Storage class for holding key/value pairs.
class _MapEntry:
    def __init__(self,key,value):
        self.key = key
        self.value = value 
