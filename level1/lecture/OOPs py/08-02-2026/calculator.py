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

