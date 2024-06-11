"""A hashing function is used to convert strings and other non-numeric data types into numbers,
which can then be used as list indices."""
MAX_HASH_TABLE_SIZE = 5000


def get_index(data_list, astring):
    result = 0
    for achar in astring:
        anum = ord(achar)
        result += anum

    list_index = result % len(data_list)
    return list_index


def get_valid_index(data_list, astring):
    result = 0
    for achar in astring:
        anum = ord(achar)
        result += anum

    idx = result % len(data_list)
    while True:
        kv = data_list[idx]
        if kv is None:
            return idx

        k, v = kv
        if k == astring:
            return idx

        idx += 1

        if idx == len(data_list):
            idx = 0


class BasicHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None for _ in range(max_size)]

    def insert(self, key, value):
        idx = get_index(data_list=self.data_list, astring=key)
        self.data_list[idx] = (key, value)

    def get(self, key):
        idx = get_index(data_list=self.data_list, astring=key)
        kv = self.data_list[idx]
        return kv[1] if kv is not None else None

    def update(self, key, value):
        idx = get_index(data_list=self.data_list, astring=key)
        self.data_list[idx] = (key, value)

    def get_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]


if __name__ == "__main__":
    data_list = [None for _ in range(MAX_HASH_TABLE_SIZE)]
    print(len(data_list))
    print(data_list[99])
    print(get_index(data_list, '') == 0)
    print(get_index(data_list, 'Aakash') == 585)
    print(get_index(data_list, 'Don O Leary') == 941)
    key, value = "Akshay", "9876543210"
    idx = get_index(data_list, key)
    data_list[idx] = (key, value)
    kv = data_list[idx]
    print(kv)
    data_list2 = [None] * MAX_HASH_TABLE_SIZE
    print(get_valid_index(data_list2, 'listen') == 655)
    data_list2[get_index(data_list2, 'listen')] = ('listen', 99)
    print(get_valid_index(data_list2, 'silent') == 656)