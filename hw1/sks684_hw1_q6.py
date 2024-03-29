'''
Simran Soin
CS UY 1134
11 February 2019
Homework 1 Question 6
'''
class Vector:
    def __init__(self, d):
        if type(d) == list:
            self.coords = d
        else:
            self.coords = [0]*d
        
    def __len__(self):
        return len(self.coords)
    
    def __getitem__(self, j):
        return self.coords[j]
    
    def __setitem__(self, j, val):
        self.coords[j] = val
        
    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
           result[j] = self[j] + other[j]
        return result
    
    def __eq__(self, other):
        return self.coords == other.coords
    
    def __ne__(self, other):
        return not (self == other)
    
    def __str__(self):
        return '<'+ str(self.coords)[1:-1] + '>'
    
    def __repr__(self):
        return str(self)

    def __neg__(self):
        v2 = [-1*i for i in self.coords]
        return Vector(v2)

    def __sub__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
           result[j] = self[j] - other[j]
        return result

    def __mul__(self, k):
        if type(k) == Vector:
            if (len(self) != len(k)):
                raise ValueError("dimensions must agree")
            total_mul = sum([self[i]*k[i] for i in range(len(self.coords))])
            return total_mul
        else:
            product = Vector(len(self.coords))
            for i in range(len(self.coords)):
                product[i] = k*self.coords[i]
            return product
        
    def __rmul__(self, k):
        if type(k) == Vector:
            if (len(self) != len(k)):
                raise ValueError("dimensions must agree")
            total_mul = sum([self[i]*k[i] for i in range(len(self.coords))])
            return total_mul
        else:
            product = Vector(len(self.coords))
            for i in range(len(self.coords)):
                product[i] = k*self.coords[i]
            return product
