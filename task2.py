import timeit
from task1 import HashTable


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


def time_to_hash(word_list, table_size):
    hash_table = HashTable(table_size)
    start = timeit.default_timer()
    for i in word_list:
        hash_table[i] = i
    taken = (timeit.default_timer() - start)
    return taken


def wall_time_for_english_small():
    word_list = file_to_list("english_small.txt")
    print("wall time for small english dictionary: ")
    print("table size is 210000: {}".format(time_to_hash(word_list, 210000)))
    print("table size is 209987: {}".format(time_to_hash(word_list, 209987)))
    print("table size is 400000: {}".format(time_to_hash(word_list, 400000)))
    print("table size is 399989: {}".format(time_to_hash(word_list, 399989)))
    print("table size is 202361: {}".format(time_to_hash(word_list, 202361)))


def wall_time_for_english_large():
    word_list = file_to_list("english_large.txt")
    print("wall time for large english dictionary: ")
    print("table size is 210000: {}".format(time_to_hash(word_list, 210000)))
    print("table size is 209987: {}".format(time_to_hash(word_list, 209987)))
    print("table size is 400000: {}".format(time_to_hash(word_list, 400000)))
    print("table size is 399989: {}".format(time_to_hash(word_list, 399989)))
    print("table size is 202361: {}".format(time_to_hash(word_list, 202361)))


def wall_time_for_french():
    word_list = file_to_list("french.txt")
    print("wall time for french dictionary: ")
    print("table size is 210000: {}".format(time_to_hash(word_list, 210000)))
    print("table size is 209987: {}".format(time_to_hash(word_list, 209987)))
    print("table size is 400000: {}".format(time_to_hash(word_list, 400000)))
    print("table size is 399989: {}".format(time_to_hash(word_list, 399989)))
    print("table size is 202361: {}".format(time_to_hash(word_list, 202361)))


if __name__ == '__main__':
    wall_time_for_english_small()
    wall_time_for_english_large()
    wall_time_for_french()
