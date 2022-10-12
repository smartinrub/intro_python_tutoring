# Loops

You'll often want to run through all entries in a list and perform the same action with every item, you can use Python's `for` loop.

## Iteration

```python
sports = ['football', 'basketball', 'tennis', 'rugby']
for sport in sports:
    print(sport)
```

>Always indent the line after the for statement in a loop. If you want to run multiple statement you have to indent all of them.

## Numerical Lists

Use `range()` method to generate a series of numbers and iterate through them.

```python
for value in range(1, 5):
    print(value)
```
