def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b and return with optional truncation and custom message."""
    result = None

    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        if b != 0:
            result = a / b

    if result is not None:
        if make_int:
            result = int(result)
        return f'{message} {result}'
    else:
        return None

# Test cases
print(calculate('add', 2.5, 4))                               # Output: 'The result is 6.5'
print(calculate('subtract', 4, 1.5, make_int=True))            # Output: 'The result is 2'
print(calculate('multiply', 1.5, 2))                           # Output: 'The result is 3.0'
print(calculate('divide', 10, 4, message='I got'))             # Output: 'I got 2.5'
print(calculate('foo', 2, 3))                                  # Output: None (Invalid operation)
