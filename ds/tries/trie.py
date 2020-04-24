class Node:
    def __init__(self, alphabet_size):
        # isend? of word
        self.end_of_word = False
        self.alphabet_size = alphabet_size
        # Stores number of strings that are possible fromt this node
        self.strings_possible_from_here = 0
        self.children_map = [None for _ in range(alphabet_size)]

    def __repr__(self):
        return f'end? = {self.end_of_word}, strings_possible_from_here = {self.strings_possible_from_here}'

    def is_leaf(self):
        for i in range(self.alphabet_size):
            if self.children_map[i]:
                return False
        return True

# Trie for lowercase english letter words or for |alphabet| = 26
# Pass the mapper function for mapping keys = 0 ... size - 1 if not default impl
class Trie:
    def __init__(self, alphabet_size):
        self.alphabet_size = alphabet_size
        self.root = Node(self.alphabet_size)

    # Mapping 'a' to 0 
    def mapper(self, ch):
        return ord(ch) - 97

    def rev_mapper(self, idx):
        return chr(idx + 97)

    def build(self, words):
        for word in words:  
            self.insert(self.root, word, 0)

    def insert(self, root, word, word_i):
        if word_i == len(word):
            root.end_of_word = True 
            return 
        pos = self.mapper(word[word_i]) # ->bat node for b, b->at node for a
        # If b mapping is there then go to a
        if root.children_map[pos]:
            self.insert(root.children_map[pos], word, word_i + 1)
        else:
            new_node = Node(self.alphabet_size)
            root.children_map[pos] = new_node
            self.insert(root.children_map[pos], word, word_i + 1)

        root.strings_possible_from_here += 1

    def delete(self, word):
        def helper(root, word, word_i):
            if word_i == len(word):
                root.end_of_word = False 
                return None if root.is_leaf() else root

            pos = self.mapper(word[word_i])
            root.children_map[pos] = helper(root.children_map[pos], word, word_i + 1)
            root.strings_possible_from_here -= 1

            return root

        if self.in_trie(word):
            helper(self.root, word, 0)
        else:
            print(f'{word} not present in Trie')

    def print_all(self, root=None, prefix_string=''):
        def helper(root, prefix_string, acc):
            if root.end_of_word:
                acc.append(prefix_string)
            for i in range(self.alphabet_size):
                if root.children_map[i]:
                    helper(root.children_map[i], prefix_string + self.rev_mapper(i), acc)
        acc = []
        if not root:
            helper(self.root, prefix_string, acc)
        else:
            helper(root, prefix_string, acc)
        print(acc)

    def in_trie(self, prefix_string):
        root = self.root 
        for s in prefix_string:
            root = root.children_map[self.mapper(s)]
            if not root:
                return False
        return True

    def traverse_to(self, prefix_string):
        root = self.root 
        for s in prefix_string:
            root = root.children_map[self.mapper(s)]
            if not root:
                raise Exception(f'{prefix_string} is not present in trie')
        return root

    def starts_with(self, prefix_string):
        root = self.traverse_to(prefix_string)
        self.print_all(root, prefix_string)

    def starts_with_count(self, prefix_string):
        root = self.traverse_to(prefix_string)
        return root.strings_possible_from_here

def main():
    trie = Trie(26)
    trie.build(['bac', 'bacs','bacsss', 'tap'])
    print(trie.root.children_map[1])
    print(trie.root.children_map[1].children_map[0])
    print(trie.root.children_map[1].children_map[0].children_map[2])

    trie.delete('tap')
    trie.print_all()
    print(trie.starts_with_count('ba'))

if __name__ == '__main__':
    main()