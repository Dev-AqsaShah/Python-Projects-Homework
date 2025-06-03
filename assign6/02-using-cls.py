# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.


class Counter:
    count = 0
    
    def __init__(self):
        Counter.count += 1
        
        @classmethod
        def display_count(cls):
            return f'Total objects created: {cls.count}'
        
    obj1 : Counter = Counter()  # noqa: F821
    obj2 : Counter = Counter()  # noqa: F821
    obj3 : Counter = Counter()  # noqa: F821
    print(Counter.display_count())