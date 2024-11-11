
from huffman_tree import HuffmanTree

class HuffmanCompressor:
    def __init__(self, data):
        self.data = data
        self.tree = HuffmanTree(data)
        self.tree.generate_codes()

    def compress(self):
        encoded_data = ''.join(self.tree.codes[char] for char in self.data)
        return encoded_data

    def decompress(self, encoded_data):
        current_code = ""
        decoded_text = ""

        for bit in encoded_data:
            current_code += bit
            if current_code in self.tree.reverse_codes:
                character = self.tree.reverse_codes[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text
