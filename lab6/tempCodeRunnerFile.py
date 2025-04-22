import random as rn

class Game:
    # rounds = int(input("Number of rounds: "))
    options = ['stone', 'paper', 'scissor']
    resultsList = []

    def __init__(self, rounds):
        self.rounds = rounds

    @staticmethod
    def computer_turn():
        return rn.randint(0, 2)
    
    def game_logic(self, query1, query2):
        if query1 == query2:
            return 0
        elif (query1 == 0 and query2 == 1):
            return 1 
        elif (query1 == 1 and query2 == 2):
            return 1
        elif (query1 == 2 and query2 == 0):
            return 1
        else:
            return -1
    
    def newRound(self):
        print(self.resultsList)
        user_choice = input("Stone, paper, scisssor: ")
        try:
            user_choice = self.options.index(user_choice.lower())
        except:
            print("Please enter valid name")
        computer_choice = self.computer_turn()

        result = self.game_logic(user_choice, computer_choice)
        # print("user choice, comp choice", user_choice, computer_choice)
        self.resultsList.append(result)
        # print(f"Computer chose: {self.options[computer_choice]}")
        self.displayScoreBoard();


    def displayScoreBoard(self):
        print(f"Computer: {self.resultsList.count(1)}\t|User: {self.resultsList.count(-1)}\n")

    def declareWinner(self):
        param = sum(self.resultsList)
        if param < 0:
            print("User Won!")
        elif param == 0:
            print("Draw!")
        else:
            print("Computer Won!")


    def start(self):
        for i in range(self.rounds):
            self.newRound()
        self.declareWinner()

n = int(input("ENter the number of rounds to be played: "))
game1 = Game(n)
game1.start()