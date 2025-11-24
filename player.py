def guess():
    while True:
        guess_num = input("수를 입력하세요.\n입력: ")
        
        if len(guess_num) == 5:
            return guess_num
        else:
            print("5자리 수를 입력하세요!")
            continue

