```python
3//2
```




    1




```python
3%2
```




    1




```python
3/2
```




    1.5




```python
8%2
```




    0




```python
9%2
```




    1




```python
3**3
```




    27




```python
2**32
```




    4294967296




```python
2**64
```




    18446744073709551616




```python
True == 1
```




    True




```python
False == 0
```




    True




```python
my_var = "Hello"
my_var == "Hello"
```




    True




```python
x=1
x>2
```




    False




```python
if x > 2:
    print("X is more than 2")
    print("More text")
else:
    print("X isn't more than 2")
print("Left the condition")
```

    X isn't more than 2
    Left the condition



```python
x=x+2
x>2
```




    True




```python
if x > 2:
    print("X is more than 2")
    print("More text")
else:
    print("X isn't more than 2")
print("Left the condition")
```

    X is more than 2
    More text
    Left the condition



```python
if x < 1:
    print("X is less than 1")
elif my_var == "Hello":
    print("My var was hello")
else:
    print("Neither condition were matched")
```

    My var was hello



```python
if x < 1:
    print("X is less than 1")
elif my_var == "Alex":
    print("My var was hello")
else:
    # We should not do anything in this case
    pass  # Pass doesn't do anything, a so called no-op.

def work_in_progress():
    # This function will be implemented later
    # Two commented lines
    pass

def another_func():
    # This function will be implemented later
    pass

work_in_progress() is None
```




    True




```python
for x in range(10):
    print(x)
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9



```python
for name in ["Alex", "Kalle", "Anka", "Python"]:
    print(name)
```

    Alex
    Kalle
    Anka
    Python



```python
some_num = 0
while some_num < 10:
    print("Running")
    print(some_num)
    some_num = some_num + 1
```

    Running
    0
    Running
    1
    Running
    2
    Running
    3
    Running
    4
    Running
    5
    Running
    6
    Running
    7
    Running
    8
    Running
    9



```python
print(some_num + 1)
```

    11



```python
len("Alex")
```




    4




```python
len(["A", "l", "e", "x"])
```




    4




```python
for character in "Alex":
    print(character)
```

    A
    l
    e
    x



```python
# Define a start and stop value
for x in range(10, 20):
    print(x)
```

    10
    11
    12
    13
    14
    15
    16
    17
    18
    19



```python
# Version with start, stop and step
for x in range(10, 90, 10):
    print(x)
```

    10
    20
    30
    40
    50
    60
    70
    80



```python
def greet_someone(name):
    return f"Hello {name}!"
```


```python
greet_someone(name="Alex")
```




    'Hello Alex!'




```python
user_data = input()
```

     Alex was here



```python
print(user_data)
```

    Alex was here



```python
def greet_someone_somewhere(name, location):
    return f"Hello {name}, nice to see you in {location}!"
```


```python
greet_someone_somewhere("Alex")
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [64], in <cell line: 1>()
    ----> 1 greet_someone_somewhere("Alex")


    TypeError: greet_someone_somewhere() missing 1 required positional argument: 'location'



```python
greet_someone_somewhere("Alex", "USA")
```




    'Hello Alex, nice to see you in USA!'




```python
greet_someone_somewhere(name="Alex", location="USA")
```




    'Hello Alex, nice to see you in USA!'




```python
greet_someone_somewhere(location="USA", name="Alex")
```




    'Hello Alex, nice to see you in USA!'




```python
def greet_someone_somewhere_default_sweden(name, location="Sweden"):
    return f"Hello {name}, nice to see you in {location}!"
```


```python
greet_someone_somewhere_default_sweden("Alex")
```




    'Hello Alex, nice to see you in Sweden!'




```python

```
