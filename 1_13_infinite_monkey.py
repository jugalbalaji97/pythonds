from random import randint

def generate_random_text():
    letter_corpus = "abcdefghijklmnopqrstuvwxyz"

    output_text = ""
    for i in range(28):
        output_text += letter_corpus[randint(0,25)]

    return output_text

def score():
    target = "methinks it is like a weasel"

    

def main():
    print(generate_random_text())

if __name__ == "__main__":
    main()