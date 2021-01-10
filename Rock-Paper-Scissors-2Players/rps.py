import emoji
def rps(p1,p2):
    if p1 == p2:
        return "It's a tie!"
    elif p1 == 'rock':
       if p2 == 'scissors' or p2 == 'scissor':
           return "First player wins!"
       else:
           return "Second Player wins!"
    elif p1 == 'scissors' or p1 == 'scissor':
       if p2 == 'paper':
           return "First player win!"
       else:
           return"Second player wins!"
    elif p1 == 'paper':
       if p2 == 'rock':
           return "First player wins!"
       else:
           return "Second player win!"
    else:
       return "Invalid input!"

print("Write your choice in TEXT:" +emoji.emojize(u"\u2B07"))       
print(emoji.emojize(":raised_fist:")+"--Rock") 
print(emoji.emojize(u"\u2702")+"--Scissors")  
print(emoji.emojize(u"\U0001F4C4")+"--Paper")

player1=input("Enter Player One Choice:")
player2=input("Enter Player Two Choice:")
 
print(rps(player1, player2))