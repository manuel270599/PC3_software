import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    if not text:
        raise ValueError("Input text cannot be empty.")
    
    # Contar frecuencias de caracteres
    freq = Counter(text)

    # Crear cola de prioridad
    heap = [HuffmanNode(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)

    # Construir el árbol de Huffman
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    return heap[0]

def build_huffman_codes(tree):
    codes = {}

    def traverse(node, prefix=""):
        if not node.left and not node.right:  # Es una hoja
            codes[node.char] = prefix
            return
        if node.left:
            traverse(node.left, prefix + "0")
        if node.right:
            traverse(node.right, prefix + "1")

    traverse(tree)
    return codes

def compress(text):
    tree = build_huffman_tree(text)
    codes = build_huffman_codes(tree)
    compressed_text = ''.join(codes[char] for char in text)
    return compressed_text, tree

def decompress(compressed_text, tree):
    result = []
    current = tree

    # Caso especial cuando el árbol tiene solo una hoja
    if not current.left and not current.right:
        return current.char * len(compressed_text)

    for bit in compressed_text:
        current = current.left if bit == "0" else current.right
        if not current.left and not current.right:  # Es una hoja
            result.append(current.char)
            current = tree
    return ''.join(result)

def write_tree_to_file(tree, filename):
    with open(filename, 'w') as f:
        def serialize(node):
            if node is None:
                return "#"
            if not node.left and not node.right:  # Es una hoja
                return f"{node.char}"
            return f"({serialize(node.left)}{serialize(node.right)})"
        f.write(serialize(tree))

def some_function(tree):
    write_tree_to_file(tree, "tree.txt")


if __name__ == "__main__":
    text = "AAABBCCCC"
    print("Texto original:", text)

    # Compresión
    compressed, tree = compress(text)
    print("Texto comprimido:", compressed)

    # Descompresión
    decompressed = decompress(compressed, tree)
    print("Texto descomprimido:", decompressed)

    # Verificar
    assert text == decompressed, "El texto original y descomprimido no coinciden."
