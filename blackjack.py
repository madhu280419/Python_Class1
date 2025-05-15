#write a program for blackjack game
import random
count = 0
#

def user_function(user1_li):
    input ("press enter to start the game; ")
    random_cards = random.choice(user1_li)
def blackjack():
    cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K','A']
    # diamonds = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'J', 'Q', 'K','A']
    # clubs = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'J', 'Q', 'K','A']
    # spades = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 'J', 'Q', 'K','A']

    

    user1_li = []
    user2_li = []


    user1_name = input ("Enter your name: ")
    input ("press enter to start the game; ")

    random_cards = random.choice(cards)
    print(random_cards)

    user1_li.append(random_cards)
    print(f"{user1_name}  {random_cards}")

    user2_name = input ("Enter your name: ")
    input ("press enter to start the game; ")

    random_cards = random.choice(cards)
    print(random_cards)


    user2_li.append(random_cards)
    print(f"{user2_name}  {random_cards}")
    
    sum((user1_li,cards))
    for i in list:
        if i == 'J' or i == 'K' or i == 'Q':
            i = 10
            count += 10
        elif i == 'A':
            i = 11
            count += 11
        else:
            i = int(i)
            count += i
            print(count)
    
    if sum(user1_li) <= 21 or sum(user2_li) <= 21:
        
        result = user1_function(user2_li)
 




# cursor.execute('''
#     INSERT INTO Basic_info (id, name, fees_paid, fees_due) VALUES (?, ?, ?, ?)''', (1, "Madhu", 5000, 10000))


# cursor.execute('''
#             INSERT INTO Basic_info (id, name, section, total_fees)
#             VALUES (?, ?, ?, ?)
#         ''', (4, "Madhu", "D", 10000))



#pseudo code for black jack
#1.create a listof cards and assign values to them.
#2.add a function to shuffle the cards.
#3 add users to start the game.
#4.add values to the specific cards.
#5.write a code to calculate the total value of cards.
#6.set range for the cards
#7.write function to check if user has won or loose.
