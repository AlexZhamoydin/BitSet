class BitSetException(Exception):
    def __init__(self, message):
        super(BitSetException, self).__init__(message)


class BitSet:
    def __init__(self):
        self._set = 0

    def __str__(self):
        # TODO: rework str representation
        return format(self._set, 'b').zfill(256)

    @staticmethod
    def is_valid_char(char):
        """Checks if char belongs to ASCII table

        :param char: char which value is checked
        :return: True if char belongs to ASCII table.
        """
        if len(char) != 1:
            raise BitSetException("Char expected")
        return 0 <= ord(char) < 127

    @property
    def set(self):
        return self._set

    def add(self, char):
        """Adds an element to set

        :param char:
        :return: True if
        """
        if not BitSet.is_valid_char(char):
            raise BitSetException("Invalid character")
        else:
            pass

    def delete(self, char):
        """Deletes an element from set

        :param char:
        :return:
        """
        if not BitSet.is_valid_char(char):
            raise BitSetException("Invalid character")
        else:
            pass


a = BitSet()
a.add('a')
print(a)
