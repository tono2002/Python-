
secret_word = "giraffe"
guess = ""

guess_count = 0
guess_limit = 3

out_of_guesses = False

# The loop will be executed while the guess doesn't match 
#   the secret word and the user still has guesses
 
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lose!")
else:
    print("You win!")