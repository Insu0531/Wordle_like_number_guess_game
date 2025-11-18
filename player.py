def guess(n): # n은 main에서 입력받은 정답의 자리수
    while True:
        guess_num = input("수를 입력하세요.\n입력: ")
        
        if len(guess_num) == n:
            return guess_num
        else:
            print(f'* {n}자리수를 입력하셔야 합니다!')
            continue

