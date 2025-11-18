def score(guess, ans):
    score = ''
    for i in range(len(guess)):
        if guess[i] == ans[i]:
            score += '🟩'
        elif guess[i] in ans:
            score += '🟨'
        else:
            score += '🟥'
    return score

def compare_num(guess, ans):
    if guess == ans:
        return 1
    else:
        return 0




    