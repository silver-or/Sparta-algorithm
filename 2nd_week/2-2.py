def longest_substring_without_repeating(s: str) -> int:
    """
    중복 문자가 없는 가장 긴 부분 문자열의 길이를 반환하는 함수

    Args:
        s (str): 입력 문자열

    Returns:
        int: 중복 문자가 없는 가장 긴 부분 문자열의 길이
    """
    # 문자의 최근 등장 위치를 저장할 해시테이블
    char_position = {}

    max_length = 0  # 최대 길이를 저장할 변수
    start = 0  # 현재 부분 문자열의 시작 위치

    for current_pos, char in enumerate(s):
        # 문자가 이미 등장했고, 그 위치가 현재 부분 문자열의 시작 위치보다 뒤에 있는 경우
        if char in char_position and char_position[char] >= start:
            # 시작 위치를 중복된 문자의 다음 위치로 업데이트
            start = char_position[char] + 1
        else:
            # 현재 부분 문자열의 길이를 계산하고 최대 길이 업데이트
            current_length = current_pos - start + 1
            max_length = max(max_length, current_length)

        # 현재 문자의 위치를 해시테이블에 저장
        char_position[char] = current_pos

    return max_length


def process_input() -> str:
    return input().strip()

if __name__ == "__main__":
    s = process_input()

    # 결과 계산
    result = longest_substring_without_repeating(s)

    # 결과 출력
    print(result)