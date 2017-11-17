import itertools #imports the tools used in the programming so that the program understands certain functions used
import random 
global hand
suits = ['x', 'x', 'x', 'x', 'x'] #list of the suits of cards
card_value = [0,0,0,0,0]#values of each card
deck = ['A Spades','2 Spades','3 Spades','4 Spades','5 Spades','6 Spades','7 Spades','8 Spades','9 Spades','T Spades','J Spades','Q Spades','K Spades','A Hearts','2 Hearts','3 Hearts','4 Hearts','5 Hearts','6 Hearts','7 Hearts','8 Hearts','9 Hearts','T Hearts','J Hearts','Q Hearts','K Hearts','A Clubs','2 Clubs','3 Clubs','4 Clubs','5 Clubs','6 Clubs','7 Clubs','8 Clubs','9 Clubs','T Clubs','J Clubs','Q Clubs','K Clubs','A Diamonds','2 Diamonds','3 Diamonds','4 Diamonds','5 Diamonds','6 Diamonds','7 Diamonds','8 Diamonds','9 Diamonds','T Diamonds','J Diamonds','Q Diamonds','K Diamonds',]
deck2 = deck #for security, I have created a second deck that will keep track of cards that have not been drawn
drawn_cards = random.sample(deck,5) #creates a 5 element list of randomly selected elements in the 'deck' list
deck2.remove(drawn_cards[0]) #removes the first drawn card from the deck so that it will not be drawn again
deck2.remove(drawn_cards[1]) #removes the second drawn card
deck2.remove(drawn_cards[2]) #removes the third drawn card
deck2.remove(drawn_cards[3]) #removes the fourth drawn card
deck2.remove(drawn_cards[4]) #removes the fifth drawn card
print 'You drew:'
print drawn_cards #Shows the list of cards you drew
choices = ['0','0','0','0','0'] #The default list of cards you would like to swap, all five of your choices
def swap(): #function checks if you would like to swap any cards, swaps the first.
    print "Would you like to swap any cards? (Type y for yes, Type n if you are happy with your cards)" # asks question and tells player what to do.
    swap1 = raw_input() #receives the input of the player
    if swap1 == "y": #if the player input a y for yes
        while 0==0: #will loop continuing to check for a swap
            print "Which card would you like to switch first? (Type a number 1 through 5 inclusive that corresponds to the card you want to the card you want to switch, 1 for far left, 5 for far right)" #tells player how to select a card to swap
            change1 = raw_input() #will take the players input
            if change1 == '1': #checks if the input was a 1
                drawn_cards[0] = random.choice(deck2) #replaces the first element in the list of drawn cards with a random card from the deck
                choices[0] = '1' #keeps track of the first card you chose in the list 'choices'
                deck2.remove(drawn_cards[0]) #removes the newly drawn card from the deck
            elif change1 == '2': #checks if the input was a 2
                drawn_cards[1] = random.choice(deck2)#replaces the second element in the list of drawn cards with a random card from the deck
                choices[0] = '2' #keeps track of the second card you chose in the list 'choices'
                deck2.remove(drawn_cards[1]) #removes the newly drawn card from the deck
            elif change1 == '3': #checks if the input was a 3
                drawn_cards[2] = random.choice(deck2)#replaces the third element in the list of drawn cards with a random card from the deck
                choices[0] = '3' #keeps track of the third card you chose in the list 'choices'
                deck2.remove(drawn_cards[2]) #removes the newly drawn card from the deck
            elif change1 == '4': #checks if the input was a 4
                drawn_cards[3] = random.choice(deck2)#replaces the fourth element in the list of drawn cards with a random card from the deck
                choices[0] = '4' #keeps track of the fourth card you chose in the list 'choices'
                deck2.remove(drawn_cards[3]) #removes the newly drawn card from the deck
            elif change1 == '5': #checks if the input was a 5
                drawn_cards[4] = random.choice(deck2)#replaces the fifth element in the list of drawn cards with a random card from the deck
                choices[0] = '5' #keeps track of the fifth card you chose in the list 'choices'
                deck2.remove(drawn_cards[4]) #removes the newly drawn card from the deck
            else: #if the player did not input a 1,2,3,4 or 5
                print "I didn't catch that." #the program says it didn't understand.
                continue #goes back to the while loop, asks to pick a card to swap again
            swap_2() #once the player selects a card to change it will move on to ask for a second swap
            return #stops the while loop so that it will stop checking for a number
    elif swap1 == "n": #If the player's input was a n for no, it will swap anycards and directly go to show the hand
        check_suit1()
    else: #If the player entered something other than y or n, it will ask them to re enter that
        print "I didn't catch that."
        swap()
def swap_2():#If the player has not already pressed n to stop swapping cards, they will be asked if they want to switch another.
    print "Would you like to swap a second card? (Type y for yes, Type n if you like the other 4 cards)"
    swap2 = raw_input()#player's input
    if swap2 == 'y':#if player pressed y
        while 0==0:#loops indefinitely
            print "What other card would you like to swap? (Type a different number 1 through 5 inclusive that corresponds to the card you want to the card you want to switch NOT THE SAME NUMBER)"
            change2 = raw_input()#another player's input
            if change2 == choices[0]:#if the player entered the same number for the first swap, tell them they can't do that. Ask them if they want to swap again
                print "You already changed that card."
                swap_2()
                return
            else:#if it is a new card, check which one
                if change2 == "1":#If they choose to swap 1
                    drawn_cards[0] = random.choice(deck2) #replaces the first element in the list of drawn cards with a random card from the deck
                    choices[1] = '1' #keeps track of the second card you chose in the list 'choices'
                    deck2.remove(drawn_cards[0]) #removes the newly drawn card from the deck
                elif change2 == "2":#If they choose to swap 2
                    drawn_cards[1] = random.choice(deck2) #replaces the second element in the list of drawn cards with a random card from the deck
                    choices[1] = '2' #keeps track of the second card you chose in the list 'choices'
                    deck2.remove(drawn_cards[1]) #removes the newly drawn card from the deck
                elif change2 == "3":#If they choose to swap 3
                    drawn_cards[2] = random.choice(deck2) #replaces the third element in the list of drawn cards with a random card from the deck
                    choices[1] = '3' #keeps track of the second card you chose in the list 'choices'
                    deck2.remove(drawn_cards[2]) #removes the newly drawn card from the deck
                elif change2 == "4":#If they choose to swap 4
                    drawn_cards[3] = random.choice(deck2) #replaces the fourth element in the list of drawn cards with a random card from the deck
                    choices[1] = '4' #keeps track of the second card you chose in the list 'choices'
                    deck2.remove(drawn_cards[3]) #removes the newly drawn card from the deck
                elif change2 == "5":#If they choose to swap 5
                    drawn_cards[4] = random.choice(deck2) #replaces the fifth element in the list of drawn cards with a random card from the deck
                    choices[1] = '5' #keeps track of the second card you chose in the list 'choices'
                    deck2.remove(drawn_cards[4]) #removes the newly drawn card from the deck
                else: #if they didn't put in a 1,2,3,4 or 5 it will recheck which card they wanted to swap
                    print "I didn't catch that."
                    continue
                swap_3()  #once a card has been chosen, check if they want to swap a third.
                return
    elif swap2 == 'n': #if they choose not to swap a second time, show them their hand.
        check_suit1()
    else: #If they did not enter a y or n, ask them to re enter
        print "I didn't catch that"
        swap_2()
def swap_3():#If the player has not already pressed n to stop swapping cards, they will be asked if they want to switch another.
    print "Would you like to swap a third card? (Type y for yes, Type n if you like the other 3 cards)"
    swap3 = raw_input()#player's input
    if swap3 == 'y':#if they choose y to swap a card
        while 0==0:#loops indefinitely
            print "What other card would you like to swap? (Type a different number 1 through 5 inclusive that corresponds to the card you want to the card you want to switch NOT THE SAME NUMBER)"
            change3 = raw_input()#another input of the player
            if change3 == choices[0] or change3 == choices[1]: #Checks if the player chose a card that they already swapped the first or second time
                print "You already changed that card."
                swap_3()
                return
            else:#if they picked a new card
                if change3 == "1":#checks if they want to swap card 1
                    drawn_cards[0] = random.choice(deck2) #replaces the first element in the list of drawn cards with a random card from the deck
                    choices[2] = '1' #keeps track of the third card you chose in the list 'choices'
                    deck2.remove(drawn_cards[0]) #removes the newly drawn card from the deck
                elif change3 == "2":#checks if they want to swap card 2
                    drawn_cards[1] = random.choice(deck2) #replaces the second element in the list of drawn cards with a random card from the deck
                    choices[2] = '2' #keeps track of the third card you chose in the list 'choices'
                    deck2.remove(drawn_cards[1]) #removes the newly drawn card from the deck
                elif change3 == "3":#checks if they want to swap card 3
                    drawn_cards[2] = random.choice(deck2) #replaces the third element in the list of drawn cards with a random card from the deck
                    choices[2] = '3' #keeps track of the third card you chose in the list 'choices'
                    deck2.remove(drawn_cards[2]) #removes the newly drawn card from the deck
                elif change3 == "4":#checks if they want to swap card 4
                    drawn_cards[3] = random.choice(deck2) #replaces the fourth element in the list of drawn cards with a random card from the deck
                    choices[2] = '4' #keeps track of the third card you chose in the list 'choices'
                    deck2.remove(drawn_cards[3]) #removes the newly drawn card from the deck
                elif change3 == "5":#checks if they want to swap card 5
                    drawn_cards[4] = random.choice(deck2) #replaces the fifth element in the list of drawn cards with a random card from the deck
                    choices[2] = '5' #keeps track of the third card you chose in the list 'choices'
                    deck2.remove(drawn_cards[4]) #removes the newly drawn card from the deck
                else:#if they enter something other than 1,2,3,4 or 5, ask them to try again.
                    print "I didn't catch that."
                    continue
                swap_4()#once they choose a number to swap, check if they swap a fourth card.
                return
    elif swap3 == 'n':#if they don't want to swap a third card, show hand
        check_suit1()
    else:#if they didn't enter y or n, ask them to re enter
        print "I didn't catch that"
        swap_3()
def swap_4():#If the player has not already pressed n to stop swapping cards, they will be asked if they want to switch another.
    print "Would you like to swap a fourth card? (Type y for yes, Type n if you like the other 2 cards)"
    swap4 = raw_input()#player's input
    if swap4 == 'y':#if they choose y to swap a card
        while 0==0:#loops indefinitely
            print "What other card would you like to swap? (Type a different number 1 through 5 inclusive that corresponds to the card you want to the card you want to switch NOT THE SAME NUMBER)"
            change4 = raw_input()#another input of the player
            if change4 == choices[0] or change4 == choices[1] or change4 == choices[2]: #Checks if the player chose a card that they already swapped the first, second, or third time
                print "You already changed that card."
                swap_4()
                return
            else:#if they picked a new card
                if change4 == "1":#checks if they want to swap card 1
                    drawn_cards[0] = random.choice(deck2) #replaces the first element in the list of drawn cards with a random card from the deck
                    choices[3] = '1' #keeps track of the fourth card you chose in the list 'choices'
                    deck2.remove(drawn_cards[0]) #removes the newly drawn card from the deck
                elif change4 == "2":#checks if they want to swap card 2
                    drawn_cards[1] = random.choice(deck2) #replaces the second element in the list of drawn cards with a random card from the deck
                    choices[3] = '2' #keeps track of the fourth card you chose in the list 'choices'
                    deck2.remove(drawn_cards[1]) #removes the newly drawn card from the deck
                elif change4 == "3":#checks if they want to swap card 3
                    drawn_cards[2] = random.choice(deck2) #replaces the third element in the list of drawn cards with a random card from the deck
                    choices[3] = '3' #keeps track of the fourth card you chose in the list 'choices'
                    deck2.remove(drawn_cards[2]) #removes the newly drawn card from the deck
                elif change4 == "4":#checks if they want to swap card 4
                    drawn_cards[3] = random.choice(deck2) #replaces the fourth element in the list of drawn cards with a random card from the deck
                    choices[3] = '4' #keeps track of the fourth card you chose in the list 'choices'
                    deck2.remove(drawn_cards[3]) #removes the newly drawn card from the deck
                elif change4 == "5":#checks if they want to swap card 5
                    drawn_cards[4] = random.choice(deck2) #replaces the fifth element in the list of drawn cards with a random card from the deck
                    choices[3] = '5' #keeps track of the fourth card you chose in the list 'choices'
                    deck2.remove(drawn_cards[4]) #removes the newly drawn card from the deck
                else:#if they enter something other than 1,2,3,4 or 5, ask them to try again.
                    print "I didn't catch that."
                    continue
                swap_5()#once they choose a number to swap, check if they swap a fifth card.
                return
    elif swap4 == 'n':#if they don't want to swap a fourth card, show hand
        check_suit1()
    else:#if they didn't enter y or n, ask them to re enter
        print "I didn't catch that"
        swap_4()
def swap_5():#If the player has not already pressed n to stop swapping cards, they will be asked if they want to switch the last one.
    print "Would you like to swap the last card? (Type y for yes, Type n if you like the last card)"
    swap5 = raw_input()#player's input
    if swap5 == 'y':#if they choose y to swap a card
        if '1' not in choices:#if they swapped every card except for number 1, swap number 1
            drawn_cards[0] = random.choice(deck2) #replaces the first element in the list of drawn cards with a random card from the deck
            choices[4] = '1' #keeps track of the fifth card you chose in the list 'choices'
            deck2.remove(drawn_cards[0]) #removes the newly drawn card from the deck
        elif '2' not in choices:#if they swapped every card except for number 2, swap number 2
            drawn_cards[1] = random.choice(deck2) #replaces the second element in the list of drawn cards with a random card from the deck
            choices[4] = '2' #keeps track of the fifth card you chose in the list 'choices'
            deck2.remove(drawn_cards[1]) #removes the newly drawn card from the deck
        elif '3' not in choices:#if they swapped every card except for number 3, swap number 3
            drawn_cards[2] = random.choice(deck2) #replaces the third element in the list of drawn cards with a random card from the deck
            choices[4] = '3' #keeps track of the fifth card you chose in the list 'choices'
            deck2.remove(drawn_cards[2]) #removes the newly drawn card from the deck
        elif '4' not in choices:#if they swapped every card except for number 4, swap number 4
            drawn_cards[3] = random.choice(deck2) #replaces the fourth element in the list of drawn cards with a random card from the deck
            choices[4] = '4' #keeps track of the fifth card you chose in the list 'choices'
            deck2.remove(drawn_cards[3]) #removes the newly drawn card from the deck
        elif '5' not in choices:#if they swapped every card except for number 5, swap number 5
            drawn_cards[4] = random.choice(deck2) #replaces the fifth element in the list of drawn cards with a random card from the deck
            choices[4] = '5' #keeps track of the fifth card you chose in the list 'choices'
            deck2.remove(drawn_cards[4]) #removes the newly drawn card from the deck
        check_suit1()
    elif swap5 == 'n':#if they don't want to swap a fifth card, show hand
        check_suit1()
    else:#if they didn't enter y or n, ask them to re enter
        print "I didn't catch that"
        swap_5()
def check_suit1():
    if 'Spades' in drawn_cards[0]:
        suits[0] = 'Spades'
    elif 'Diamonds' in drawn_cards[0]:
        suits[0] = 'Diamonds'
    elif 'Hearts' in drawn_cards[0]:
        suits[0] = 'Hearts'
    elif 'Clubs' in drawn_cards[0]:
        suits[0] = 'Clubs'
    check_suit2()
def check_suit2():
    if 'Spades' in drawn_cards[1]:
        suits[1] = 'Spades'
    elif 'Diamonds' in drawn_cards[1]:
        suits[1] = 'Diamonds'
    elif 'Hearts' in drawn_cards[1]:
        suits[1] = 'Hearts'
    elif 'Clubs' in drawn_cards[1]:
        suits[1] = 'Clubs'
    check_suit3()
def check_suit3():
    if 'Spades' in drawn_cards[2]:
        suits[2] = 'Spades'
    elif 'Diamonds' in drawn_cards[2]:
        suits[2] = 'Diamonds'
    elif 'Hearts' in drawn_cards[2]:
        suits[2] = 'Hearts'
    elif 'Clubs' in drawn_cards[2]:
        suits[2] = 'Clubs'
    check_suit4()
def check_suit4():
    if 'Spades' in drawn_cards[3]:
        suits[3] = 'Spades'
    elif 'Diamonds' in drawn_cards[3]:
        suits[3] = 'Diamonds'
    elif 'Hearts' in drawn_cards[3]:
        suits[3] = 'Hearts'
    elif 'Clubs' in drawn_cards[3]:
        suits[3] = 'Clubs'
    check_suit5()
def check_suit5():
    if 'Spades' in drawn_cards[4]:
        suits[4] = 'Spades'
    elif 'Diamonds' in drawn_cards[4]:
        suits[4] = 'Diamonds'
    elif 'Hearts' in drawn_cards[4]:
        suits[4] = 'Hearts'
    elif 'Clubs' in drawn_cards[4]:
        suits[4] = 'Clubs'
    check_HC()
def check_HC():
    global hc
    if 'A' in drawn_cards[0] or 'A' in drawn_cards[1] or 'A' in drawn_cards[2] or 'A' in drawn_cards[3] or 'A' in drawn_cards[4]:
        hc = 'Ace'
    elif 'K' in drawn_cards[0] or 'K' in drawn_cards[1] or 'K' in drawn_cards[2] or 'K' in drawn_cards[3] or 'K' in drawn_cards[4]:
        hc = 'King'
    elif 'Q' in drawn_cards[0] or 'Q' in drawn_cards[1] or 'Q' in drawn_cards[2] or 'Q' in drawn_cards[3] or 'Q' in drawn_cards[4]:
        hc = 'Queen'
    elif 'J' in drawn_cards[0] or 'J' in drawn_cards[1] or 'J' in drawn_cards[2] or 'J' in drawn_cards[3] or 'J' in drawn_cards[4]:
        hc = 'Jack'
    elif 'T' in drawn_cards[0] or 'T' in drawn_cards[1] or 'T' in drawn_cards[2] or 'T' in drawn_cards[3] or 'T' in drawn_cards[4]:
        hc = 'Ten'
    elif '9' in drawn_cards[0] or '9' in drawn_cards[1] or '9' in drawn_cards[2] or '9' in drawn_cards[3] or '9' in drawn_cards[4]:
        hc = 'Nine'
    elif '8' in drawn_cards[0] or '8' in drawn_cards[1] or '8' in drawn_cards[2] or '8' in drawn_cards[3] or '8' in drawn_cards[4]:
        hc = 'Eight'
    elif '7' in drawn_cards[0] or '7' in drawn_cards[1] or '7' in drawn_cards[2] or '7' in drawn_cards[3] or '7' in drawn_cards[4]:
        hc = 'Seven'
    elif '6' in drawn_cards[0] or '6' in drawn_cards[1] or '6' in drawn_cards[2] or '6' in drawn_cards[3] or '6' in drawn_cards[4]:
        hc = 'Six'
    elif '5' in drawn_cards[0] or '5' in drawn_cards[1] or '5' in drawn_cards[2] or '5' in drawn_cards[3] or '5' in drawn_cards[4]:
        hc = 'Five'
    elif '4' in drawn_cards[0] or '4' in drawn_cards[1] or '4' in drawn_cards[2] or '4' in drawn_cards[3] or '4' in drawn_cards[4]:
        hc = 'Four'
    elif '3' in drawn_cards[0] or '3' in drawn_cards[1] or '3' in drawn_cards[2] or '3' in drawn_cards[3] or '3' in drawn_cards[4]:
        hc = 'Three'
    else:
        hc = 'Two'
    check_card_value1()
def check_card_value1():
    if 'A' in drawn_cards[0]:
        card_value[0] = 14
    elif 'K' in drawn_cards[0]:
        card_value[0] = 13
    elif 'Q' in drawn_cards[0]:
        card_value[0] = 12
    elif 'J' in drawn_cards[0]:
        card_value[0] = 11
    elif 'T' in drawn_cards[0]:
        card_value[0] = 10
    elif '9' in drawn_cards[0]:
        card_value[0] = 9
    elif '8' in drawn_cards[0]:
        card_value[0] = 8
    elif '7' in drawn_cards[0]:
        card_value[0] = 7
    elif '6' in drawn_cards[0]:
        card_value[0] = 6
    elif '5' in drawn_cards[0]:
        card_value[0] = 5
    elif '4' in drawn_cards[0]:
        card_value[0] = 4
    elif '3' in drawn_cards[0]:
        card_value[0] = 3
    elif '2' in drawn_cards[0]:
        card_value[0] = 2
    check_card_value2()
def check_card_value2():
    if 'A' in drawn_cards[1]:
        card_value[1] = 14
    elif 'K' in drawn_cards[1]:
        card_value[1] = 13
    elif 'Q' in drawn_cards[1]:
        card_value[1] = 12
    elif 'J' in drawn_cards[1]:
        card_value[1] = 11
    elif 'T' in drawn_cards[1]:
        card_value[1] = 10
    elif '9' in drawn_cards[1]:
        card_value[1] = 9
    elif '8' in drawn_cards[1]:
        card_value[1] = 8
    elif '7' in drawn_cards[1]:
        card_value[1] = 7
    elif '6' in drawn_cards[1]:
        card_value[1] = 6
    elif '5' in drawn_cards[1]:
        card_value[1] = 5
    elif '4' in drawn_cards[1]:
        card_value[1] = 4
    elif '3' in drawn_cards[1]:
        card_value[1] = 3
    elif '2' in drawn_cards[1]:
        card_value[1] = 2
    check_card_value3()
def check_card_value3():
    if 'A' in drawn_cards[2]:
        card_value[2] = 14
    elif 'K' in drawn_cards[2]:
        card_value[2] = 13
    elif 'Q' in drawn_cards[2]:
        card_value[2] = 12
    elif 'J' in drawn_cards[2]:
        card_value[2] = 11
    elif 'T' in drawn_cards[2]:
        card_value[2] = 10
    elif '9' in drawn_cards[2]:
        card_value[2] = 9
    elif '8' in drawn_cards[2]:
        card_value[2] = 8
    elif '7' in drawn_cards[2]:
        card_value[2] = 7
    elif '6' in drawn_cards[2]:
        card_value[2] = 6
    elif '5' in drawn_cards[2]:
        card_value[2] = 5
    elif '4' in drawn_cards[2]:
        card_value[2] = 4
    elif '3' in drawn_cards[2]:
        card_value[2] = 3
    elif '2' in drawn_cards[2]:
        card_value[2] = 2
    check_card_value4()
def check_card_value4():
    if 'A' in drawn_cards[3]:
        card_value[3] = 14
    elif 'K' in drawn_cards[3]:
        card_value[3] = 13
    elif 'Q' in drawn_cards[3]:
        card_value[3] = 12
    elif 'J' in drawn_cards[3]:
        card_value[3] = 11
    elif 'T' in drawn_cards[3]:
        card_value[3] = 10
    elif '9' in drawn_cards[3]:
        card_value[3] = 9
    elif '8' in drawn_cards[3]:
        card_value[3] = 8
    elif '7' in drawn_cards[3]:
        card_value[3] = 7
    elif '6' in drawn_cards[3]:
        card_value[3] = 6
    elif '5' in drawn_cards[3]:
        card_value[3] = 5
    elif '4' in drawn_cards[3]:
        card_value[3] = 4
    elif '3' in drawn_cards[3]:
        card_value[3] = 3
    elif '2' in drawn_cards[3]:
        card_value[3] = 2
    check_card_value5()
def check_card_value5():
    if 'A' in drawn_cards[4]:
        card_value[4] = 14
    elif 'K' in drawn_cards[4]:
        card_value[4] = 13
    elif 'Q' in drawn_cards[4]:
        card_value[4] = 12
    elif 'J' in drawn_cards[4]:
        card_value[4] = 11
    elif 'T' in drawn_cards[4]:
        card_value[4] = 10
    elif '9' in drawn_cards[4]:
        card_value[4] = 9
    elif '8' in drawn_cards[4]:
        card_value[4] = 8
    elif '7' in drawn_cards[4]:
        card_value[4] = 7
    elif '6' in drawn_cards[4]:
        card_value[4] = 6
    elif '5' in drawn_cards[4]:
        card_value[4] = 5
    elif '4' in drawn_cards[4]:
        card_value[4] = 4
    elif '3' in drawn_cards[4]:
        card_value[4] = 3
    elif '2' in drawn_cards[4]:
        card_value[4] = 2
    check_RF()
def check_RF():
    global hand
    if suits[0] == suits[1] and suits[0] == suits[2] and suits[0] == suits[3] and suits[0] == suits[4]:
        if hc == 'Ace':
            if card_value[0] == 13 or card_value[1] == 13 or card_value[2] == 13 or card_value[3] == 13 or card_value[4] == 13:
                if card_value[0] == 12 or card_value[1] == 12 or card_value[2] == 12 or card_value[3] == 12 or card_value[4] == 12:
                    if card_value[0] == 11 or card_value[1] == 11 or card_value[2] == 11 or card_value[3] == 11 or card_value[4] == 11:
                        if card_value[0] == 10 or card_value[1] == 10 or card_value[2] == 10 or card_value[3] == 10 or card_value[4] == 10:
                            hand = 'Royal Flush in ' + suits[0]
                            show_hand()
                        else:
                            hand = 'Flush in ' + suits[0]
                            show_hand()
                    else:
                        hand = 'Flush in ' + suits[0]
                        show_hand()
                else:
                    hand = 'Flush in ' + suits[0]
                    show_hand()
            else:
                check_SF()
        else:
            check_SF()
    else:
        check_FOAK()
def check_SF():
    global hand
    if hc == 'King':
        if card_value[0] == 12 or card_value[1] == 12 or card_value[2] == 12 or card_value[3] == 12 or card_value[4] == 12:
            if card_value[0] == 11 or card_value[1] == 11 or card_value[2] == 11 or card_value[3] == 11 or card_value[4] == 11:
                if card_value[0] == 10 or card_value[1] == 10 or card_value[2] == 10 or card_value[3] == 10 or card_value[4] == 10:
                    if card_value[0] == 9 or card_value[1] == 9 or card_value[2] == 9 or card_value[3] == 9 or card_value[4] == 9:
                        hand = 'Straight Flush in ' + suits[0]
                        show_hand()
                    else:
                        hand = 'Flush in ' + suits[0]
                        show_hand()
                else:
                    hand = 'Flush in ' + suits[0]
                    show_hand()
            else:
                hand = 'Flush in ' + suits[0]
                show_hand()
        else:
            hand = 'Flush in ' + suits[0]
            show_hand()
    elif hc == 'Queen':
        if card_value[0] == 11 or card_value[1] == 11 or card_value[2] == 11 or card_value[3] == 11 or card_value[4] == 11:
            if card_value[0] == 10 or card_value[1] == 10 or card_value[2] == 10 or card_value[3] == 10 or card_value[4] == 10:
                if card_value[0] == 9 or card_value[1] == 9 or card_value[2] == 9 or card_value[3] == 9 or card_value[4] == 9:
                    if card_value[0] == 8 or card_value[1] == 8 or card_value[2] == 8 or card_value[3] == 8 or card_value[4] == 8:
                        hand = 'Straight Flush in ' + suits[0]
                        show_hand()
                    else:
                        hand = 'Flush in ' + suits[0]
                        show_hand()
                else:
                    hand = 'Flush in ' + suits[0]
                    show_hand()
            else:
                hand = 'Flush in ' + suits[0]
                show_hand()
        else:
            hand = 'Flush in ' + suits[0]
            show_hand()
    elif hc == 'Jack':
        if card_value[0] == 10 or card_value[1] == 10 or card_value[2] == 10 or card_value[3] == 10 or card_value[4] == 10:
            if card_value[0] == 9 or card_value[1] == 9 or card_value[2] == 9 or card_value[3] == 9 or card_value[4] == 9:
                if card_value[0] == 8 or card_value[1] == 8 or card_value[2] == 8 or card_value[3] == 8 or card_value[4] == 8:
                    if card_value[0] == 7 or card_value[1] == 7 or card_value[2] == 7 or card_value[3] == 7 or card_value[4] == 7:
                        hand = 'Straight Flush in ' + suits[0]
                        show_hand()
                    else:
                        hand = 'Flush in ' + suits[0]
                        show_hand()
                else:
                    hand = 'Flush in ' + suits[0]
                    show_hand()
            else:
                hand = 'Flush in ' + suits[0]
                show_hand()
        else:
            hand = 'Flush in ' + suits[0]
            show_hand()
    elif hc == 'Ten':
        if card_value[0] == 9 or card_value[1] == 9 or card_value[2] == 9 or card_value[3] == 9 or card_value[4] == 9:
            if card_value[0] == 8 or card_value[1] == 8 or card_value[2] == 8 or card_value[3] == 8 or card_value[4] == 8:
                if card_value[0] == 7 or card_value[1] == 7 or card_value[2] == 7 or card_value[3] == 7 or card_value[4] == 7:
                    if card_value[0] == 6 or card_value[1] == 6 or card_value[2] == 6 or card_value[3] == 6 or card_value[4] == 6:
                        hand = 'Straight Flush in ' + suits[0]
                        show_hand()
                    else:
                        hand = 'Flush in ' + suits[0]
                        show_hand()
                else:
                    hand = 'Flush in ' + suits[0]
                    show_hand()
            else:
                hand = 'Flush in ' + suits[0]
                show_hand()
        else:
            hand = 'Flush in ' + suits[0]
            show_hand()
    elif hc == 'Nine':
        if card_value[0] == 8 or card_value[1] == 8 or card_value[2] == 8 or card_value[3] == 8 or card_value[4] == 8:
            if card_value[0] == 7 or card_value[1] == 7 or card_value[2] == 7 or card_value[3] == 7 or card_value[4] == 7:
                if card_value[0] == 6 or card_value[1] == 6 or card_value[2] == 6 or card_value[3] == 6 or card_value[4] == 6:
                    if card_value[0] == 5 or card_value[1] == 5 or card_value[2] == 5 or card_value[3] == 5 or card_value[4] == 5:
                        hand = 'Straight Flush in ' + suits[0]
                        show_hand()
                    else:
                        hand = 'Flush in ' + suits[0]
                        show_hand()
                else:
                    hand = 'Flush in ' + suits[0]
                    show_hand()
            else:
                hand = 'Flush in ' + suits[0]
                show_hand()
        else:
            hand = 'Flush in ' + suits[0]
            show_hand()
    elif hc == 'Eight':
        if card_value[0] == 7 or card_value[1] == 7 or card_value[2] == 7 or card_value[3] == 7 or card_value[4] == 7:
            if card_value[0] == 6 or card_value[1] == 6 or card_value[2] == 6 or card_value[3] == 6 or card_value[4] == 6:
                if card_value[0] == 5 or card_value[1] == 5 or card_value[2] == 5 or card_value[3] == 5 or card_value[4] == 5:
                    if card_value[0] == 4 or card_value[1] == 4 or card_value[2] == 4 or card_value[3] == 4 or card_value[4] == 4:
                        hand = 'Straight Flush in ' + suits[0]
                        show_hand()
                    else:
                        hand = 'Flush in ' + suits[0]
                        show_hand()
                else:
                    hand = 'Flush in ' + suits[0]
                    show_hand()
            else:
                hand = 'Flush in ' + suits[0]
                show_hand()
        else:
            hand = 'Flush in ' + suits[0]
            show_hand()
    elif hc == 'Seven':
        if card_value[0] == 6 or card_value[1] == 6 or card_value[2] == 6 or card_value[3] == 6 or card_value[4] == 6:
            if card_value[0] == 5 or card_value[1] == 5 or card_value[2] == 5 or card_value[3] == 5 or card_value[4] == 5:
                if card_value[0] == 4 or card_value[1] == 4 or card_value[2] == 4 or card_value[3] == 4 or card_value[4] == 4:
                    if card_value[0] == 3 or card_value[1] == 3 or card_value[2] == 3 or card_value[3] == 3 or card_value[4] == 3:
                        hand = 'Straight Flush in ' + suits[0]
                        show_hand()
                    else:
                        hand = 'Flush in ' + suits[0]
                        show_hand()
                else:
                    hand = 'Flush in ' + suits[0]
                    show_hand()
            else:
                hand = 'Flush in ' + suits[0]
                show_hand()
        else:
            hand = 'Flush in ' + suits[0]
            show_hand()
    elif hc == 'Six':
        if card_value[0] == 5 or card_value[1] == 5 or card_value[2] == 5 or card_value[3] == 5 or card_value[4] == 5:
            if card_value[0] == 4 or card_value[1] == 4 or card_value[2] == 4 or card_value[3] == 4 or card_value[4] == 4:
                if card_value[0] == 3 or card_value[1] == 3 or card_value[2] == 3 or card_value[3] == 3 or card_value[4] == 3:
                    if card_value[0] == 2 or card_value[1] == 2 or card_value[2] == 2 or card_value[3] == 2 or card_value[4] == 2:
                        hand = 'Straight Flush in ' + suits[0]
                        show_hand()
                    else:
                        hand = 'Flush in ' + suits[0]
                        show_hand()
                else:
                    hand = 'Flush in ' + suits[0]
                    show_hand()
            else:
                hand = 'Flush in ' + suits[0]
                show_hand()
        else:
            hand = 'Flush in ' + suits[0]
            show_hand()
    elif hc == 'Ace':
        if card_value[0] == 5 or card_value[1] == 5 or card_value[2] == 5 or card_value[3] == 5 or card_value[4] == 5:
            if card_value[0] == 4 or card_value[1] == 4 or card_value[2] == 4 or card_value[3] == 4 or card_value[4] == 4:
                if card_value[0] == 3 or card_value[1] == 3 or card_value[2] == 3 or card_value[3] == 3 or card_value[4] == 3:
                    if card_value[0] == 2 or card_value[1] == 2 or card_value[2] == 2 or card_value[3] == 2 or card_value[4] == 2:
                        hand = 'Straight Flush in ' + suits[0]
                        show_hand()
                    else:
                        hand = 'Flush in ' + suits[0]
                        show_hand()
                else:
                    hand = 'Flush in ' + suits[0]
                    show_hand()
            else:
                hand = 'Flush in ' + suits[0]
                show_hand()
        else:
            hand = 'Flush in ' + suits[0]
            show_hand()
    else:
        hand = 'Flush in ' + suits[0]
        show_hand()
def check_FOAK():
    global hand
    global pair_card
    if card_value[0] == card_value[1] and card_value[0] == card_value[2] and card_value[0] == card_value[3]:
        if card_value[0] == 14:
            pair_card = 'Aces'
        elif card_value[0] == 13:
            pair_card = 'Kings'
        elif card_value[0] == 12:
            pair_card = 'Queens'
        elif card_value[0] == 11:
            pair_card = 'Jacks'
        elif card_value[0] == 10:
            pair_card = 'Tens'
        elif card_value[0] == 9:
            pair_card = 'Nines'
        elif card_value[0] == 8:
            pair_card = 'Eights'
        elif card_value[0] == 7:
            pair_card = 'Sevens'
        elif card_value[0] == 6:
            pair_card = 'Sixes'
        elif card_value[0] == 5:
            pair_card = 'Fives'
        elif card_value[0] == 4:
            pair_card = 'Fours'
        elif card_value[0] == 3:
            pair_card = 'Threes'
        elif card_value[0] == 2:
            pair_card = 'Twos'
        hand = 'Four of a Kind: ' + pair_card
    elif card_value[0] == card_value[1] and card_value[0] == card_value[2] and card_value[0] == card_value[4]:
        if card_value[0] == 14:
            pair_card = 'Aces'
        elif card_value[0] == 13:
            pair_card = 'Kings'
        elif card_value[0] == 12:
            pair_card = 'Queens'
        elif card_value[0] == 11:
            pair_card = 'Jacks'
        elif card_value[0] == 10:
            pair_card = 'Tens'
        elif card_value[0] == 9:
            pair_card = 'Nines'
        elif card_value[0] == 8:
            pair_card = 'Eights'
        elif card_value[0] == 7:
            pair_card = 'Sevens'
        elif card_value[0] == 6:
            pair_card = 'Sixes'
        elif card_value[0] == 5:
            pair_card = 'Fives'
        elif card_value[0] == 4:
            pair_card = 'Fours'
        elif card_value[0] == 3:
            pair_card = 'Threes'
        elif card_value[0] == 2:
            pair_card = 'Twos'
        hand = 'Four of a Kind: ' + pair_card
    elif card_value[0] == card_value[1] and card_value[0] == card_value[3] and card_value[0] == card_value[4]:
        if card_value[0] == 14:
            pair_card = 'Aces'
        elif card_value[0] == 13:
            pair_card = 'Kings'
        elif card_value[0] == 12:
            pair_card = 'Queens'
        elif card_value[0] == 11:
            pair_card = 'Jacks'
        elif card_value[0] == 10:
            pair_card = 'Tens'
        elif card_value[0] == 9:
            pair_card = 'Nines'
        elif card_value[0] == 8:
            pair_card = 'Eights'
        elif card_value[0] == 7:
            pair_card = 'Sevens'
        elif card_value[0] == 6:
            pair_card = 'Sixes'
        elif card_value[0] == 5:
            pair_card = 'Fives'
        elif card_value[0] == 4:
            pair_card = 'Fours'
        elif card_value[0] == 3:
            pair_card = 'Threes'
        elif card_value[0] == 2:
            pair_card = 'Twos'
        hand = 'Four of a Kind: ' + pair_card
    elif card_value[0] == card_value[2] and card_value[0] == card_value[3] and card_value[0] == card_value[4]:
        if card_value[0] == 14:
            pair_card = 'Aces'
        elif card_value[0] == 13:
            pair_card = 'Kings'
        elif card_value[0] == 12:
            pair_card = 'Queens'
        elif card_value[0] == 11:
            pair_card = 'Jacks'
        elif card_value[0] == 10:
            pair_card = 'Tens'
        elif card_value[0] == 9:
            pair_card = 'Nines'
        elif card_value[0] == 8:
            pair_card = 'Eights'
        elif card_value[0] == 7:
            pair_card = 'Sevens'
        elif card_value[0] == 6:
            pair_card = 'Sixes'
        elif card_value[0] == 5:
            pair_card = 'Fives'
        elif card_value[0] == 4:
            pair_card = 'Fours'
        elif card_value[0] == 3:
            pair_card = 'Threes'
        elif card_value[0] == 2:
            pair_card = 'Twos'
        hand = 'Four of a Kind: ' + pair_card
    elif card_value[1] == card_value[2] and card_value[0] == card_value[3] and card_value[0] == card_value[4]:
        if card_value[1] == 14:
            pair_card = 'Aces'
        elif card_value[1] == 13:
            pair_card = 'Kings'
        elif card_value[1] == 12:
            pair_card = 'Queens'
        elif card_value[1] == 11:
            pair_card = 'Jacks'
        elif card_value[1] == 10:
            pair_card = 'Tens'
        elif card_value[1] == 9:
            pair_card = 'Nines'
        elif card_value[1] == 8:
            pair_card = 'Eights'
        elif card_value[1] == 7:
            pair_card = 'Sevens'
        elif card_value[1] == 6:
            pair_card = 'Sixes'
        elif card_value[1] == 5:
            pair_card = 'Fives'
        elif card_value[1] == 4:
            pair_card = 'Fours'
        elif card_value[1] == 3:
            pair_card = 'Threes'
        elif card_value[1] == 2:
            pair_card = 'Twos'
        hand = 'Four of a Kind: ' + pair_card
    else:
        check_FH()
    show_hand()
def check_FH():
    global hand
    global pair_card
    global TOAK_card
    if card_value[0] == card_value[1] and card_value[0] == card_value[2]:
        if card_value[0] == 14:
            TOAK_card = 'Aces'
        elif card_value[0] == 13:
            TOAK_card = 'Kings'
        elif card_value[0] == 12:
            TOAK_card = 'Queens'
        elif card_value[0] == 11:
            TOAK_card = 'Jacks'
        elif card_value[0] == 10:
            TOAK_card = 'Tens'
        elif card_value[0] == 9:
            TOAK_card = 'Nines'
        elif card_value[0] == 8:
            TOAK_card = 'Eights'
        elif card_value[0] == 7:
            TOAK_card = 'Sevens'
        elif card_value[0] == 6:
            TOAK_card = 'Sixes'
        elif card_value[0] == 5:
            TOAK_card = 'Fives'
        elif card_value[0] == 4:
            TOAK_card = 'Fours'
        elif card_value[0] == 3:
            TOAK_card = 'Threes'
        elif card_value[0] == 2:
            TOAK_card = 'Twos'
        if card_value[3] == card_value[4]:
            if card_value[3] == 14:
                pair_card = 'Aces'
            elif card_value[3] == 13:
                pair_card = 'Kings'
            elif card_value[3] == 12:
                pair_card = 'Queens'
            elif card_value[3] == 11:
                pair_card = 'Jacks'
            elif card_value[3] == 10:
                pair_card = 'Tens'
            elif card_value[3] == 9:
                pair_card = 'Nines'
            elif card_value[3] == 8:
                pair_card = 'Eights'
            elif card_value[3] == 7:
                pair_card = 'Sevens'
            elif card_value[3] == 6:
                pair_card = 'Sixes'
            elif card_value[3] == 5:
                pair_card = 'Fives'
            elif card_value[3] == 4:
                pair_card = 'Fours'
            elif card_value[3] == 3:
                pair_card = 'Threes'
            elif card_value[3] == 2:
                pair_card = 'Twos'
            hand = 'Full House: ' + TOAK_card + ' over ' + pair_card
        else:
            hand = 'Three of a Kind: ' + TOAK_card
        show_hand()
    elif card_value[0] == card_value[1] and card_value[0] == card_value[3]:
        if card_value[0] == 14:
            TOAK_card = 'Aces'
        elif card_value[0] == 13:
            TOAK_card = 'Kings'
        elif card_value[0] == 12:
            TOAK_card = 'Queens'
        elif card_value[0] == 11:
            TOAK_card = 'Jacks'
        elif card_value[0] == 10:
            TOAK_card = 'Tens'
        elif card_value[0] == 9:
            TOAK_card = 'Nines'
        elif card_value[0] == 8:
            TOAK_card = 'Eights'
        elif card_value[0] == 7:
            TOAK_card = 'Sevens'
        elif card_value[0] == 6:
            TOAK_card = 'Sixes'
        elif card_value[0] == 5:
            TOAK_card = 'Fives'
        elif card_value[0] == 4:
            TOAK_card = 'Fours'
        elif card_value[0] == 3:
            TOAK_card = 'Threes'
        elif card_value[0] == 2:
            TOAK_card = 'Twos'
        if card_value[2] == card_value[4]:
            if card_value[2] == 14:
                pair_card = 'Aces'
            elif card_value[2] == 13:
                pair_card = 'Kings'
            elif card_value[2] == 12:
                pair_card = 'Queens'
            elif card_value[2] == 11:
                pair_card = 'Jacks'
            elif card_value[2] == 10:
                pair_card = 'Tens'
            elif card_value[2] == 9:
                pair_card = 'Nines'
            elif card_value[2] == 8:
                pair_card = 'Eights'
            elif card_value[2] == 7:
                pair_card = 'Sevens'
            elif card_value[2] == 6:
                pair_card = 'Sixes'
            elif card_value[2] == 5:
                pair_card = 'Fives'
            elif card_value[2] == 4:
                pair_card = 'Fours'
            elif card_value[2] == 3:
                pair_card = 'Threes'
            elif card_value[2] == 2:
                pair_card = 'Twos'
            hand = 'Full House: ' + TOAK_card + ' over ' + pair_card
        else:
            hand = 'Three of a Kind: ' + TOAK_card
        show_hand()
    elif card_value[0] == card_value[1] and card_value[0] == card_value[4]:
        if card_value[0] == 14:
            TOAK_card = 'Aces'
        elif card_value[0] == 13:
            TOAK_card = 'Kings'
        elif card_value[0] == 12:
            TOAK_card = 'Queens'
        elif card_value[0] == 11:
            TOAK_card = 'Jacks'
        elif card_value[0] == 10:
            TOAK_card = 'Tens'
        elif card_value[0] == 9:
            TOAK_card = 'Nines'
        elif card_value[0] == 8:
            TOAK_card = 'Eights'
        elif card_value[0] == 7:
            TOAK_card = 'Sevens'
        elif card_value[0] == 6:
            TOAK_card = 'Sixes'
        elif card_value[0] == 5:
            TOAK_card = 'Fives'
        elif card_value[0] == 4:
            TOAK_card = 'Fours'
        elif card_value[0] == 3:
            TOAK_card = 'Threes'
        elif card_value[0] == 2:
            TOAK_card = 'Twos'
        if card_value[2] == card_value[3]:
            if card_value[3] == 14:
                pair_card = 'Aces'
            elif card_value[3] == 13:
                pair_card = 'Kings'
            elif card_value[3] == 12:
                pair_card = 'Queens'
            elif card_value[3] == 11:
                pair_card = 'Jacks'
            elif card_value[3] == 10:
                pair_card = 'Tens'
            elif card_value[3] == 9:
                pair_card = 'Nines'
            elif card_value[3] == 8:
                pair_card = 'Eights'
            elif card_value[3] == 7:
                pair_card = 'Sevens'
            elif card_value[3] == 6:
                pair_card = 'Sixes'
            elif card_value[3] == 5:
                pair_card = 'Fives'
            elif card_value[3] == 4:
                pair_card = 'Fours'
            elif card_value[3] == 3:
                pair_card = 'Threes'
            elif card_value[3] == 2:
                pair_card = 'Twos'
            hand = 'Full House: ' + TOAK_card + ' over ' + pair_card
        else:
            hand = 'Three of a Kind: ' + TOAK_card
        show_hand()
    elif card_value[0] == card_value[2] and card_value[0] == card_value[3]:
        if card_value[0] == 14:
            TOAK_card = 'Aces'
        elif card_value[0] == 13:
            TOAK_card = 'Kings'
        elif card_value[0] == 12:
            TOAK_card = 'Queens'
        elif card_value[0] == 11:
            TOAK_card = 'Jacks'
        elif card_value[0] == 10:
            TOAK_card = 'Tens'
        elif card_value[0] == 9:
            TOAK_card = 'Nines'
        elif card_value[0] == 8:
            TOAK_card = 'Eights'
        elif card_value[0] == 7:
            TOAK_card = 'Sevens'
        elif card_value[0] == 6:
            TOAK_card = 'Sixes'
        elif card_value[0] == 5:
            TOAK_card = 'Fives'
        elif card_value[0] == 4:
            TOAK_card = 'Fours'
        elif card_value[0] == 3:
            TOAK_card = 'Threes'
        elif card_value[0] == 2:
            TOAK_card = 'Twos'
        if card_value[1] == card_value[4]:
            if card_value[1] == 14:
                pair_card = 'Aces'
            elif card_value[1] == 13:
                pair_card = 'Kings'
            elif card_value[1] == 12:
                pair_card = 'Queens'
            elif card_value[1] == 11:
                pair_card = 'Jacks'
            elif card_value[1] == 10:
                pair_card = 'Tens'
            elif card_value[1] == 9:
                pair_card = 'Nines'
            elif card_value[1] == 8:
                pair_card = 'Eights'
            elif card_value[1] == 7:
                pair_card = 'Sevens'
            elif card_value[1] == 6:
                pair_card = 'Sixes'
            elif card_value[1] == 5:
                pair_card = 'Fives'
            elif card_value[1] == 4:
                pair_card = 'Fours'
            elif card_value[1] == 3:
                pair_card = 'Threes'
            elif card_value[1] == 2:
                pair_card = 'Twos'
            hand = 'Full House: ' + TOAK_card + ' over ' + pair_card
        else:
            hand = 'Three of a Kind: ' + TOAK_card
        show_hand()
    elif card_value[0] == card_value[2] and card_value[0] == card_value[4]:
        if card_value[0] == 14:
            TOAK_card = 'Aces'
        elif card_value[0] == 13:
            TOAK_card = 'Kings'
        elif card_value[0] == 12:
            TOAK_card = 'Queens'
        elif card_value[0] == 11:
            TOAK_card = 'Jacks'
        elif card_value[0] == 10:
            TOAK_card = 'Tens'
        elif card_value[0] == 9:
            TOAK_card = 'Nines'
        elif card_value[0] == 8:
            TOAK_card = 'Eights'
        elif card_value[0] == 7:
            TOAK_card = 'Sevens'
        elif card_value[0] == 6:
            TOAK_card = 'Sixes'
        elif card_value[0] == 5:
            TOAK_card = 'Fives'
        elif card_value[0] == 4:
            TOAK_card = 'Fours'
        elif card_value[0] == 3:
            TOAK_card = 'Threes'
        elif card_value[0] == 2:
            TOAK_card = 'Twos'
        if card_value[1] == card_value[3]:
            if card_value[0] == 14:
                pair_card = 'Aces'
            elif card_value[0] == 13:
                pair_card = 'Kings'
            elif card_value[0] == 12:
                pair_card = 'Queens'
            elif card_value[0] == 11:
                pair_card = 'Jacks'
            elif card_value[0] == 10:
                pair_card = 'Tens'
            elif card_value[0] == 9:
                pair_card = 'Nines'
            elif card_value[0] == 8:
                pair_card = 'Eights'
            elif card_value[0] == 7:
                pair_card = 'Sevens'
            elif card_value[0] == 6:
                pair_card = 'Sixes'
            elif card_value[0] == 5:
                pair_card = 'Fives'
            elif card_value[0] == 4:
                pair_card = 'Fours'
            elif card_value[0] == 3:
                pair_card = 'Threes'
            elif card_value[0] == 2:
                pair_card = 'Twos'
            hand = 'Full House: ' + TOAK_card + ' over ' + pair_card
        else:
            hand = 'Three of a Kind: ' + TOAK_card
        show_hand()
    elif card_value[0] == card_value[3] and card_value[0] == card_value[4]:
        if card_value[0] == 14:
            TOAK_card = 'Aces'
        elif card_value[0] == 13:
            TOAK_card = 'Kings'
        elif card_value[0] == 12:
            TOAK_card = 'Queens'
        elif card_value[0] == 11:
            TOAK_card = 'Jacks'
        elif card_value[0] == 10:
            TOAK_card = 'Tens'
        elif card_value[0] == 9:
            TOAK_card = 'Nines'
        elif card_value[0] == 8:
            TOAK_card = 'Eights'
        elif card_value[0] == 7:
            TOAK_card = 'Sevens'
        elif card_value[0] == 6:
            TOAK_card = 'Sixes'
        elif card_value[0] == 5:
            TOAK_card = 'Fives'
        elif card_value[0] == 4:
            TOAK_card = 'Fours'
        elif card_value[0] == 3:
            TOAK_card = 'Threes'
        elif card_value[0] == 2:
            TOAK_card = 'Twos'
        if card_value[1] == card_value[2]:
            if card_value[1] == 14:
                pair_card = 'Aces'
            elif card_value[1] == 13:
                pair_card = 'Kings'
            elif card_value[1] == 12:
                pair_card = 'Queens'
            elif card_value[1] == 11:
                pair_card = 'Jacks'
            elif card_value[1] == 10:
                pair_card = 'Tens'
            elif card_value[1] == 9:
                pair_card = 'Nines'
            elif card_value[1] == 8:
                pair_card = 'Eights'
            elif card_value[1] == 7:
                pair_card = 'Sevens'
            elif card_value[1] == 6:
                pair_card = 'Sixes'
            elif card_value[1] == 5:
                pair_card = 'Fives'
            elif card_value[1] == 4:
                pair_card = 'Fours'
            elif card_value[1] == 3:
                pair_card = 'Threes'
            elif card_value[1] == 2:
                pair_card = 'Twos'
            hand = 'Full House: ' + TOAK_card + ' over ' + pair_card
        else:
            hand = 'Three of a Kind: ' + TOAK_card
        show_hand()
    elif card_value[1] == card_value[2] and card_value[1] == card_value[3]:
        if card_value[1] == 14:
            TOAK_card = 'Aces'
        elif card_value[1] == 13:
            TOAK_card = 'Kings'
        elif card_value[1] == 12:
            TOAK_card = 'Queens'
        elif card_value[1] == 11:
            TOAK_card = 'Jacks'
        elif card_value[1] == 10:
            TOAK_card = 'Tens'
        elif card_value[1] == 9:
            TOAK_card = 'Nines'
        elif card_value[1] == 8:
            TOAK_card = 'Eights'
        elif card_value[1] == 7:
            TOAK_card = 'Sevens'
        elif card_value[1] == 6:
            TOAK_card = 'Sixes'
        elif card_value[1] == 5:
            TOAK_card = 'Fives'
        elif card_value[1] == 4:
            TOAK_card = 'Fours'
        elif card_value[1] == 3:
            TOAK_card = 'Threes'
        elif card_value[1] == 2:
            TOAK_card = 'Twos'
        if card_value[0] == card_value[4]:
            if card_value[0] == 14:
                pair_card = 'Aces'
            elif card_value[0] == 13:
                pair_card = 'Kings'
            elif card_value[0] == 12:
                pair_card = 'Queens'
            elif card_value[0] == 11:
                pair_card = 'Jacks'
            elif card_value[0] == 10:
                pair_card = 'Tens'
            elif card_value[0] == 9:
                pair_card = 'Nines'
            elif card_value[0] == 8:
                pair_card = 'Eights'
            elif card_value[0] == 7:
                pair_card = 'Sevens'
            elif card_value[0] == 6:
                pair_card = 'Sixes'
            elif card_value[0] == 5:
                pair_card = 'Fives'
            elif card_value[0] == 4:
                pair_card = 'Fours'
            elif card_value[0] == 3:
                pair_card = 'Threes'
            elif card_value[0] == 2:
                pair_card = 'Twos'
            hand = 'Full House: ' + TOAK_card + ' over ' + pair_card
        else:
            hand = 'Three of a Kind: ' + TOAK_card
        show_hand()
    elif card_value[1] == card_value[2] and card_value[1] == card_value[4]:
        if card_value[1] == 14:
            TOAK_card = 'Aces'
        elif card_value[1] == 13:
            TOAK_card = 'Kings'
        elif card_value[1] == 12:
            TOAK_card = 'Queens'
        elif card_value[1] == 11:
            TOAK_card = 'Jacks'
        elif card_value[1] == 10:
            TOAK_card = 'Tens'
        elif card_value[1] == 9:
            TOAK_card = 'Nines'
        elif card_value[1] == 8:
            TOAK_card = 'Eights'
        elif card_value[1] == 7:
            TOAK_card = 'Sevens'
        elif card_value[1] == 6:
            TOAK_card = 'Sixes'
        elif card_value[1] == 5:
            TOAK_card = 'Fives'
        elif card_value[1] == 4:
            TOAK_card = 'Fours'
        elif card_value[1] == 3:
            TOAK_card = 'Threes'
        elif card_value[1] == 2:
            TOAK_card = 'Twos'
        if card_value[0] == card_value[3]:
            if card_value[3] == 14:
                pair_card = 'Aces'
            elif card_value[3] == 13:
                pair_card = 'Kings'
            elif card_value[3] == 12:
                pair_card = 'Queens'
            elif card_value[3] == 11:
                pair_card = 'Jacks'
            elif card_value[3] == 10:
                pair_card = 'Tens'
            elif card_value[3] == 9:
                pair_card = 'Nines'
            elif card_value[3] == 8:
                pair_card = 'Eights'
            elif card_value[3] == 7:
                pair_card = 'Sevens'
            elif card_value[3] == 6:
                pair_card = 'Sixes'
            elif card_value[3] == 5:
                pair_card = 'Fives'
            elif card_value[3] == 4:
                pair_card = 'Fours'
            elif card_value[3] == 3:
                pair_card = 'Threes'
            elif card_value[3] == 2:
                pair_card = 'Twos'
            hand = 'Full House: ' + TOAK_card + ' over ' + pair_card
        else:
            hand = 'Three of a Kind: ' + TOAK_card
        show_hand()
    elif card_value[1] == card_value[3] and card_value[1] == card_value[4]:
        if card_value[1] == 14:
            TOAK_card = 'Aces'
        elif card_value[1] == 13:
            TOAK_card = 'Kings'
        elif card_value[1] == 12:
            TOAK_card = 'Queens'
        elif card_value[1] == 11:
            TOAK_card = 'Jacks'
        elif card_value[1] == 10:
            TOAK_card = 'Tens'
        elif card_value[1] == 9:
            TOAK_card = 'Nines'
        elif card_value[1] == 8:
            TOAK_card = 'Eights'
        elif card_value[1] == 7:
            TOAK_card = 'Sevens'
        elif card_value[1] == 6:
            TOAK_card = 'Sixes'
        elif card_value[1] == 5:
            TOAK_card = 'Fives'
        elif card_value[1] == 4:
            TOAK_card = 'Fours'
        elif card_value[1] == 3:
            TOAK_card = 'Threes'
        elif card_value[1] == 2:
            TOAK_card = 'Twos'
        if card_value[0] == card_value[2]:
            if card_value[0] == 14:
                pair_card = 'Aces'
            elif card_value[0] == 13:
                pair_card = 'Kings'
            elif card_value[0] == 12:
                pair_card = 'Queens'
            elif card_value[0] == 11:
                pair_card = 'Jacks'
            elif card_value[0] == 10:
                pair_card = 'Tens'
            elif card_value[0] == 9:
                pair_card = 'Nines'
            elif card_value[0] == 8:
                pair_card = 'Eights'
            elif card_value[0] == 7:
                pair_card = 'Sevens'
            elif card_value[0] == 6:
                pair_card = 'Sixes'
            elif card_value[0] == 5:
                pair_card = 'Fives'
            elif card_value[0] == 4:
                pair_card = 'Fours'
            elif card_value[0] == 3:
                pair_card = 'Threes'
            elif card_value[0] == 2:
                pair_card = 'Twos'
            hand = 'Full House: ' + TOAK_card + ' over ' + pair_card
        else:
            hand = 'Three of a Kind: ' + TOAK_card
        show_hand()
    elif card_value[2] == card_value[3] and card_value[2] == card_value[4]:
        if card_value[2] == 14:
            TOAK_card = 'Aces'
        elif card_value[2] == 13:
            TOAK_card = 'Kings'
        elif card_value[2] == 12:
            TOAK_card = 'Queens'
        elif card_value[2] == 11:
            TOAK_card = 'Jacks'
        elif card_value[2] == 10:
            TOAK_card = 'Tens'
        elif card_value[2] == 9:
            TOAK_card = 'Nines'
        elif card_value[2] == 8:
            TOAK_card = 'Eights'
        elif card_value[2] == 7:
            TOAK_card = 'Sevens'
        elif card_value[2] == 6:
            TOAK_card = 'Sixes'
        elif card_value[2] == 5:
            TOAK_card = 'Fives'
        elif card_value[2] == 4:
            TOAK_card = 'Fours'
        elif card_value[2] == 3:
            TOAK_card = 'Threes'
        elif card_value[2] == 2:
            TOAK_card = 'Twos'
        if card_value[0] == card_value[1]:
            if card_value[0] == 14:
                pair_card = 'Aces'
            elif card_value[0] == 13:
                pair_card = 'Kings'
            elif card_value[0] == 12:
                pair_card = 'Queens'
            elif card_value[0] == 11:
                pair_card = 'Jacks'
            elif card_value[0] == 10:
                pair_card = 'Tens'
            elif card_value[0] == 9:
                pair_card = 'Nines'
            elif card_value[0] == 8:
                pair_card = 'Eights'
            elif card_value[0] == 7:
                pair_card = 'Sevens'
            elif card_value[0] == 6:
                pair_card = 'Sixes'
            elif card_value[0] == 5:
                pair_card = 'Fives'
            elif card_value[0] == 4:
                pair_card = 'Fours'
            elif card_value[0] == 3:
                pair_card = 'Threes'
            elif card_value[0] == 2:
                pair_card = 'Twos'
            hand = 'Full House: ' + TOAK_card + ' over ' + pair_card
        else:
            hand = 'Three of a Kind: ' + TOAK_card
        show_hand()
    else:
        check_S()
def check_S():
    global hand
    if hc == 'King':
        if card_value[0] == 12 or card_value[1] == 12 or card_value[2] == 12 or card_value[3] == 12 or card_value[4] == 12:
            if card_value[0] == 11 or card_value[1] == 11 or card_value[2] == 11 or card_value[3] == 11 or card_value[4] == 11:
                if card_value[0] == 10 or card_value[1] == 10 or card_value[2] == 10 or card_value[3] == 10 or card_value[4] == 10:
                    if card_value[0] == 9 or card_value[1] == 9 or card_value[2] == 9 or card_value[3] == 9 or card_value[4] == 9:
                        hand = 'Straight'
                        show_hand()
                    else:
                        check_TP()
                else:
                    check_TP()
            else:
                check_TP()
        else:
            check_TP()
    elif hc == 'Queen':
        if card_value[0] == 11 or card_value[1] == 11 or card_value[2] == 11 or card_value[3] == 11 or card_value[4] == 11:
            if card_value[0] == 10 or card_value[1] == 10 or card_value[2] == 10 or card_value[3] == 10 or card_value[4] == 10:
                if card_value[0] == 9 or card_value[1] == 9 or card_value[2] == 9 or card_value[3] == 9 or card_value[4] == 9:
                    if card_value[0] == 8 or card_value[1] == 8 or card_value[2] == 8 or card_value[3] == 8 or card_value[4] == 8:
                        hand = 'Straight'
                        show_hand()
                    else:
                        check_TP()
                else:
                    check_TP()
            else:
                check_TP()
        else:
            check_TP()
    elif hc == 'Jack':
        if card_value[0] == 10 or card_value[1] == 10 or card_value[2] == 10 or card_value[3] == 10 or card_value[4] == 10:
            if card_value[0] == 9 or card_value[1] == 9 or card_value[2] == 9 or card_value[3] == 9 or card_value[4] == 9:
                if card_value[0] == 8 or card_value[1] == 8 or card_value[2] == 8 or card_value[3] == 8 or card_value[4] == 8:
                    if card_value[0] == 7 or card_value[1] == 7 or card_value[2] == 7 or card_value[3] == 7 or card_value[4] == 7:
                        hand = 'Straight'
                        show_hand()
                    else:
                        check_TP()
                else:
                    check_TP()
            else:
                check_TP()
        else:
            check_TP()
    elif hc == 'Ten':
        if card_value[0] == 9 or card_value[1] == 9 or card_value[2] == 9 or card_value[3] == 9 or card_value[4] == 9:
            if card_value[0] == 8 or card_value[1] == 8 or card_value[2] == 8 or card_value[3] == 8 or card_value[4] == 8:
                if card_value[0] == 7 or card_value[1] == 7 or card_value[2] == 7 or card_value[3] == 7 or card_value[4] == 7:
                    if card_value[0] == 6 or card_value[1] == 6 or card_value[2] == 6 or card_value[3] == 6 or card_value[4] == 6:
                        hand = 'Straight'
                        show_hand()
                    else:
                        check_TP()
                else:
                    check_TP()
            else:
                check_TP()
        else:
            check_TP()
    elif hc == 'Nine':
        if card_value[0] == 8 or card_value[1] == 8 or card_value[2] == 8 or card_value[3] == 8 or card_value[4] == 8:
            if card_value[0] == 7 or card_value[1] == 7 or card_value[2] == 7 or card_value[3] == 7 or card_value[4] == 7:
                if card_value[0] == 6 or card_value[1] == 6 or card_value[2] == 6 or card_value[3] == 6 or card_value[4] == 6:
                    if card_value[0] == 5 or card_value[1] == 5 or card_value[2] == 5 or card_value[3] == 5 or card_value[4] == 5:
                        hand = 'Straight'
                        show_hand()
                    else:
                        check_TP()
                else:
                    check_TP()
            else:
                check_TP()
        else:
            check_TP()
    elif hc == 'Eight':
        if card_value[0] == 7 or card_value[1] == 7 or card_value[2] == 7 or card_value[3] == 7 or card_value[4] == 7:
            if card_value[0] == 6 or card_value[1] == 6 or card_value[2] == 6 or card_value[3] == 6 or card_value[4] == 6:
                if card_value[0] == 5 or card_value[1] == 5 or card_value[2] == 5 or card_value[3] == 5 or card_value[4] == 5:
                    if card_value[0] == 4 or card_value[1] == 4 or card_value[2] == 4 or card_value[3] == 4 or card_value[4] == 4:
                        hand = 'Straight'
                        show_hand()
                    else:
                        check_TP()
                else:
                    check_TP()
            else:
                check_TP()
        else:
            check_TP()
    elif hc == 'Seven':
        if card_value[0] == 6 or card_value[1] == 6 or card_value[2] == 6 or card_value[3] == 6 or card_value[4] == 6:
            if card_value[0] == 5 or card_value[1] == 5 or card_value[2] == 5 or card_value[3] == 5 or card_value[4] == 5:
                if card_value[0] == 4 or card_value[1] == 4 or card_value[2] == 4 or card_value[3] == 4 or card_value[4] == 4:
                    if card_value[0] == 3 or card_value[1] == 3 or card_value[2] == 3 or card_value[3] == 3 or card_value[4] == 3:
                        hand = 'Straight'
                        show_hand()
                    else:
                        check_TP()
                else:
                    check_TP()
            else:
                check_TP()
        else:
            check_TP()
    elif hc == 'Six':
        if card_value[0] == 5 or card_value[1] == 5 or card_value[2] == 5 or card_value[3] == 5 or card_value[4] == 5:
            if card_value[0] == 4 or card_value[1] == 4 or card_value[2] == 4 or card_value[3] == 4 or card_value[4] == 4:
                if card_value[0] == 3 or card_value[1] == 3 or card_value[2] == 3 or card_value[3] == 3 or card_value[4] == 3:
                    if card_value[0] == 2 or card_value[1] == 2 or card_value[2] == 2 or card_value[3] == 2 or card_value[4] == 2:
                        hand = 'Straight'
                        show_hand()
                    else:
                        check_TP()
                else:
                    check_TP()
            else:
                check_TP()
        else:
            check_TP()
    elif hc == 'Ace':
        if card_value[0] == 5 or card_value[1] == 5 or card_value[2] == 5 or card_value[3] == 5 or card_value[4] == 5:
            if card_value[0] == 4 or card_value[1] == 4 or card_value[2] == 4 or card_value[3] == 4 or card_value[4] == 4:
                if card_value[0] == 3 or card_value[1] == 3 or card_value[2] == 3 or card_value[3] == 3 or card_value[4] == 3:
                    if card_value[0] == 2 or card_value[1] == 2 or card_value[2] == 2 or card_value[3] == 2 or card_value[4] == 2:
                        hand = 'Straight'
                        show_hand()
                    else:
                        check_TP()
                else:
                    check_TP()
            else:
                check_TP()
        elif card_value[0] == 13 or card_value[1] == 13 or card_value[2] == 13 or card_value[3] == 13 or card_value[4] == 13:
            if card_value[0] == 12 or card_value[1] == 12 or card_value[2] == 12 or card_value[3] == 12 or card_value[4] == 12:
                if card_value[0] == 11 or card_value[1] == 11 or card_value[2] == 11 or card_value[3] == 11 or card_value[4] == 11:
                    if card_value[0] == 10 or card_value[1] == 10 or card_value[2] == 10 or card_value[3] == 10 or card_value[4] == 10:
                        hand = 'Straight'
                        show_hand()
                    else:
                        check_TP()
                else:
                    check_TP()
            else:
                check_TP()
        else:
            check_TP()
    else:
        check_TP()
def check_TP():
    global hand
    global pair_card1
    global pair_card2
    if card_value[0] == card_value[1] or card_value[0] == card_value[2] or card_value[0] == card_value[3] or card_value[0] == card_value[4]:
        if card_value[0] == 14:
            pair_card1 = 'Aces'
        elif card_value[0] == 13:
            pair_card1 = 'Kings'
        elif card_value[0] == 12:
            pair_card1 = 'Queens'
        elif card_value[0] == 11:
            pair_card1 = 'Jacks'
        elif card_value[0] == 10:
            pair_card1 = 'Tens'
        elif card_value[0] == 9:
            pair_card1 = 'Nines'
        elif card_value[0] == 8:
            pair_card1 = 'Eights'
        elif card_value[0] == 7:
            pair_card1 = 'Sevens'
        elif card_value[0] == 6:
            pair_card1 = 'Sixes'
        elif card_value[0] == 5:
            pair_card1 = 'Fives'
        elif card_value[0] == 4:
            pair_card1 = 'Fours'
        elif card_value[0] == 3:
            pair_card1 = 'Threes'
        elif card_value[0] == 2:
            pair_card1 = 'Twos'
        if card_value[1] == card_value[2] or card_value[1] == card_value[3] or card_value[1] == card_value[4]:
            if card_value[1] == 14:
                pair_card2 = 'Aces'
            elif card_value[1] == 13:
                pair_card2 = 'Kings'
            elif card_value[1] == 12:
                pair_card2 = 'Queens'
            elif card_value[1] == 11:
                pair_card2 = 'Jacks'
            elif card_value[1] == 10:
                pair_card2 = 'Tens'
            elif card_value[1] == 9:
                pair_card2 = 'Nines'
            elif card_value[1] == 8:
                pair_card2 = 'Eights'
            elif card_value[1] == 7:
                pair_card2 = 'Sevens'
            elif card_value[1] == 6:
                pair_card2 = 'Sixes'
            elif card_value[1] == 5:
                pair_card2 = 'Fives'
            elif card_value[1] == 4:
                pair_card2 = 'Fours'
            elif card_value[1] == 3:
                pair_card2 = 'Threes'
            elif card_value[1] == 2:
                pair_card2 = 'Twos'
            hand = 'Two Pair: ' + pair_card1 + ' and ' + pair_card2
        elif card_value[2] == card_value[3] or card_value[2] == card_value[4]:
            if card_value[2] == 14:
                pair_card2 = 'Aces'
            elif card_value[2] == 13:
                pair_card2 = 'Kings'
            elif card_value[2] == 12:
                pair_card2 = 'Queens'
            elif card_value[2] == 11:
                pair_card2 = 'Jacks'
            elif card_value[2] == 10:
                pair_card2 = 'Tens'
            elif card_value[2] == 9:
                pair_card2 = 'Nines'
            elif card_value[2] == 8:
                pair_card2 = 'Eights'
            elif card_value[2] == 7:
                pair_card2 = 'Sevens'
            elif card_value[2] == 6:
                pair_card2 = 'Sixes'
            elif card_value[2] == 5:
                pair_card2 = 'Fives'
            elif card_value[2] == 4:
                pair_card2 = 'Fours'
            elif card_value[2] == 3:
                pair_card2 = 'Threes'
            elif card_value[2] == 2:
                pair_card2 = 'Twos'
            hand = 'Two Pair: ' + pair_card1 + ' and ' + pair_card2
        elif card_value[3] == card_value[4]:
            if card_value[3] == 14:
                pair_card2 = 'Aces'
            elif card_value[3] == 13:
                pair_card2 = 'Kings'
            elif card_value[3] == 12:
                pair_card2 = 'Queens'
            elif card_value[3] == 11:
                pair_card2 = 'Jacks'
            elif card_value[3] == 10:
                pair_card2 = 'Tens'
            elif card_value[3] == 9:
                pair_card2 = 'Nines'
            elif card_value[3] == 8:
                pair_card2 = 'Eights'
            elif card_value[3] == 7:
                pair_card2 = 'Sevens'
            elif card_value[3] == 6:
                pair_card2 = 'Sixes'
            elif card_value[3] == 5:
                pair_card2 = 'Fives'
            elif card_value[3] == 4:
                pair_card2 = 'Fours'
            elif card_value[3] == 3:
                pair_card2 = 'Threes'
            elif card_value[3] == 2:
                pair_card2 = 'Twos'
            hand = 'Two Pair: ' + pair_card1 + ' and ' + pair_card2
        else:
            hand = 'Pair of ' + pair_card1
    elif card_value[1] == card_value[2] or card_value[1] == card_value[3] or card_value[1] == card_value[4]:
        if card_value[1] == 14:
            pair_card1 = 'Aces'
        elif card_value[1] == 13:
            pair_card1 = 'Kings'
        elif card_value[1] == 12:
            pair_card1 = 'Queens'
        elif card_value[1] == 11:
            pair_card1 = 'Jacks'
        elif card_value[1] == 10:
            pair_card1 = 'Tens'
        elif card_value[1] == 9:
            pair_card1 = 'Nines'
        elif card_value[1] == 8:
            pair_card1 = 'Eights'
        elif card_value[1] == 7:
            pair_card1 = 'Sevens'
        elif card_value[1] == 6:
            pair_card1 = 'Sixes'
        elif card_value[1] == 5:
            pair_card1 = 'Fives'
        elif card_value[1] == 4:
            pair_card1 = 'Fours'
        elif card_value[1] == 3:
            pair_card1 = 'Threes'
        elif card_value[1] == 2:
            pair_card1 = 'Twos'
        if card_value[2] == card_value[3] or card_value[2] == card_value[4]:
            if card_value[2] == 14:
                pair_card2 = 'Aces'
            elif card_value[2] == 13:
                pair_card2 = 'Kings'
            elif card_value[2] == 12:
                pair_card2 = 'Queens'
            elif card_value[2] == 11:
                pair_card2 = 'Jacks'
            elif card_value[2] == 10:
                pair_card2 = 'Tens'
            elif card_value[2] == 9:
                pair_card2 = 'Nines'
            elif card_value[2] == 8:
                pair_card2 = 'Eights'
            elif card_value[2] == 7:
                pair_card2 = 'Sevens'
            elif card_value[2] == 6:
                pair_card2 = 'Sixes'
            elif card_value[2] == 5:
                pair_card2 = 'Fives'
            elif card_value[2] == 4:
                pair_card2 = 'Fours'
            elif card_value[2] == 3:
                pair_card2 = 'Threes'
            elif card_value[2] == 2:
                pair_card2 = 'Twos'
            hand = 'Two Pair: ' + pair_card1 + ' and ' + pair_card2
        elif card_value[3] == card_value[4]:
            if card_value[3] == 14:
                pair_card2 = 'Aces'
            elif card_value[3] == 13:
                pair_card2 = 'Kings'
            elif card_value[3] == 12:
                pair_card2 = 'Queens'
            elif card_value[3] == 11:
                pair_card2 = 'Jacks'
            elif card_value[3] == 10:
                pair_card2 = 'Tens'
            elif card_value[3] == 9:
                pair_card2 = 'Nines'
            elif card_value[3] == 8:
                pair_card2 = 'Eights'
            elif card_value[3] == 7:
                pair_card2 = 'Sevens'
            elif card_value[3] == 6:
                pair_card2 = 'Sixes'
            elif card_value[3] == 5:
                pair_card2 = 'Fives'
            elif card_value[3] == 4:
                pair_card2 = 'Fours'
            elif card_value[3] == 3:
                pair_card2 = 'Threes'
            elif card_value[3] == 2:
                pair_card2 = 'Twos'
            hand = 'Two Pair: ' + pair_card1 + ' and ' + pair_card2
        else:
            hand = 'Pair of ' + pair_card1
    elif card_value[2] == card_value[3] or card_value[2] == card_value[4]:
        if card_value[2] == 14:
            pair_card1 = 'Aces'
        elif card_value[2] == 13:
            pair_card1 = 'Kings'
        elif card_value[2] == 12:
            pair_card1 = 'Queens'
        elif card_value[2] == 11:
            pair_card1 = 'Jacks'
        elif card_value[2] == 10:
            pair_card1 = 'Tens'
        elif card_value[2] == 9:
            pair_card1 = 'Nines'
        elif card_value[2] == 8:
            pair_card1 = 'Eights'
        elif card_value[2] == 7:
            pair_card1 = 'Sevens'
        elif card_value[2] == 6:
            pair_card1 = 'Sixes'
        elif card_value[2] == 5:
            pair_card1 = 'Fives'
        elif card_value[2] == 4:
            pair_card1 = 'Fours'
        elif card_value[2] == 3:
            pair_card1 = 'Threes'
        elif card_value[2] == 2:
            pair_card1 = 'Twos'
        hand = 'Pair of ' + pair_card1
    elif card_value[3] == card_value[4]:
        if card_value[3] == 14:
            pair_card1 = 'Aces'
        elif card_value[3] == 13:
            pair_card1 = 'Kings'
        elif card_value[3] == 12:
            pair_card1 = 'Queens'
        elif card_value[3] == 11:
            pair_card1 = 'Jacks'
        elif card_value[3] == 10:
            pair_card1 = 'Tens'
        elif card_value[3] == 9:
            pair_card1 = 'Nines'
        elif card_value[3] == 8:
            pair_card1 = 'Eights'
        elif card_value[3] == 7:
            pair_card1 = 'Sevens'
        elif card_value[3] == 6:
            pair_card1 = 'Sixes'
        elif card_value[3] == 5:
            pair_card1 = 'Fives'
        elif card_value[3] == 4:
            pair_card1 = 'Fours'
        elif card_value[3] == 3:
            pair_card1 = 'Threes'
        elif card_value[3] == 2:
            pair_card1 = 'Twos'
        hand = 'Pair of ' + pair_card1
    else:
        hand = 'High Card'
def show_hand():
    print 'You got a ' + hand + ' with a High Card of ' + hc
    print drawn_cards
swap()