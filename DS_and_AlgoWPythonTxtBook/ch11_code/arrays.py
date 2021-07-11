import ctypes

class Array:
    #creates an array with size elements.
    def __init__(self,size):
        assert size>0, "Array size must be > 0"
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear(None)

    # returns size of array.
    def __len__(self):
        return self._size

    #gets the content of the index element
    def __getitem__(self,index):
        assert index>=0 and index<len(self), "Array subscript out of range"
        return self._elements[index]

    #puts the value of the in the array element at index position
    def __setitem__(self,index,value):
        assert index>=0 and index<len(self), "Array subscript out of range"
        self._elements[index] = value

    #clears the array by setting each element to the given value.
    def clear(self,value):
        for i in range(len(self)):
            self._elements[i] = value

class _ArrayIterator:
    def __init__(self,theArray):
        self._arrayRef = theArray
        self.curNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration
