def calc_checksum(word: str):
    checksum = 0
    for char in word:
        checksum = (checksum * checksum + ord(char) - ord('A') + 1) % 100
    return checksum


for word in ['HELLO', 'ALICE', 'LOVES', 'BATTLE']:
    print(word, calc_checksum(word))
print()

print("Make sure the following are not valid:")
for word in ['PZERO', 'EMPIRE', 'REBEL', 'WINS', 'LOSES', 'YOU', 'BROWN']:
    print(word, calc_checksum(word))
