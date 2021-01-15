import itertools
from queue import PriorityQueue

from graphviz import Digraph

plain_text = "Bananas in Pyjamas Are Coming down the Stairs Bananas in Pyjamas Are Coming down in pairs Bananas in Pyjamas Are Chasing teddy bears".lower().replace(
    "\n", " ")
plain_text = plain_text

print(plain_text)
print(len(plain_text))

output = []
x = 0
while x < len(plain_text):
    max_substring = None
    for y in range(x + 5, len(plain_text)):
        substring = plain_text[x:y]
        index = plain_text.index(substring, max(0, x - 256))
        if index < x:
            max_substring = (x - index, len(substring), substring)
        else:
            break
    if max_substring:
        output.append(max_substring)
        x += max_substring[1]
    else:
        output.append(plain_text[x])
        x += 1

print(output)
print(len(output))

dictionary_tokens = [c for c in output if type(c) is str]
dictionary_tokens += ["LENGTH-DISTANCE" for c in output if type(c) is not str]

total_tokens = len([c for c in dictionary_tokens])
frequencies = [(len(list(cs)), c) for c, cs in itertools.groupby(sorted(dictionary_tokens))]
print(frequencies)

queue = PriorityQueue()
for frequency, letter in frequencies:
    queue.put((frequency / total_tokens, letter, None, None))

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
dot.render('huffman', view=True, format='svg')

cipher_text = []
bits = []


def to_binary(i):
    return format(i, "08b")


for c in output:
    if type(c) is str:
        bits.append(dictionary[c])
    else:
        bits.append(dictionary["LENGTH-DISTANCE"])
        bits.append(to_binary(c[1]))
        bits.append(to_binary(c[0]))

result = "".join(bits)
print(len(result) // 8)
print(result)
