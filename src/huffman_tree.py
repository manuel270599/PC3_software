
from heapq import heappush, heappop
from collections import Counter
from huffman_node import HuffmanNode

class HuffmanTree:
    def __init__(self, data):
        self.data = data
        self.codes = {}
        self.reverse_codes = {}
        self.root = self._build_tree()

    def _build_tree(self):
        frequency = Counter(self.data)
        heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
        for node in heap:
            heappush(heap, node)

        while len(heap) > 1:
            left = heappop(heap)
            right = heappop(heap)
            merged = HuffmanNode(freq=left.freq + right.freq)
            merged.left = left
            merged.right = right
            heappush(heap, merged)

        return heap[0] if heap else None

    def generate_codes(self, node=None, current_code=""):
        if node is None:
            node = self.root

        if node.char is not None:
            self.codes[node.char] = current_code
            self.reverse_codes[current_code] = node.char
            return

        if node.left:
            self.generate_codes(node.left, current_code + "0")
        if node.right:
            self.generate_codes(node.right, current_code + "1")
