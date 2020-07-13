def add(num1, num2):
# adds two given numbers
# int, int -> int
    return (num1 + num2)


def substract(num1, num2):
# substracts second number from first
# int, int -> int
    return (num1 - num2)


def calc(num1, num2, operation):
# performs given operation on two numers
# int, int, string -> int
    operations = {'+': add, '-': substract}
    calculation = operations.get(operation)
    if (calculation):
        return (calculation(num1, num2))
    else:
        return None