import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import unittest
from src.huffman_compressor import HuffmanCompressor

class TestHuffmanCompressor(unittest.TestCase):
    def test_compress_and_decompress(self):
        data = "hello huffman"
        compressor = HuffmanCompressor(data)
        
        # Act
        compressed_data = compressor.compress()
        decompressed_data = compressor.decompress(compressed_data)

        # Assert
        self.assertEqual(decompressed_data, data)

if __name__ == "__main__":
    unittest.main()
