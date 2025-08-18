import random

def generate_random_text(strlen):
    letter_corpus = "abcdefghijklmnopqrstuvwxyz "

    output_text = ""
    for i in range(strlen):
        output_text += letter_corpus[random.randrange(27)]

    return output_text

def scorer(text, target):
    score = 0
    target_length = len(target)
    for i in range(target_length):
        if text[i] == target[i]:
            score += 1
    return score / target_length    
    
def main():
    best_text = None
    best_score = 0
    iteration = 0
    target = "methinks it is like a weasel"

    while True:
        text = generate_random_text(len(target))
        score = scorer(text, target)

        if score == 1:
            print(f"Completed! The generated text is '{text}'")
            return 0
        
        if score > best_score:
            best_score = score
            best_text = text

        if iteration % 10000 == 0:
            print(f"Iteration {iteration}: Best text - '{best_text}' with Score - {best_score:.2f}")

        iteration += 1

        
if __name__ == "__main__":
    main()