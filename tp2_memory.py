"""
CSCI 150 Test Project 2

Name: Hinda Ibraahim 
Section: 150B



This programs plays a text-based version of memory game. The user has to find
the matching pairs of letters. The letters will only appear of a match has been
made or for 2 seconds. At the end after all matches have been made, all the
letters will displayed.

"""



from random import shuffle, randint
import time
import datetime


track = []

letter = ['A','A', 'B', 'B', 'C', 'C', 'E', 'E','D','D','F','F','G','G','H','H']
row = 4
com = 4 
  
def disboard(track):
    """
    Displays board witrh 4 rows and 4 columns
    
    Args:
        track =  list of numbers 
    Return:
        
        board
        

    """
    
    for i in range(len(track)):
        if (i+1) % row == 0:
            print((track)[i], end = '\n')
        else:
            if i >= 9: 
                print(list(track)[i], end = ' ')
            else:
                print(list(track)[i], end = '  ')

def inputs(track, letter):
    """
    checks if the inputs are in the range of 1 to 16, if it's not the same number and
    if it wasn't already answered
    
    Args:
        track = list of numbers 
        letter = list of letters
        
    Return:
        2 answer choices from user 
    
    """
    disboard(track)
    
    while True:
        answer1, answer2 = input("Pick two squares to look under: ").split()
        
        answer1, answer2 = int(answer1), int(answer2)
        if answer1 < 1 or answer1 > 16 or answer2 < 1 or answer2 > 16 or answer1 == answer2:
            print("Invalid input, please try again.")
            continue
            
            answer1 -= 1
            answer2 -= 1

            
        if track[answer1] == letter[answer1] or track[answer2] == letter[answer2]:
            print("Invalid input, please try again.")
            continue
        
        
        return answer1, answer2


def wrongchoice(track, letter, answer1, answer2):
    """
    Tells the user the matches are wrong 
    
    Args:
        track = list of number
        letter = list of letters
        answer1 = frist input from user
        answer2 = second input from user
        
    Return:
        
        
    """
    choice1, choice2 = track[answer1], track[answer2]
    
    track[answer1], track[answer2] = letter[answer1], letter[answer2]
    disboard(track)

    print("Sorry! The letter do not match!")
    time.sleep(2)
    track[answer1], track[answer2] = choice1, choice2
            
         
    
            
def play_game():
    """
    Game initializer. Plays the whole game 
    
    Args:
        
    
    Return:
    
    """
    
    
    for i in range(16):
        track.append(str(i+1))
    
    shuffle(letter)
    
    start = datetime.datetime.now()
    sets = 0
    
    while (sets < 16):
        
        answer1, answer2 = inputs(track, letter)
        if letter[answer1] == letter[answer2]:
            track[answer1], track[answer2] = letter[answer1], letter[answer2]
            sets += 2
            
        else:
            wrongchoice(track, letter, answer1, answer2)
            
    
    disboard(track)
    print("You win!")
    done = datetime.datetime.now()
    difference = done - start
    print("It took you, " ,sets, "guesses and", difference.seconds, " seconds.")
     
if __name__ == "__main__":
    play_game()
     
    


