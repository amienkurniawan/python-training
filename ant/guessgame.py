secret_keyword = "june"
guess = ""
guess_limit = 3
guess_count = 0
out_of_game = False

while guess != secret_keyword and not(out_of_game):
    if guess_count < guess_limit :
        guess = input("enter the guess keyword : ")
    else :
        out_of_game = True
    guess_count +=1

if out_of_game :
    print("you lose !")
else :
    print("you win!")
