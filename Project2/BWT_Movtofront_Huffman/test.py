from Encode_Decode_BWT import *
from Encode_Decode_Movetofront import *
from Encode_Decode_Huffman import *
from timeit import default_timer as timer

start = timer()

a = suffix()

encode_path = a.compress()
b = Movetofront(encode_path)
encode_path = b.compress()
c = HuffmanCoding(encode_path)
encode_path = c.compress()
decom_path = c.decompress(encode_path)
decom_path = b.decompress(decom_path)
decom_path = a.decompress(decom_path)


end = timer()
print(end - start)
