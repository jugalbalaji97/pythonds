import random

def generate_random_text(mask, base_text):
    letter_corpus = "abcdefghijklmnopqrstuvwxyz "

    output_text = ""
    for i in range(len(mask)):
        if mask[i] == 0:
            output_text += letter_corpus[random.randrange(27)]
        else:
            output_text += base_text[i]

    return output_text

def scorer(text, target):
    score = 0
    mask = []
    target_length = len(target)
    for i in range(target_length):
        if text[i] == target[i]:
            score += 1
            mask.append(1)
        else:
            mask.append(0)
    return score / target_length, mask    
    
def main():
    best_text = None
    best_score = 0
    iteration = 0
    mask = [0]*28
    target = "methinks it is like a weasel"

    while True:
        text = generate_random_text(mask, best_text)
        score, mask = scorer(text, target)

        if score == 1:
            print(f"Completed at {iteration} iterations! The generated text is '{text}'")
            return 0
        
        if score > best_score:
            best_score = score
            best_text = text

        if iteration % 10 == 0:
            print(f"Iteration {iteration}: Best text - '{best_text}' with Score - {best_score:.2f}")

        iteration += 1

        
if __name__ == "__main__":
    main()