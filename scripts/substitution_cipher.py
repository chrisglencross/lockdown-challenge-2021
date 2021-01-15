plain_text = """
STAR WARS : EPISODE 1:THE PHANTOM MENACE

TITLE CARD : A long time ago in a galaxy far, far away....

A vast sea of stars serves as the backdrop for the main title, followed by a roll up, which crawls up into infinity.

EPISODE 1 THE PHANTOM MENACE

Turmoil has engulfed the Galactic Republic. The taxation of trade routes to outlaying star systems is in dispute.

Hoping to resolve the matter with a blockade of deadly battleships, the greedy Trade Federation has stopped all shipping to the small planet of Naboo.

While the congress of the Republic endlessly debates this alarming chain of events, the Supreme Chancellor has secretly dispatched two Jedi Knights, the guardians of peace and justice in the galaxy, to settle the conflict.....

PAN DOWN to reveal a small space cruiser heading TOWARD CAMERA at great speed.
PAN with the cruiser as it heads toward the beautiful green planet of Naboo, which is surrounded by hundreds of Trade Federation battleships.

The space cruiser explodes to reveal the code word lightsabre. I hope you enjoyed the clue.
"""

import random

alphabet = [chr(letter) for letter in range(ord('A'), ord('Z') + 1)]
remaining_letters = list(alphabet)

mapping = {}
for letter in alphabet:
    map_to_letter = random.choice(remaining_letters)
    remaining_letters.remove(map_to_letter)
    mapping[letter] = map_to_letter

print(mapping)
print()
encoded = "".join([mapping.get(letter.upper(), letter.upper()) for letter in plain_text])
print(encoded)
