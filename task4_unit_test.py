from task4_hash_table import HashTable


def test_getitem():
    a_table = HashTable(10)
    for i in range(13):
        a_table["{}".format(i)] = "lemons"
    assert a_table.table_size == 20, "test failed: underlying array size not properly updated"
    assert a_table.count == 13, "test failed: data of the hash table has been lost"
    b_table = HashTable(67)
    for j in range(500):
        b_table["{}".format(j)] = "limes"
    assert b_table.count == 500, "test failed: count of elements in hash table not properly counted"
    assert b_table.table_size == 1072, "test failed: underlying array size not properly updated"


if __name__ == '__main__':
    test_getitem()
    print("all tests passing...")
