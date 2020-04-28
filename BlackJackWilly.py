# -*- coding: utf-8 -*-
"""
This is my BlackJack program :)
BlackJack Willy
"""
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"[{self.rank} of {self.suit}]"

class Deck:
    def __init__(self):
        self.deck = []  
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        printdeck = "Full Deck:\n"
        for cards in self.deck:
            printdeck += cards.rank +" of " + cards.suit +"\n"
        return printdeck

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop(0)

class Hand:
    def __init__(self):
        self.cards = []  
        self.value = 0   
        self.aces = 0    
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        if self.value > 21 and self.aces >0:
            self.aces -= 1
            self.value -= 10
        
    def __str__(self):
        printhand = ''
        for heldcards in self.cards:
            printhand += '[' + heldcards.rank + ' of ' + heldcards.suit + '] '
        return printhand

class Chips:
    def __init__(self,total=100):
        self.total = total  
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(mychips):
    print(f"\nYou have {mychips.total} chips")
    player_bet = 0
    while True:
            try:
                player_bet=int(input("Place your bet: "))
            except:
                print ("Whole number of chips only!")
                continue
            else:
                if player_bet > mychips.total or player_bet <= 0:
                    print("You can't bet that many chips!")
                    continue                    
                else:
                    mychips.bet = player_bet
                    return player_bet

def show_some(playerhand,dealerhand):
    print ("\nDealer's Hand (one card is hidden!): ",dealerhand.cards[0],"[?? of ?????]")
    print ("\nYour Hand: ",playerhand)
    
def hit(deck,hand):
    hand.add_card(deck.deal())

def hit_or_stand(deck,hand):
    global playing  
    while True:
            try:
                hitstick = input("Enter H for another card or any other key to stick: ").upper()
            except:
                continue
            else:
                if hitstick == "H":
                    hit(deck,hand)
                    break
                else:
                    playing = False
                    break

def player_wins(chips):
    print(f"\nYou won {chips.bet} chips!")
    chips.win_bet()
    print(f"You have {chips.total} chips")

def player_loses(chips):
    print(f"\nYou lost {chips.bet} chips!")
    chips.lose_bet()
    print(f"You have {chips.total} chips")
       
def replay():
    playagain = ""
    while playagain not in ["Y","N"]:
        playagain = input("Play again? (Y/N)")
        playagain = playagain.upper()
    return playagain == "Y"

# Main routine starts here

print("\n" * 10, "Welcome to MinerWilly's BlackJack\n","=" * 33)

plchips = Chips()

while True:

    thedeck = Deck()
    thedeck.shuffle()
    playerhand = Hand()
    dealerhand = Hand()
    bust = False
     
    for dealing in [1,2]:
        playerhand.add_card(thedeck.deal())
        dealerhand.add_card(thedeck.deal())
    
    plbet = take_bet(plchips)
    
    show_some(playerhand,dealerhand)
    
    print("\nYou are in Play\n---------------")
    
    while playing:
        hit_or_stand(thedeck,playerhand)
        print ("\nYour Hand: ",playerhand)
        if playerhand.value > 21:
            print("\nYOU BUST!")
            playing = False
            bust = True
            player_loses(plchips)
            print("\n The Dealer's Hand was: ",dealerhand)

    if not bust:
        print("\nDealer is in Play\n---------------")
        print("\nDealer's Hand: ",dealerhand)
        while dealerhand.value < 17:
            hit(thedeck,dealerhand)
            print("\nDealer takes a card...\nDealer's Hand: ",dealerhand)
        if dealerhand.value > 21:
            print("\nDealer BUST...You win!")
            player_wins(plchips)
        elif playerhand.value > dealerhand.value:
            print("\nYour hand is better...You win!")
            player_wins(plchips)
        else:
            print("\nUnlucky...You lose!")
            player_loses(plchips)
                   
    if plchips.total == 0:
        print("\nYou've run out of chips - goodbye!")
        break    

    if replay():
        playing = True
    else:
        break
    
