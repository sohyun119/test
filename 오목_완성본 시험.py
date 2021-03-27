def getWinner(play):
    num1=0
    num2=0
    for i in range(13):
        for j in range(13):
            if play[i][j]=='B':
                num1+=1
            elif play[i][j]=='W':
                num2+=1
    p1=0
    p2=0
    for i in range(13):
        for j in range(9):
            horizontal_1=horizontal_2=0
            vertical_1=vertical_2=0
            left_diagonal_1=left_diagonal_2=0
            right_diagonal_1=right_diagonal_2=0
            for k in range(5):
                #가로 판별
                if play[i][j+k]=='B':
                    horizontal_1+=1
                elif play[i][j+k]=='W':
                    horizontal_2+=1
                #세로 판별
                if play[j+k][i]=='B':
                    vertical_1+=1
                elif play[j+k][i]=='W':
                    vertical_2+=1
                #왼쪽 위 시작 대각선 판별
                if play[j+k][j+k]=='B':
                    left_diagonal_1+=1
                elif play[j+k][j+k]=='W':
                    left_diagonal_2+=1
                #오른쪽 위 시작 대각선 판별
                if play[j+k][12-j-k]=='B':
                    right_diagonal_1+=1
                elif play[j+k][12-j-k]=='W':
                    right_diagonal_2+=1

            if horizontal_1==5 or vertical_1==5 or left_diagonal_1==5 or right_diagonal_1==5:
                p1=1
            elif horizontal_2==5 or vertical_2==5 or left_diagonal_2==5 or right_diagonal_2==5:
                p2=1



    if (p1==1 and p2==1) or (num2>num1) or (num2+2<=num1):
        return 'X'
    elif p1==1:
        return 'B'
    elif p2==1:
        return 'W'
    else :
        return 'None'
