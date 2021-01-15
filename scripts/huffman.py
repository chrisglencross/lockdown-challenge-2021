import itertools
import queue

from graphviz import Digraph

training_text = """
Letter frequency is simply the amount of times letters of the alphabet appear on average in written language. Letter frequency analysis dates back to the Arab mathematician Al-Kindi (c. 801–873 AD), who formally developed the method to break ciphers. Letter frequency analysis gained importance in Europe with the development of movable type in 1450 AD, where one must estimate the amount of type required for each letterform. Linguists use letter frequency analysis as a rudimentary technique for language identification, where it's particularly effective as an indication of whether an unknown writing system is alphabetic, syllabic, or ideographic.

The use of letter frequencies and frequency analysis plays a fundamental role in cryptograms and several word puzzle games, including Hangman, Scrabble and the television game show Wheel of Fortune. One of the earliest descriptions in classical literature of applying the knowledge of English letter frequency to solving a cryptogram is found in Edgar Allan Poe's famous story The Gold-Bug, where the method is successfully applied to decipher a message instructing on the whereabouts of a treasure hidden by Captain Kidd.[1]

Letter frequencies also have a strong effect on the design of some keyboard layouts. The most frequent letters are on the bottom row of the Blickensderfer typewriter, and the home row of the Dvorak keyboard layout.
""".lower()

total_letters = len([c for c in training_text if c.isalpha() or c == " "])
frequencies = [(len(list(cs)), c) for c, cs in itertools.groupby(sorted(training_text)) if c.isalpha() or c == " "]
print(frequencies)

queue = queue.PriorityQueue()
for frequency, letter in frequencies:
    queue.put((frequency / total_letters, letter, None, None))

while True:
    left = queue.get_nowait()
    if queue.empty():
        break
    right = queue.get_nowait()
    queue.put((left[0] + right[0], '', left, right))


def add_to_dictionary(dictionary, path, node):
    frequency, letter, left, right = node
    if letter:
        dictionary[letter] = path
    else:
        add_to_dictionary(dictionary, path + "0", left)
        add_to_dictionary(dictionary, path + "1", right)


def add_to_graph(dot: Digraph, path, node):
    frequency, letter, left, right = node
    if letter:
        dot.node(path, ("space" if letter == " " else letter) + "\n" + path, color='red')
    else:
        dot.node(path)
        left_path = path + "0"
        right_path = path + "1"
        add_to_graph(dot, left_path, left)
        add_to_graph(dot, right_path, right)
        dot.edge(path, left_path, "0")
        dot.edge(path, right_path, "1")


dictionary = {}
print(left)
add_to_dictionary(dictionary, "", left)
print(dictionary)

dot = Digraph(comment="Encoding Tree")
add_to_graph(dot, "", left)
print(dot)
dot.render('huffman', view=True, format='svg')

plain_text = "help me obi won kenobi you are my only hope"
cipher_text = []
print("".join([dictionary[c] for c in plain_text]))

# you only have 24 bytes, 43 bytes
