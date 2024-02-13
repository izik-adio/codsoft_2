class Operations:
    def __init__(self, a, b, operation) -> None:
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        match self.operation:
            case "a":
                return self.add
            case "b":
                return self.sub
            case "c":
                return self.mul
            case "d":
                return self.div

    @property
    def add(self):
        return self.a + self.b

    @property
    def sub(self):
        return self.a - self.b

    @property
    def mul(self):
        return self.a * self.b

    @property
    def div(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return f"Cant divide {self.a} by {self.b}.\nZero division is not supported"
