import random

# Create a random grid
for x in range(0, 10):
    print(",".join([chr(random.randint(ord('A'), ord('Z'))) for y in range(0, 10)]))


def next_value(value):
    return int(str(value * value).zfill(4)[1:3])


lengths = {}
for seed in range(0, 100):
    already_seen = set()
    number = seed
    counter = 0
    print(f"\nseed: {seed}")
    while number not in already_seen:
        counter += 1
        already_seen.add(number)
        number = next_value(number)
        print(f"{counter}: {number}")
    lengths[seed] = counter

print(sorted([(key, value) for value, key in lengths.items()]))
