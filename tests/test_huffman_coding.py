import unittest
from unittest import mock
from unittest.mock import mock_open
from src.huffman_coding import (
    compress,
    decompress,
    build_huffman_tree,
    build_huffman_codes,
    write_tree_to_file,
    some_function,
)


class TestHuffmanCoding(unittest.TestCase):
    def setUp(self):
        self.text = "AAABBCCCC"
        self.tree = build_huffman_tree(self.text)
        self.codes = build_huffman_codes(self.tree)

    def test_build_huffman_tree(self):
        self.assertIsNotNone(self.tree)
        self.assertEqual(self.tree.freq, len(self.text))

    def test_build_huffman_codes(self):
        self.assertEqual(len(self.codes), len(set(self.text)))

    def test_compress(self):
        compressed_text, tree = compress(self.text)
        decompressed_text = decompress(compressed_text, tree)
        self.assertEqual(self.text, decompressed_text)  # Compara original y descomprimido

    @mock.patch("builtins.open", new_callable=mock_open)
    def test_write_tree_to_file(self, mock_file):
        write_tree_to_file(self.tree, "tree.txt")
        mock_file.assert_called_once_with("tree.txt", "w")
        # Puedes añadir más verificaciones si es necesario, como contenido escrito.

    @mock.patch("src.huffman_coding.write_tree_to_file")
    def test_some_function(self, mock_write_tree):
        some_function(self.tree)
        mock_write_tree.assert_called_once_with(self.tree, "tree.txt")


if __name__ == "__main__":
    unittest.main()
