# -*- coding: utf-8 -*-

class Calculator:
    def __init__(self): pass

    def isValid(self,arr):
        if isinstance(arr[0], (int, float)) and isinstance(arr[1], (int,float)):
            return True
        return False

    def add(self,arr):
        if len(arr) < 3:
            if self.isValid(arr):
                return arr[0] + arr[1]
            return False
        return self.add(arr[:-1]) + arr[-1]

    def substract(self,arr):
        if len(arr) < 3:
            if self.isValid(arr):
                return arr[0] - arr[1]
            return False
        return self.substract(arr[:-1]) - arr[-1]

    def multiply(self,arr):
        if len(arr) < 3:
            if self.isValid(arr):
                return arr[0] * arr[1]
            return False
        return arr[-1] * self.multiply(arr[:-1])
        
    
    def div(self, data):
        if self.isValid(data) and data[1] != 0:
            return data[0]/data[1]
        return False
