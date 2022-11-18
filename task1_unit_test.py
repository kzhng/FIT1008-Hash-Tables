from task1 import HashTable


def test_get_item():
    try:
        error_table = HashTable(9973)
        error_table[29]
        assert False, "test failed: ValueError not triggered when integer type is entered for key"
    except ValueError:
        assert True

    try:
        a_table = HashTable(9973)
        a_table["foobar"]
        assert False, "test failed: invalid key not triggering KeyError"
    except KeyError:
        assert True

    try:
        err_table = HashTable(10)
        for i in range(10):
            err_table["{}".format(i)] = "foobar"
        err_table["cookies"]
    except KeyError:
        assert True

    b_table = HashTable(9973)
    b_table["Phil"] = "FIT1045"
    b_table["Julian"] = "FIT1008"
    assert b_table["Phil"] == "FIT1045", "test failed: value for key phil fit1045 != fit1045"
    assert b_table["Julian"] == "FIT1008", "test failed: value for key julian is fit1008 != fit1008"


def test_set_item():
    try:
        error_table = HashTable(9973)
        error_table[29]
        assert False, "test failed: ValueError not triggered when integer type is entered for key"
    except ValueError:
        assert True

    try:
        err_table = HashTable(11)
        for i in range(11):
            err_table["{}".format(i)] = "ducks"
        err_table["ice"] = "cream"
        assert False, "Test failed: StopIteration not triggered when the hash table is full and trying to insert tuple"
    except StopIteration:
        assert True

    a_table = HashTable(9973)
    a_table["Phil"] = "FIT1045"
    a_table["Julian"] = "FIT1008"
    assert a_table["Phil"] == "FIT1045", "test failed: value for key phil fit1045 != fit1045"
    assert a_table["Julian"] == "FIT1008", "test failed: value for key julian is fit1008 != fit1008"


def test_contains():
    try:
        error_table = HashTable(9973)
        error_table[29]
        assert False, "test failed: ValueError not triggered when integer type is entered for key"
    except ValueError:
        assert True

    a_table = HashTable(9973)
    assert "foo" not in a_table, "test failed: foo in hash table in table but in table"
    a_table["hello"] = "world"
    assert "hello" in a_table, "test failed: hello key not in hash table but in table"
    assert "bar" not in a_table, "test failed: bar not in hash table but in table"


def test_hash():
    pass


def test_str():
    pass


if __name__ == '__main__':
    test_get_item()
    test_set_item()
    test_contains()
    test_hash()
    test_str()
    print("all tests passing...")
