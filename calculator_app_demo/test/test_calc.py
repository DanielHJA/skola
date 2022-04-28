from src.calc import add


def test_add():
    assert 3 == add(1, 2)
    assert 3 == add(2, 1)
    assert -1 == add(-2, 1)
    # Failing test
    # assert -1 == add(-20, 1)


if __name__ == "__main__":
    # Run test when starting program
    try:
        test_add()
    except AssertionError as err:
        print("Test failed")
        raise
    print("All tests passed!")