'''
1. 문자열 팰린드롬 여부 확인
문제 설명:
주어진 문자열이 팰린드롬인지 확인하는 프로그램을 작성하세요.
팰린드롬은 앞으로 읽으나 뒤로 읽으나 같은 문자열을 의미합니다.

요구사항:
1. 문자열의 처음과 끝에서부터 중앙까지 이동하며, 각 위치의 문자가 서로 일치하는지 확인합니다.
2. 문자열의 길이가 홀수인 경우 중앙의 문자는 확인하지 않아도 됩니다.
'''
word = input()
wordLength = len(word)
is_palindrome = True

for i in range(wordLength // 2):
    if word[i] != word[wordLength - 1 - i]:
        is_palindrome = False
        break
print(is_palindrome)