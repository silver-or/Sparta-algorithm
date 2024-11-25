def calculate_postfix(expression):
    """
    후위 표기법으로 된 수식을 계산하는 함수

    Args:
        expression (str): 공백으로 구분된 후위 표기법 수식

    Returns:
        int: 계산 결과

    Raises:
        ValueError: 잘못된 수식이 입력된 경우
    """
    # 연산자 함수 매핑
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y  # 정수 나눗셈 사용
    }

    stack = []
    tokens = expression.strip().split()

    try:
        for token in tokens:
            if token in operators:  # 연산자인 경우
                if len(stack) < 2:
                    raise ValueError("잘못된 수식: 연산자에 비해 피연산자가 부족합니다")

                # 스택에서 피연산자 두 개를 꺼냄 (순서 주의)
                b = stack.pop()
                a = stack.pop()

                # 연산 수행 및 결과를 스택에 저장
                result = operators[token](a, b)
                stack.append(result)

            else:  # 숫자인 경우
                try:
                    num = int(token)
                    stack.append(num)
                except ValueError:
                    raise ValueError(f"잘못된 토큰입니다: {token}")

        if len(stack) != 1:
            raise ValueError("잘못된 수식: 연산자가 부족합니다")

        return stack[0]

    except ZeroDivisionError:
        raise ValueError("0으로 나눌 수 없습니다")

if __name__ == "__main__":
    print(calculate_postfix(input()))