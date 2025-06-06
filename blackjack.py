import random
import art

print(art.logo)

#function to check if blackjack is acquired after first round of cards is dealt
def is_blackjack(cpu_score, player1_score):
    if cpu_score == 21:
        print("BlackJack! CPU wins!")
        return True
    elif player1_score == 21:
        print("BlackJack! You win!")
        return True
    return False

def calculate_score(hand):
    total = sum(hand)
    while total > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        total = sum(hand)
    return total


#will check for a winner if blackjack is not won after first round
def is_Winner(cpu_score, player1_score):
    if cpu_score > 21:
        print("Bust! Player 1 wins!")
        return True
    elif player1_score > 21:
        print("Bust! Cpu wins!")
        return True
    elif cpu_score == 21:
        print("Cpu wins!")
        return True
    elif player1_score == 21:
        print("You win!")
        return True
    elif player1_score > cpu_score and player1_score <= 21:
        print("You win!")
        return True
    elif cpu_score > player1_score and cpu_score <= 21:
        print("You lose! Cpu wins!")
        return True
    elif cpu_score == 20 and player1_score == 20:
        print("Draw!")
        return True
    return False

game_start = input("Do you want to play BlackJack? Type 'y' for yes or 'n' for no: ").lower()
play_again = True

while play_again:
    game_over = False
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    while not game_over:
        if game_start == 'y':
            player1_cards = random.choices(cards,k=2)
            player1_score = sum(player1_cards)
            print("Your cards:",player1_cards, "current score:",player1_score)
            cpu_card = random.choices(cards,k=2)
            cpu_score = sum(cpu_card)
            print("Computer's first cards:", cpu_card, "current score:",cpu_score)
            player1_score = calculate_score(player1_cards)
            cpu_score = calculate_score(cpu_card)
        else:
            print("Thank you!")

        #Check for blackjack
        game_over = is_blackjack(cpu_score, player1_score)

        while player1_score < 21:
            next_round = input("Type 'y' for another card or 'n' to pass: ").lower()
            if next_round == 'y':
                next_card = random.choice(cards)
                player1_cards.append(next_card)
                player1_score = sum(player1_cards)
                print("Your cards:",player1_cards, "current score:",player1_score)
            else:
                break
        while cpu_score < 17:
            next_card = random.choice(cards)
            cpu_card.append(next_card)
            cpu_score = sum(cpu_card)
            print("CPU cards:", cpu_card, "current score:", cpu_score)
        player1_score = calculate_score(player1_cards)
        cpu_score = calculate_score(cpu_card)
        game_over = is_Winner(cpu_score, player1_score)

        restart = input("Would you like to play again? Type 'y' for yes and 'n' for no: ")
        if restart == 'y':
            play_again = True
        else:
            play_again = False
            print("Thanks for playing!")
