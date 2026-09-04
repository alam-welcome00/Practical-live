from my_module import calculator

if __name__ == '__main__':
    calculator.hello_world()

    c = calculator.Calulcator()

    c.add(1,2,2)
    c.add(1,2,2, 100)
    c.add(1,2,2, 17392193)
    c.add(1,-90, 2)

    c.get_history()