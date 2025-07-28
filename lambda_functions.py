class MathLibrary:
    def __init__(self):
        self.functions = {
            'add': self.add,
            'subtract': self.subtract,
            'multiply': self.multiply,
            'divide': self.divide,
            'square': self.square
        }
    
    def square(self,x):
        return lambda x: x * x
    def add(self, x, y):
        return x + y
    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y 
    def get_function(self, name):
        if name in self.functions:
            return self.functions[name]
        else:
            raise ValueError(f"Function '{name}' not found in the library.")

class StringLibrary:
    def __init__(self):
        self.functions = {
            'uppercase': self.uppercase,
            'lowercase': self.lowercase,
            'capitalize': self.capitalize
        }
    
    def uppercase(self, s):
        return s.upper()
    
    def lowercase(self, s):
        return s.lower()
    
    def capitalize(self, s):
        return s.capitalize()
    
    def get_function(self, name):
        if name in self.functions:
            return self.functions[name]
        else:
            raise ValueError(f"Function '{name}' not found in the library.")
        
class ListLibrary:
    def __init__(self):
        self.functions = {
            "reverse": self.__reverse,
            "sort": self.__sort,
            "filter_even": self.__filter_even,
            "flatten": self.__flatten
        }
    
              
    def __reverse(self, lst):
        return lst[::-1]
    def __sort(self, lst):
        return sorted(lst)
    def __filter_even(self, lst):
        return [x for x in lst if x % 2 == 0]
    def __flatten(self, nested_list):
        return [item for sublist in nested_list for item in sublist]
    def get_function(self, name):
        if name in self.functions:
            return self.functions[name]
        else:
            raise ValueError(f"Function '{name}' not found in the library.")
    

mathsLib = MathLibrary()
stringLib = StringLibrary()
listLib = ListLibrary()

print(mathsLib.get_function('add')(5, 3))
print(stringLib.get_function('uppercase')("hello"))
print(listLib.get_function('filter_even')([1, 2, 3, 4, 5, 6]))