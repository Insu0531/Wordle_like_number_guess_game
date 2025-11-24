from randomAI import number_generator
from player import guess
from logic import compare_num
from logic import score

print("*간단한 수 맞히기 게임*\n")
answer = number_generator(5)

while True:
    player_guess = guess()
    if player_guess == 'admin':
        print(answer)
        continue
    print(score(player_guess, answer))

    if compare_num(player_guess, answer):
        print("**** 정답입니다! ****")
        break
    else:
        continue

    

