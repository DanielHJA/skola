def add(x, y):
    """
    Returns the sum of x and y
    """
    # ^ This is a multi-line doc-string ("""),
    #   used to document the function.
    return x + y


def test_add():
    assert 3 == add(1, 2)
    assert 3 == add(2, 1)
    assert -1 == add(-2, 1)
    # Failing test
    # assert -1 == add(-20, 1)


if __name__ == "__main__":
    # Run test when starting program
    test_add()

    # Read input from user, convert to int
    our_x = int(input())
    our_y = int(input())
    # Calculate the answer
    answer = add(our_x, our_y)
    # Print out the answer
    print(answer)
