from base import Base

class Fibonacci(Base):

    def run(self):
        lst = [1,2]
        if self.number == 0:
            return 0
        elif self.number in lst:
            return 1
        else:
            return Fibonacci(self.number-1).run() + Fibonacci(self.number-2).run()
