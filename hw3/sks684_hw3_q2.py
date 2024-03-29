'''
Simran Soin
CS-UY 1134
Homework 3 Q2
'''
import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()


class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1)
        self.n = 0
        self.capacity = 1

    def __len__(self):
        return self.n

    def append(self, val):
        if(self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1

    def __iter__(self):
        for i in range(self.n):
            yield self.data_arr[i]
            
    def resize(self, new_size):
        new_arr = make_array(new_size)
        for i in range(self.n):
            new_arr[i] = self.data_arr[i]
        self.data_arr = new_arr
        self.capacity = new_size

    def __getitem__(self, ind):
        if ind < 0 and ((ind*-1)<= self.n):
            ind *= -1
            ind = len(self) - ind
            return self.data_arr[ind]
        elif 0 <= ind <= (self.n - 1):
            return self.data_arr[ind]
        else:
            raise IndexError("Invalid Index")

    def __setitem__(self, ind, val):
        if ind < 0 and ((ind*-1)<= self.n):
            ind *= -1
            ind = len(self) - ind
            self.data_arr[ind] = val
        elif 0 <= ind <= (self.n - 1):
            self.data_arr[ind] = val
        else:
            raise IndexError("Invalid Index")

    def extend(self, other_iterable):
        for elem in other_iterable:
            self.append(elem)
            
    def __repr__(self):
        return "[" + ", ".join(repr(e) for e in self) + "]"

    def __add__(self, other):
        sum_of_both = ArrayList()
        for e in self:
            sum_of_both.append(e)
        for e in other:
            sum_of_both.append(e)
        return sum_of_both

    def __iadd__(self, other):
        self.extend(other)

    def __mul__(self, k):
        mul_of_array = ArrayList()
        for i in range(k):
            for e in self:
                mul_of_array.append(e)
        return mul_of_array

    def __rmul__(self,k):
        return self*k

    def insert(self, index, val):
        prev_val =  0
        curr_val = 0
        for i in range(self.n):
            if i == index:
                prev_val = self[i]
                self[i] = val
            if i > index:
                curr_val = self[i]
                self[i] = prev_val
                prev_val = curr_val
        self.append(prev_val)
        return self

    def pop(self, val=-1):
        popped_val = None
        if val < 0 and ((val*-1)<= self.n):
            val *= -1
            val = self.n - val
        elif val > (self.n-1) or (val < 0 and ((val*-1)> self.n)):
            raise IndexError("Invalid Index")
        for i in range(self.n):
            if i > val:
                self[i-1] = self[i]
            if i == val:
                popped_val = self[i]
                self[i] = None
        self.n -= 1
        if self.n * 4 < self.capacity:
            self.capacity/= 2
        return popped_val 
