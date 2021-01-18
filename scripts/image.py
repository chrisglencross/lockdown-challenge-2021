import itertools
from queue import PriorityQueue

from PIL import Image
from graphviz import Digraph

image: Image = Image.open('droid.png')

COLOURS = {
    (0, 0, 0): "black",
    (127, 127, 127): "grey",
    (0, 0, 255): "blue",
    (255, 0, 0): "red",
    (255, 255, 255): "white"
}

pixels = []
for y in range(0, image.height):
    for x in range(0, image.width):
        r, g, b, _ = image.getpixel((x, y))
        name = COLOURS[(r, g, b)]
        pixels.append(name)
print(pixels)


def find_index(full_list, sublist, start_index):
    for i in range(start_index, len(full_list) - len(sublist)):
        if full_list[i:i + len(sublist)] == sublist:
            return i
    return None


output = []
x = 0
while x < len(pixels):
    max_sublist = None
    for y in range(x + 16, len(pixels)):
        sublist = pixels[x:y]
        index = find_index(pixels, sublist, max(0, x - 256))
        if index < x:
            max_sublist = (x - index, len(sublist), sublist)
        else:
            break
    if max_sublist:
        output.append(max_sublist)
        x += max_sublist[1]
    else:
        output.append(pixels[x])
        x += 1

print(len(pixels))
print(len(output))

dictionary_tokens = [c for c in output if type(c) is str]
dictionary_tokens += ["LENGTH-DISTANCE" for c in output if type(c) is not str]

frequencies = [(len(list(cs)), c) for c, cs in itertools.groupby(sorted(dictionary_tokens))]
print(frequencies)

queue = PriorityQueue()
for frequency, colour in frequencies:
    queue.put((frequency, colour, None, None))

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
    frequency, colour, left, right = node
    if colour:
        dot.node(path, colour + "\n" + path, color='red')
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
dot.render('image', view=True, format='svg')

cipher_text = []
bits = []


def to_binary(i):
    return format(i, "08b")


bits.append(to_binary(image.width))
bits.append(to_binary(image.height))
print(image.size)

print("Output:")
print(output)

for c in output:
    if type(c) is str:
        bits.append(dictionary[c])
    else:
        bits.append(dictionary["LENGTH-DISTANCE"])
        bits.append(to_binary(c[1]))
        bits.append(to_binary(c[0]))

print(len([bit for chunk in bits for bit in chunk]) / 8)

outstr = []
for i, bit in enumerate([bit for chunk in bits for bit in chunk]):
    outstr.append(bit)
    if i % 8 == 7:
        outstr.append(" ")

print(outstr)
result = "".join(outstr)
print(result)
