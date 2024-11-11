import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from huffman_tree import HuffmanTree

class TestHuffmanTree(unittest.TestCase):
    def test_generate_codes(self):
        data = "hello huffman"
        tree = HuffmanTree(data)
        tree.generate_codes()

        self.assertTrue(len(tree.codes) > 0)
        self.assertIn('h', tree.codes)

if __name__ == "__main__":
    unittest.main()
