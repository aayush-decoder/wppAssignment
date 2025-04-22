import random as rn

class Game:
    options = ['stone', 'paper', 'scissor']
    resultsList = []

    def __init__(self, rounds):
        self.rounds = rounds

    @staticmethod
    def computer_turn():
        turn = rn.randint(0, 2)
        return turn
    
    def game_logic(self, user_choice, comp_choice):
        if user_choice == comp_choice:
            return 0 
        elif (user_choice == 0 and comp_choice == 2) or \
             (user_choice == 1 and comp_choice == 0) or \
             (user_choice == 2 and comp_choice == 1):
            return -1 
        else:
            return 1  
    
    def newRound(self):
        print("Current Score:", self.resultsList)
        user_choice = input("Stone, Paper, Scissor: ").strip().lower()

        if user_choice not in self.options:
            print("Please enter a valid choice (stone, paper, scissor).")
            return

        user_choice = self.options.index(user_choice)
        computer_choice = self.computer_turn()

        print(f"Computer chose: {self.options[computer_choice]}")
        
        result = self.game_logic(user_choice, computer_choice)
        self.resultsList.append(result)
        self.displayScoreBoard()

    def displayScoreBoard(self):
        print(f"Computer: {self.resultsList.count(1)}\t| User: {self.resultsList.count(-1)}\n")

    def declareWinner(self):
        total = sum(self.resultsList)
        if total < 0:
            print("User Won!")
        elif total == 0:
            print("Draw!!")
        else:
            print("Computer Won!")

    def start(self):
        for _ in range(self.rounds):
            self.newRound()
        self.declareWinner()

n = int(input("Enter the number of rounds to be played: "))
game1 = Game(n)
game1.start()
