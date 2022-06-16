from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)
        self.reset()

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    @property
    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value
        return total

    @classmethod
    def run(cls):
        count = 0
        runner = cls()
        while True:

            print("Round {}\n".format(runner.round))

            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer:
                print("Congrats, you can add like a 5 year old...")
                runner.wins += 1
                count += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
                count = 0
            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            runner.round += 1

            if count == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break

            prompt = input("Would you like to play again?[Y/n]: ")

            if prompt.lower() == 'y' or prompt == '':
                continue
            else:
                break
