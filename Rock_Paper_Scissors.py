import random

class Game:
    
    def __init__(self):
        self.score1=0
        self.score2=0
        self.helper()
    
    def helper(self):
        print(f"Your score is {self.score1} and Computer score is {self.score2}")
        #human move
        print()
        if self.score1>=4:
            print("You Won Game Over")
            k=self.choose()
            if k!=1:
                return
        elif self.score2>=4:
            print("You Lost Game Over")
            l=self.choose()
            if l!=1:
                return
        self.move1=input("Enter your move: ")
        self.c_move()
        
    def c_move(self):
        l=['r','p','s']
        #computer move
        self.move2=random.choice(l)
        self.check()
    
    def check(self):
        if self.move1=='p' and self.move2=='r':
            print(f"You Won -- your move is {self.move1} and computer move is {self.move2}")
            self.score1+=1
            return self.helper()
        
        elif self.move1=='s' and self.move2=='p':
            self.score1+=1
            print(f"You Won -- your move is {self.move1} and computer move is {self.move2}")
            return self.helper()
        
        elif self.move1=='r' and self.move2=='s':
            self.score1+=1
            print(f"You Won -- your move is {self.move1} and computer move is {self.move2}")
            return self.helper()
        
        elif self.move1=='r' and self.move2=='p':
            self.score2+=1
            print(f"You Lost -- your move is {self.move1} and computer move is {self.move2}")
            return self.helper()
        
        elif self.move1=='p' and self.move2=='s':
            self.score2+=1
            print(f"You Lost -- your move is {self.move1} and computer move is {self.move2}")
            return self.helper()
        
        elif self.move1=='s' and self.move2=='r':
            self.score2+=1
            print(f"You Lost -- your move is {self.move1} and computer move is {self.move2}")
            return self.helper()
        
        elif self.move1==self.move2:
            print(f"Its a draw -- your move is {self.move1} and computer move is {self.move2}")
            self.helper()
            
        else:
            print("Invalid Input")
            return self.helper()
    
    def choose(self):
        print("Press 1 to continue")
        print("Press 2 to quit")
        choice=input("Enter your choice: ")
        if choice==1:
            return 1
        elif choice==2:
            return -1
        
g=Game()
















