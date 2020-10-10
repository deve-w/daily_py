class IOstring:
    def __init__(self):
        pass
    def get_string(self):
        self.s = input()
    def print_string(self):
        print(self.s.upper())


print(IOstring('abc').get_string())
print(IOstring('abc').print_string())