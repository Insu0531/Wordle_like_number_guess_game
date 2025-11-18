import random

def number_generator(n):
    answer = str(random.randint(1,9))
    while len(answer) != n:
        num = random.randint(0,9)
        answer += str(num)

    return answer

