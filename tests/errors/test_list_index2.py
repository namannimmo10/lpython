from lpython import i32

def test_list_index2_error():
    a: list[i32]
    a = [1, 2, 3]
    print(a.index(1, 1))

test_list_index2_error()
