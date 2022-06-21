import random

class card:
    """A small card with a value between 1 and 13.
    
    The responsibility of the Card is to keep track of the value of the current and the next card.
    
    Attributes:
        value (int): The number value on the card.
    """
    """Constructs a new instance of Card.
        
        Args:
            sefl (Card): An instance of Card.
    """

            
import random
class Card:

    def __init__(self):
        self.value = 0

    def roll(self):
        self.value = random.randrange(1,13)
    
    def get_value(self):
        return self.value
