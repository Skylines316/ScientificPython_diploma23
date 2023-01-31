import numpy as np

class MyMatrix:
    def __init__(self, N):
      self.matrix = np.random.rand(N, N)        
    def inverse(self):
        return np.linalg.inv(self.matrix)
    
    def determinant(self):
        return np.linalg.det(self.matrix)
    
    def eigenvalues(self):
        return np.linalg.eigvals(self.matrix)
    
    def __add__(self, other):
        return np.add(self.matrix,other.matrix)
    
    def __mul__(self, other):
        return np.multiply(self.matrix, other.matrix)
    
    def __repr__(self):
        return str(self.matrix)
