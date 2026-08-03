import time

def hello_world():
    print("hello world")

class Calulcator:
    def __init__(self):
        self.__history = []

    def add(self, *args):
        total = 0
        for i in args:
            total+=i
        
        t = time.time()

        self.__history.append({f"Add_{t}" : {str(args) : total}})
        return total
    
    def get_history(self):
        print(self.__history)


print(__name__)
if __name__ == '__main__':
    # only when i run python calculator.py, run below code
    hello_world()

    c = Calulcator()

    c.add(1,2,2)
    c.add(1,2,2, 100)
    c.add(1,2,2, 17392193)
    c.add(1,-90, 2)

    c.get_history()