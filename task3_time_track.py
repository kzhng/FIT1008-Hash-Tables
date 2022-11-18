import timeit
from task3_hash_table import HashTable


def file_to_list(file_name):
    if not isinstance(file_name, str):
        raise ValueError("file name must be a string")

    if file_name[-4:] != ".txt":
        raise ValueError("file name must be text type")

    file = open(file_name, 'r')
    words_list = []
    for line in file:
        line_string = line.strip()
        line_string = line_string
        words_list.append(line_string)
    file.close()
    return words_list


def time_to_hash(word_list, table_size, base):
    hash_table = HashTable(table_size, base)
    start = timeit.default_timer()
    for i in word_list:
        hash_table[i] = i
    taken = (timeit.default_timer() - start)
    collisions = hash_table.collisions
    average_probe_length = hash_table.total_probe_length / hash_table.count
    return taken, collisions, average_probe_length


def wall_time_for_english_small():
    word_list = file_to_list("english_small.txt")
    base = 101
    print("statistics for small english dictionary: (wall time, collisions, average probe length)")
    print("table size is 210000: {}".format(time_to_hash(word_list, 210000, base)))
    print("table size is 209987: {}".format(time_to_hash(word_list, 209987, base)))
    print("table size is 400000: {}".format(time_to_hash(word_list, 400000, base)))
    print("table size is 399989: {}".format(time_to_hash(word_list, 399989, base)))
    print("table size is 202361: {}".format(time_to_hash(word_list, 202361, base)))


def wall_time_for_english_large():
    word_list = file_to_list("english_large.txt")
    base = 101
    print("statistics for large english dictionary: (wall time, collisions, average probe length)")
    print("table size is 210000: {}".format(time_to_hash(word_list, 210000, base)))
    print("table size is 209987: {}".format(time_to_hash(word_list, 209987, base)))
    print("table size is 400000: {}".format(time_to_hash(word_list, 400000, base)))
    print("table size is 399989: {}".format(time_to_hash(word_list, 399989, base)))
    print("table size is 202361: {}".format(time_to_hash(word_list, 202361, base)))


def wall_time_for_french():
    word_list = file_to_list("french.txt")
    base = 101
    print("statistics for french dictionary: (wall time, collisions, average probe length)")
    print("table size is 210000: {}".format(time_to_hash(word_list, 210000, base)))
    print("table size is 209987: {}".format(time_to_hash(word_list, 209987, base)))
    print("table size is 400000: {}".format(time_to_hash(word_list, 400000, base)))
    print("table size is 399989: {}".format(time_to_hash(word_list, 399989, base)))
    print("table size is 202361: {}".format(time_to_hash(word_list, 202361, base)))


def statistics_for_hash_table():
    table_size = 399989
    base = 101
    english_small_list = file_to_list("english_small.txt")
    english_large_list = file_to_list("english_large.txt")
    french_list = file_to_list("french.txt")
    print("(wall time, collisions, average probe length)")
    print("statistics for small english dictionary: base {}, table size {}: {}"
          .format(base, table_size, time_to_hash(english_small_list, table_size, base)))
    print("statistics for large english dictionary: base {}, table size {}: {}"
          .format(base, table_size, time_to_hash(english_large_list, table_size, base)))
    print("statistics for french dictionary: base {}, table size {}: {}"
          .format(base, table_size, time_to_hash(french_list, table_size, base)))


if __name__ == '__main__':
    wall_time_for_english_small()
    wall_time_for_english_large()
    wall_time_for_french()
    statistics_for_hash_table()
