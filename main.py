from itertools import product, repeat

def generate_all_codes():
    codes = []
    for i in range(10):
        for j in range(10):
            if j == i:
                continue
            for k in range(10):
                if k == i or k == j:
                    continue
                codes.append(f"{i}{j}{k}")
    return codes

def initial_guess():
    return "150"

def evaluate_guess(guess, secret):
    hits = sum(1 for g, s in zip(guess, secret) if g == s)
    blows = sum(min(guess.count(n), secret.count(n)) for n in set(guess)) - hits
    return hits, blows

def filter_codes(possible_codes, guess, hits, blows):
    return [code for code in possible_codes if evaluate_guess(guess, code) == (hits, blows)]

def next_guess(possible_codes):
    return possible_codes[0]

def hit_and_blow_solver(secret):
    possible_codes = generate_all_codes()
    guess = initial_guess()

    while True:
        hits, blows = evaluate_guess(guess, secret)
        if hits == 3:
            return guess
        possible_codes = filter_codes(possible_codes, guess, hits, blows)
        guess = next_guess(possible_codes)
        print(guess)

secret = "617"
print("Found secret:", hit_and_blow_solver(secret))
