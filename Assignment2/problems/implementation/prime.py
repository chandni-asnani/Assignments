from base import Base

class Prime(Base):
    
    def run(self):
        if self.number <= 1:
            return False
        elif self.number == 2:
            return True
        else:
            for i in range(2,self.number):
                if all(self.number%i!=0 for i in range(2,self.number)):
                    return True
                else:
                    return False