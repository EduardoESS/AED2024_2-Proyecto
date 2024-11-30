class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.start = -1
        self.end = -1
        self.suffix_link = None


class SuffixTree:
    def __init__(self, text):
        self.text = text
        self.root = SuffixTreeNode()
        self.build_suffix_tree()

    def build_suffix_tree(self):
        """
        Construye el Suffix Tree para el texto dado.
        Implementación básica para propósito ilustrativo.
        """
        for i in range(len(self.text)):
            self.insert_suffix(self.text[i:], i)

    def insert_suffix(self, suffix, index):
        """
        Inserta un sufijo en el árbol.
        """
        node = self.root
        for char in suffix:
            if char not in node.children:
                new_node = SuffixTreeNode()
                node.children[char] = new_node
            node = node.children[char]
        node.start = index
        node.end = len(self.text)

    def search(self, pattern):
        """
        Busca un patrón en el árbol.
        """
        node = self.root
        for char in pattern:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def get_tree_structure(self):
        """
        Devuelve una representación del árbol como lista para visualización.
        """
        result = []
        self._collect_edges(self.root, result, "")
        return result

    def _collect_edges(self, node, result, prefix):
        for char, child in node.children.items():
            result.append((prefix + char, child.start, child.end))
            self._collect_edges(child, result, prefix + char)
