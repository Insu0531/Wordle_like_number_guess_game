def guess(n): # n은 5자리수
    while True:
        guess_num = input("수를 입력하세요.\n입력: ")
        
        if len(guess_num) == n:
            return guess_num

