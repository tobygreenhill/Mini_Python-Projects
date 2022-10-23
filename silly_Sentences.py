from random import randint
def pick(words):
    num_words = len(words)
    num_Picked = randint(0, num_words - 1)
    words_picked = words[num_Picked]
    return words_picked

name = ["Neha", "lee", "Sam"]
verb = ["buys", "rides", "kicks"]
noun = ["lion", "bicycle", "plane"]

print(pick(name), pick(verb), "a", pick(noun), end=".\n")

while True:
    print(pick(name), pick(verb), "a", pick(noun), end=".")
    input()