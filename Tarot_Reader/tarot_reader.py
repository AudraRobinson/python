"""
   Tarot Card Reading:
   1. Shuffle deck.
   2. Determine spread for reading.
   3. For 3-card spread, ask questions about past, present, future.
   4. For 6-card spread, ask questions about: how player views themself, what they want right now, fears, what is going for them, what is going against them, and the likely outcome.
   5. Draw number of cards equal to spread.
"""

from pathlib import Path
import random as rand
import pandas

# Class for card objects
class Cards:
    def __init__(self, upright_filePath, reverse_filePath):
       self.cardsInDeck = []
       self.cardsDrawn = []
       self.upright_filePath = upright_filePath
       self.reverse_filePath = reverse_filePath
       
       
    # Creates an upright tarot cards
    def createUprightDeck(self, upright_filePath):
        upright_deck = pandas.read_csv(upright_filePath)
        list_upright_card = upright_deck["CARD"].values
        list_upright_description = upright_deck["DESCRIPTION"].values
        upright_tarot = {card:desc for card, desc in zip(list_upright_card,list_upright_description, strict=True)}
        return upright_tarot
            
    # Creates a reversed tarot deck        
    def createReverseDeck(self, reverse_filePath):
        reversed_deck = pandas.read_csv(reverse_filePath)
        list_reversed_card = reversed_deck["CARD"].values
        list_reversed_description = reversed_deck["DESCRIPTION"].values
        reversed_tarot = {card:desc for card, desc in zip(list_reversed_card, list_reversed_description, strict=True)}
        return reversed_tarot
    
    def standard_reading(self, reading=True):
        self.reading = reading
        while reading:
            try:
                user_input = input(int
                                   ("\nWhat type of tarot reading would you like? Please\n"
                                            "enter a number that corresponds to an available option.\n"
                                            "1: Standard Major Arcana Spread\n"
                                            "2: Universal Major Arcana Spread\n"
                                            "3. Exit\n"
                                            "Enter a choice: ")
                                   )
                
                if user_input == 1:
                    # call standard spread
                    upright_deck = self.createUprightDeck(upright_filePath)
                    reverse_deck = self.createReverseDeck(reverse_filePath)
                    self.three_card_spread(user_input, upright_deck,reverse_deck)
                    
                elif user_input == 2:
                    # call universal spread
                    upright_deck = self.createUprightDeck(upright_filePath)
                    reverse_deck = self.createReverseDeck(reverse_filePath)
                    self.six_card_spread(user_input, upright_deck, reverse_deck)
                    
                elif user_input == 3:
                    # Exit program
                    print("Bye, come again soon!")
                    break
                
                else:
                    # Catch integers that are not 1, 2, or 3
                    print(user_input, " is not a valid option. Please try again.\n\n")
                
            except ValueError:
                """
                value error exception displays a message for all other
                non integer inputs entered.
                """
                # Catches all other inputs enter str, float, etc
                print("ERROR: Please enter a valid option. "
                "Valid options are integers 1, 2, or 3\n\n")
            
    def three_card_spread(self, user_input, upright_tarot, reverse_tarot):
        """
        three_card_spread:
        If user input is equal to 1, display a 3 card tarot spread.
        """
        self.user_input = user_input
        self.upright_tarot = upright_tarot
        self.reverse_tarot = reverse_tarot
        
        while user_input == 1:
            # Randomizing ints to draw a random number of cards
            x = rand.randint(0,3)
            upright_deck = rand.sample(upright_tarot, x)
            y = 3 - x
            if y > 0:
                revese_deck = rand.sample(reverse_tarot, y)
                deck = upright_deck
                deck.extend(revese_deck)
            else:
                deck = upright_deck

            # Randomize the order the cards are drawn
            tarot_deck = rand.sample(deck, 3)
            
            # Set headers for cards drawn (made a set to remove any duplicates)
            set_header = {"~~ Draw 1 : The Past ~~",
                          "~~ Draw 2 : The Present ~~",
                          "~~ Draw 3 : The Future ~~"
                          }
            
            # Turn set header into a sorted tuple
            set_header_standard = sorted(tuple(set_header))
            
            # Changes tarot deck from list -> dict -> list
            dict_tarot_deck = {k:v for k, v in tarot_deck}
            list_tarot_deck = list(dict_tarot_deck.items())
            
            # Create header to display with reading
            print("\n\n\n\033[1;30;48m" + 
                  "~~~~~ STANDARD TAROT READING ~~~~~"
                  + "\033[0;30;48m\n")
            
            # Print out header, drawn number, card and its description
            for x, (key, value) in zip(set_header_standard, list_tarot_deck):
                print("\033[1;46;48m" + x + "\033[0;30;48m")
                print("\033[1;30;48m" + key + "\033[0;30;48m")
                print(value, "\n")
            
                  
    def six_card_spread(self, user_input, upright_tarot, reverse_tarot):
        """
        six_card_spread: If user input is equal to 2, display a 6 card tarot spread.

        Args:
            user_input (_type_): _description_
            upright_tarot (_type_): _description_
            reverse_tarot (_type_): _description_
        """
        self.user_input = user_input
        self.upright_tarot = upright_tarot
        self.reverse_tarot = reverse_tarot
        
        while user_input == 2:
            x = rand.randint(0,6)
            upright_deck = rand.sample(upright_tarot, x)
            y = 6 - x
            if y > 0:
                reverse_deck = rand.sample(reverse_deck, y)
                deck = upright_deck
                deck.extend(reverse_deck)
            else:
                deck = upright_deck
                
            tarot_deck = rand.sample(deck, 6)
            
            tuple_universal_headers = (
                '~~ Draw 1 : How you feel about yourself ~~',
                '~~ Draw 2 : What you want most right now ~~',
                '~~ Draw 3 : Your fears ~~',
                '~~ Draw 4 : What is going for you ~~',
                '~~ Draw 5 : What is going against you ~~',
                '~~ Draw 6 : The likely outcome ~~'
            )
            
            # Changes tarot deck from list -> dict -> list
            dict_tarot_deck = {k:v for k, v in tarot_deck}
            list_tarot_deck = list(dict_tarot_deck.items())
            
            # Create header to display with reading
            print("\n\n\n\033[1;30;48m" + 
                  "~~~~~ UNIVERSAL TAROT READING ~~~~~"
                  + "\033[0;30;48m\n")
            
            for x, (key, value) in zip(tuple_universal_headers, list_tarot_deck):
                print("\033[1;46;48m" + x + "\033[0;30;48m")
                print("\033[1;46;48m" + key + "\033[0;30;48m")
                print(value, "\n")
        

def OpeningMessage(player_name):
    return f"Welcome {player_name} to your card reading.\n"+\
            "You can choose from a standard reading which displays 3 cards\n"+\
            "and provides you with a reading of the past, present, or future.\n"+\
            "You can also decide on a universal reading which displays\n"+"6 cards and reveals more in depth details!"

def EndingMessage():
    return "\033[1;30;48m" +\
            "With an automated system like this, it's very tempting" \
            + " to immediately\n" +\
            "repeat a reading if the answer you got was either not" \
            + " what you wanted\n" +\
            "to hear. The first reading will always be the most" \
            + " appropriate. If you\n" +\
            "would like clarification on something, use a different " \
            + " reading spread.\n" +\
            "\033[0;30;48m \n\n"

def main():
    global upright_filePath
    upright_filePath = Path("C:\Users\audra\Documents\python-game-master\python-game-master\TarotCardsUpright.csv")
    global reverse_filePath
    reverse_filePath = Path("C:\Users\audra\Documents\python-game-master\python-game-master\TarotCardsReversed.csv")
    
    name = input("What is your name?")
    OpeningMessage(name)
    Cards(upright_filePath, reverse_filePath)
    EndingMessage()

if __name__ == "__main__":
    main()