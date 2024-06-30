import base64

# Store the sentence – 'The quick brown fox jumps over the lazy dog' – in base64 in a file and then read from, decode into utf-8 and print on screen.
a = "The quick brown fox jumps over the lazy dog"
encoded_sentence = base64.b64encode(a.encode("utf-8"))

with open("encoded_sentence.txt", "wb") as file:
    file.write(encoded_sentence)

with open("encoded_sentence.txt", "rb") as file:
    encoded_sentence = file.read()

decoded_sentence = base64.b64decode(encoded_sentence).decode("utf-8")

print(decoded_sentence)