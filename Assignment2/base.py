from abc import ABC, abstractmethod

class Base(ABC):
    
    def __init__(self,number):
        self.number = number
        

    @abstractmethod
    def run(self):
        return 0
    

# 1. User will give input to main.py
# Which will call respective py file for problem.
# 2. All problem py file must use run method of base class.
# 3. As per user input output should be generated.