# Lists

A list is a collection of items in a particular order. You can make a list of letters, digits, strings...

```python
programming_languages = ['Python', 'Java', 'C#', 'Go']
print(programming_languages)
```

it will print `['Python', 'Java', 'C#', 'Go']`

## Access element in a List

```python
programming_languages = ['Python', 'Java', 'C#', 'Go']
print(programming_languages[1])
```

it will print `Java`

>Index positions start at 0, not 1

>If you use negative numbers for the index it will use a reverse order. `-1` is the last element, `-2` is the second element starting from the end, and so on and so forth.

### Exercises

1. Store in a list 3 names and print each name by accessing each element in the list, one at a time.

## Changing, Adding and Removing Elements

### Modifying elements

Use the index to modify an element from a list.

```python
sports = ['football', 'basketball', 'tennis', 'rugby']
sports[0] = 'badminton'
print(sports)
```

### Adding elements

Use `append()` to add additional values to a list.

```python
sports = ['football', 'basketball', 'tennis', 'rugby']
sports.append('badminton')
print(sports)
```

You can also add an element at any position in your list by using `insert()`.

```python
sports = ['football', 'basketball', 'tennis', 'rugby']
sports.insert(0, 'badminton')
print(sports)
```

### Removing elements

Use the `del` statement.

```python
sports = ['football', 'basketball', 'tennis', 'rugby']
del sports[0]
print(sports)
```

Use `pop()` to remove the last element of a list. You can also remove an element from a particular position with `pop(index)`

```python
sports = ['football', 'basketball', 'tennis', 'rugby']
sports.pop()
print(sports)
```

Use `remove()` to remove an element by value.

```python
sports = ['football', 'basketball', 'tennis', 'rugby']
sports.remove('basketball')
print(sports)
```

### Exercises

1. Create a list with 3 names and add an additional name on the second position and then remove the last one. You can use any of the methods from above.

## Organizing a List

Use `sort()` method to sort a list alphabetically. By passing the argument `reverse=True` to the `sort()` method.

```python
sports = ['football', 'basketball', 'tennis', 'rugby']
sports.sort()
print(sports)
sports.sort(reverse=True)
print(sports)
```

You can use `sorted()` to temporarily sort a list without chaging the order of the list.

You can reverse a list with `reverse()`.

```python
sports = ['football', 'basketball', 'tennis', 'rugby']
sports.reverse()
print(sports)
```

Use `len()` to find the length of a list.

```python
sports = ['football', 'basketball', 'tennis', 'rugby']
print(len(sports))
```
