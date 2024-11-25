def generate_permutations(arr):
    """
    주어진 배열의 모든 순열을 생성하는 함수

    Args:
        arr: 순열을 생성할 배열
    Returns:
        모든 가능한 순열의 리스트
    """

    def permute(elements):
        if len(elements) <= 1:
            return [elements]

        result = []
        for i, current in enumerate(elements):
            remaining = elements[:i] + elements[i + 1:]
            for sub_permutation in permute(remaining):
                result.append([current] + sub_permutation)

        return result

    return permute(arr)


def main():
    try:
        # 사용자로부터 배열 형태의 입력 받기
        print("배열을 입력하세요 (예: [1, 2, 3]):")
        input_str = input().strip()

        # 입력 문자열에서 대괄호 제거하고 숫자 추출
        numbers = list(map(int, input_str.strip('[]').split(',')))

        # 중복된 숫자 확인
        if len(numbers) != len(set(numbers)):
            print("중복된 숫자가 있습니다. 모든 숫자는 서로 달라야 합니다.")
            return

        # 순열 생성
        result = generate_permutations(numbers)

        # 결과 출력
        for perm in result:
            print(perm)

    except ValueError:
        print("올바른 형식으로 입력해주세요. 예: [1, 2, 3]")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")


if __name__ == "__main__":
    main()