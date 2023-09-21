import random


def roll():
    value = random.randint(1, 6)
    return value


while True:
    numberPlayers = input("Enter the number of Players 2 - 4 :")
    if numberPlayers.isdigit():
        numberPlayers = int(numberPlayers)
        if numberPlayers <= 4 and numberPlayers >= 2:
            break
        else:
            print("Number must be between 2-4 . Try again")
    else:
        print("Invalid Input")

max_score = int(input("Set a winning score :"))
player_scores = [0 for i in range(numberPlayers)]

while max(player_scores) < max_score:
    round = 1
    print(f"Round number {round}")
    round += 1
    for _ in range(numberPlayers):
        print(f"Player {_ + 1} current score is {player_scores[_]} ")
        while True:
            play = input("Enter (y) if you want to roll else (n) :")
            if play.lower() == "y":
                score = roll()
                if score == 1:
                    player_scores[_] = 0
                    print(
                        f"You Rolled a 1 . Turn Done! \n Your score is {player_scores[_]}")
                    break
                else:
                    print(f"You rolled {score}")
                    player_scores[_] += score
                    if player_scores[_] >= 50:
                        print(f"Your score is {player_scores[_]}")
                        print(f"Player {_ + 1} won!!")
                        break
                    print(f"Your score is {player_scores[_]}")
            elif play.lower() == "n":
                break
            else:
                print("Invalid Input. Try again")

            if player_scores[_] >= 50:
                break
        if player_scores[_] >= 50:
            break
