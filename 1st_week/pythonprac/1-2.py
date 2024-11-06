'''
2. 짝수와 홀수 구분하기
문제 설명:
주어진 숫자가 짝수인지 홀수인지를 판별하는 파이썬 프로그램을 작성해보세요.


요구사항:
1. 조건문(if)과 사용자로부터 숫자를 입력받는 기능을 포함해야 합니다.
2. 입력된 숫자가 짝수이면 "짝수입니다"를, 홀수이면 "홀수입니다"를 출력해야 합니다.
'''
num = int(input())

if num % 2 == 0:
    print('짝수입니다')
else:
    print('홀수입니다')