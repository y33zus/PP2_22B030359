def reverse_sentence(input_string):
    words = input_string.split()
    return ' '.join(reversed(words))
sentence=input()
print(reverse_sentence(sentence))