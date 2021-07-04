
from problems.implementation.fibonacci import Fibonacci
from problems.implementation.armstrong import Armstrong
from problems.implementation.prime import Prime


if __name__ == "__main__":
    
    print("enter 1 for fibonacci, 2 for prime , 3 for armstrong")
    problem = int(input())
    while problem not in range(1,4):
        print("Please provide valid problem")
        print("enter 1 for fibonacci, 2 for prime , 3 for armstrong")
        problem = int(input())
    print("enter number")
    number = int(input())


    d = {
    1: Fibonacci(number).run(),
    2: Prime(number).run(),
    3: Armstrong(number).run()
}
    
    print(d[problem])
