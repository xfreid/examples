import random

def display_menu():
    print("[Menu]")
    print("1. St. Petersburg Lottery")
    print("2. First to a Word")
    print("3. Exit")

def petersburg_lottery ():
    print("Instruction for St. Petersburg Lottery:")
    print("You will select any number greater than 0.")
    print("Up to the number of times you chose, we will randomly choose 0 or 1.")
    print("If a a1 is chosen befor ethe last drawing, then you loses")
    print("If a 1 does not appear at all, then you loses")
    print("You win if 1 is chosen for the first time exactly on the last drawing.")
    print()

    user_name = input("enter player's name: ")
    play_times = int(input("how many times: "))
    i = 0
    user_win = False
    while i < play_times:
        coin = random.randint(0,i)
        debug = "num: {} coin: {}".format(i, coin)
        print(debug)
        if coin == 1:
            # is this the last time
            if i == play_times - 1:
                user_win = True
            else:
                user_win = False
                break
        i = i + 1
    
    if user_win:
        print(user_name + " you win!")
    else:
        print("you lose, better luck next time")
    print()


def first_to_word():
    print("Instruction for First to a Word:")
    print("You will take turns choosing letters one at a time until a word is formed")
    print("After each letter is chosen you will have a chance to confirm whether or not a word has been formed")
    print("When a word is formed, the player who played the last letter win")
    print("One of you has been chosen at random to initiate the game")
    print()
    print("NOte: words must be longer than two characters!")
    print()

    # user_1 : 0
    # user_2 : 1
    user1_name = input("enter player1's name: ")
    user2_name = input("enter player2's name: ")

    is_word_formed = False
    word = ""
    winner = ""
    user_id = random.randint(0, 1)
    # str() converts an int to string
    print("player " + str(user_id))

    while is_word_formed == False:
        if user_id == 0:
            user1_input = input(user1_name + " enter a character: ")
            word = word + user1_input
            print("you currently have put together the letters: " + word)

            # check the word size
            if len(word) > 2:
                answer = input("is this word? (yes or no): ")
                answer.lower()
                if answer == "yes":
                    is_word_formed = True
                    winner = user1_name
                    break
            user_id = 1

        if user_id == 1:
            user2_input = input(user2_name + " enter a character: ")
            word = word + user2_input
            print("you currently have put together the letters: " + word)
        
            # check the word size
            if len(word) > 2:
                answer = input("is this word? (yes or no): ")
                answer.lower()
                if answer == "yes":
                    is_word_formed = True
                    winner = user2_name
                    break
            user_id = 0

    print("congratulatioins " + winner + " you win!")
    print()


def main():
    print("welcome to the game")

    still_playing = True
    while still_playing == True:
        display_menu()
        game_chosen = int(input("which game option do you choose: "))
        if game_chosen == 1:
            petersburg_lottery()
        elif game_chosen == 2:
            first_to_word()
        else:
            print("we will not exit the game")
            still_playing = False
    
    print ("thank you for playing")

main()

        