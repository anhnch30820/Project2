# mtfwiki.py
import os
from typing import List, Tuple, Union
class Movetofront:

    def __init__(self, path):
        self.common_dictionary = list(range(256))
        self.path = path
    # print(encod(plain_text))

    def encod(self, plain_text: str) -> List[int]:
        # Change to bytes for 256.

        plain_text = plain_text.encode('utf-8')

        dictionary = self.common_dictionary.copy()
        rank = 0
        s = []
        for i in plain_text:
            rank = dictionary.index(i)
            s.append(rank)
            dictionary.pop(rank)
            dictionary.insert(0, i)
        return s

    def compress(self):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + "_MTF.txt"
        f = open(self.path, 'r')
        w = open(output_path, 'w')

        s = f.read()
        a = self.encod(s)
        string_ints = [str(int) for int in a]
        str_of_ints = ",".join(string_ints)
        w.write(str_of_ints)

        f.close()
        w.close()

        print("Compressed successful Movetofront")
        return output_path

    def decode(self, compressed_data: List[int]) -> str:
        compressed_text = compressed_data

        dictionary = self.common_dictionary.copy()
        plain_text = []

        # Read in each rank in the encoded text
        for rank in compressed_text:
            plain_text.append(dictionary[rank])
            a = dictionary.pop(rank)
            dictionary.insert(0, a)

        return bytes(plain_text).decode('utf-8')  # Return original string

    def decompress(self, input_path):

        output_path = input_path[:-4] + "_MTF.txt"

        f = open(input_path, 'r')
        w = open(output_path, 'w')

        s = f.read()
        s = s.split(',')
        s = list(s)
        nums = list(map(int, s))

        output = self.decode(nums)
        w.write(output)
        print("Decompressed successful Movetofront")
        return output_path




