from src.TRUE.NAME1 import TrueOrFalse
from src.TRUE.Gamestatus import GameStatus


#t.open_file()
file = input('File location: ') # You can choose path to your <file>.csv
errors = int(input('Count of errors: '))
t = TrueOrFalse(file, errors)
t.open_file()
while t.game_status == GameStatus.IN_PROGRESS:
    print(t.current_question()) 
    answer = input('Your answer Yes or No: ')
    t.let_answer(answer) # trying your answer
    t.next_question()
    if t.game_status == GameStatus.WIN:
        print('congratulations you WON!')
    elif t.game_status == GameStatus.LOSE:
        print('sorry you LOST')


#../data/Questions.csv my path to file






