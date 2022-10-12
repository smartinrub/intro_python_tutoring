# Variables and Data Types

## Variables

Think of variables as labels that you can assign to values.

Use a variable in `hello_world.py` for the `print()` method.

```python
message = "Hello World"
print(message)
```

### Variable Rules:

- Variable names can only contain letters, numbers and underscores.
- Use snake case style. e.g. `name_length`
- Spaces are not allowed.
- Avoid using Python keywords such as `print`.
- Variable names should be short but descriptive. e.g. `name` is better than `n`; `name_length` is better than `length_of_persons_name`.

### Exercises

1. Create a `simple_message.py` and assign a message to a variable, and print that message.
2. Create a `simple_messages.py` and assign a message to a variable, and print that message. Then change the value of the variable to a new message, and print the new message.

## Strings

A string is a series of characters and anything inside quotes is considered a string in Python. You can use single or double quotes.

```python
"This is a string"
'This is also a string'
```

This allows you to use quotes within your string:

```python
"This is a 'string'"
```

### String Methods

You have a complete built-in methods that you can use on strings [here](https://www.w3schools.com/python/python_ref_string.asp). Some popular ones are `capitalize()`, `lower()`, `replace()`, `split()`, `strip()` or `upper()`.

### Using Variables in Strings

In some situations you'll want to use variable's value inside a string.

```python
first_name = "John"
last_name = "Smith"
full_name = f"Hello, {first_name} {last_name}"
print(full_name)
```

These strings are called f-strings (format strings), because you can simple replace the name of any variable in braces with its value.

You can also add tabs or new lines to strings with `\t` and `\n`.

```python
first_name = "John"
last_name = "Smith"
full_name = f"Hello, \n\t{first_name} \n\t{last_name}"
print(full_name)
```

### Exercises

1. Use a variable to represent a person's name, and then print that person's name preceded by a tab, in lowercase, uppercase, and title case. You can use the same variable and override its value.

## Numbers

### Integers

- You can add (+), substract (-), multiply (*) and divide (/) integers.
- Exponents are represented with two multiplication symbols (**).
- You can use parentheses to modify the order of operations. e.g. `2 + 3 * 4` is not the same as `(2 + 3) * 4`.

### Floats

Python calls any number with a decimal point a float. e.g. `0.2`

- Wen you divide integer numbers you will always get a float.
- If you mix integers and floats you will get a float.

>You can use underscores when writing long numbers to improve readability. e.g. (`14_000_000`). The underscores won't be printed out.

>Use capital letters when you are defining a constant. e.g. `MAX_TIMEOUT = 5000` A constant never changes.

### Exercises 

1. Write a addition, substraction, multiplication and division that result in the number 8. Print the values.

## Comments

In Python, the hash mark (#) indicates a comment. Anything following a hash mark is your code is ignored by the Python interpreter.

```python
# This is just a comment and will be ignored
print("Hello World")
```

>You should write meaningful comments. However don't overuse comments, sometimes a variable or method with a meaningful name is much better.
