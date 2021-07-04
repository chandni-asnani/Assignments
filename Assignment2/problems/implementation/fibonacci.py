from base import Base

class Fibonacci(Base):

    def run(self):
        if self.number == 0:
            return 0
        elif self.number == 1 or self.number == 2:
            return 1
        else:
            return Fibonacci(self.number-1).run() + Fibonacci(self.number-2).run()
