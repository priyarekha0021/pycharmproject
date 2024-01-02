# rekha.py  <--- cal Module
a = 50

def name():
    print("From Module rekha")

def add(a, b):
    return a + b

def sub(a, b):
    return a - b


# rekha.py
class rekha:
    def __init__(self, name, roll, address):
        self.name = name
        self.roll = roll
        self.address = address

    def disp(self):
        print(f'Name: {self.name} Roll: {self.roll} Address: {self.address}')