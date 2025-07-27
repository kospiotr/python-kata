def assert_arrays(left, right):
    print(left, '==', right)
    left.sort()
    right.sort()
    assert len(left) == len(right)
    for index in range(len(right)):
        assert left[index] == right[index]