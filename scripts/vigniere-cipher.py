plain_text = """
VADER: There is no escape.  Don't make me destroy you.  You do not yet realize your importance.  You have only begun to discover your power.  Join me and I will complete your training.  With our combined
strength, we can end this destructive conflict and bring order to the galaxy.

LUKE: I'll never join you!

VADER: If you only knew the power of the dark side.  Obi-Wan never told you what happened to your father.

LUKE: He told me enough!  It was you who killed him.

VADER: No.  I am your father.

Shocked, Luke looks at Vader in utter disbelief.

LUKE: No.  No.  That's not true! That's impossible!

VADER: Search your feelings.  You know it to be true.

LUKE: No!  No!  No!

VADER: Luke.  You can destroy the Emperor.  He has foreseen this.  It is your destiny.  Join me, and together
we can rule the galaxy as father and son.  Come with me.  It is the only way.

The code phrase is Yoda.
"""

key = [ord(c) - ord('A') + 1 for c in "YODA"]

index = 0
output = []
frequencies = {}
for i in range(0, 4):
    frequencies[i] = {chr(c): 0 for c in range(ord('A'), ord('Z') + 1)}
for c in plain_text.upper():
    if c.isalpha():
        frequencies[index % 4][c] = frequencies[index % 4][c] + 1
        c = chr(ord('A') + ((ord(c) - ord('A') - key[index % 4]) % 26))
        index += 1
    output.append(c)

for i in range(0, 4):
    print(frequencies[i])

output = "".join(output)
print(output)
