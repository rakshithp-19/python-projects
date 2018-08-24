secret_word = "Giraffe"
guess = ""
guess_count = 0
guess_limit = 4
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
     if guess_count < guess_limit:
            guess = input("enter your guess: ")
            guess_count += 1
            if guess!="Whatsapp":
                print("Wrong answer")

     else:
        out_of_guesses = True

if out_of_guesses:
    print("out of guesses you lose")
else:
    print("you win")