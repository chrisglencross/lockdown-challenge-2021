plain_text = """Badger learns from his visitors that Toad has crashed seven cars, has been in hospital three times, and has spent a fortune on fines. Though nothing can be done at the moment (it being winter), they resolve that when the time is right they will make a plan to protect Toad from himself; they are, after all, his friends, and are worried about his well being."""
hidden_message = [c for c in "death star plans in droid."]

i = 0


def to_hex(c: str):
    global i
    i += 1
    asc = ord(c)
    byte = format(asc, "07b")

    parity = 1
    if hidden_message and c.lower() == hidden_message[0].lower():
        print("*" + hidden_message.pop(0))
        parity = 0
        if not hidden_message:
            print("***", i)

    if sum([int(bit) for bit in byte]) % 2 != parity:
        asc += 128
    return format(asc, "02x").upper()


print(" ".join([to_hex(c) for c in plain_text]))
