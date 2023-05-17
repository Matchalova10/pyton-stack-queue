def reverse_sentence(sentence):
    stack = []
    reversed_sentence=""

    for world in sentence.split():
        stack.append(world)

    while len(stack)>0:
        reversed_sentence+=stack.pop()+""

    return reverse_sentence.strip()

sentence = "SELAMAT PAGI, BAGAIMANA KABAR ANDA?"
print(reverse_sentence(sentence))