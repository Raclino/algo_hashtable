class Hashtable:
    """
    In this file you will find the function you need to
    implement. You SHOULD NOT change the name of each
    function, otherwise we will not be able to grade your
    work.
    """
    def __init__(self, size):
        """
        This is where you will initialize your hashtable.
        By default it value is None but feel free to change
        it to whatever you want, we will not grade you on how
        the inner function are define but on what we get and
        how fast we get it.

        Just note that size is the size of the hashtable. If
        size is '5' then your hashtable should have a size of
        5. This will cause some issue that you have to solve.
        :param size: The size of the hashtable
        """
        self.table = [None] * size

    def insert(self, key: str, val: object) -> str:
        """
        This function add an element to the hashtable. A simple
        implementation could be to put the first element into
        the first position, the second in second position...
        But this is just the beginning. You should also look
        for a thing called "collision"
        :param key: The key of the element we want to insert. Be
        aware that we can ask you to insert twice an element with
        the same key but different value. This will be tested
        during the oral evaluation
        :param val: The value associated with the key
        :return: The position of the element into the hashtable
        """
        i = hash(key) % len(self.table)
        j = 0
        dup = False
        bucket = []
        bucket = self.table[i]

        if bucket is None:
            self.table[i] = [(key, val)]
        else:
            for kv in bucket:
                k, v = kv
                if k == key:
                    dup = True
                    break
                j = j + 1
            if dup == True:
                bucket[j] = (key, val)
            else:
                bucket.append((key, val))

        return (i, j)

    def find(self, key: str):
        """
        This function will find an element into the hashtable and
        return it value. If the key is in the hashtable then you
        should return the value. If the key isn't in the hashtable
        then the program should return None
        :param key: The key we are looking for
        :return: The value or None if the key doesn't exist
        """
        i = hash(key) % len(self.table)
        bucket = []
        bucket = self.table[i]

        if bucket is None:
            return None
        else:
            for kv in bucket:
                k, v = kv
                if k == key:
                    return v
            return None
        

    def remove(self, key: str) -> bool:
        """
        This function remove an element of the hashtable. If the element
        doesn't exist, or if for some reason it could not be deleted then
        the program should return False. Otherwise True is expected.
        :param key: The key we want to remove.
        :return: True upon success, False otherwise
        """
        i = hash(key) % len(self.table)
        j = 0
        bucket = []
        bucket = self.table[i]

        if bucket is None:
            return False
        else:
            for kv in bucket:
                k, v = kv
                if k == key:
                    bucket.pop(j)
                    if len(bucket) == 0:
                        self.table[i] = None
                    return True
                j = j + 1
            return False
