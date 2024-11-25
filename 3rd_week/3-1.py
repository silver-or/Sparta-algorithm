from collections import deque


def find_maze_path(maze):
    # 미로의 크기
    N = len(maze)
    M = len(maze[0])

    # 방문 여부를 저장할 2차원 리스트
    visited = [[False] * M for _ in range(N)]

    # 거리를 저장할 2차원 리스트
    distance = [[0] * M for _ in range(N)]

    # 상하좌우 이동을 위한 방향 벡터
    dx = [-1, 1, 0, 0]  # 상하
    dy = [0, 0, -1, 1]  # 좌우

    # BFS 구현
    queue = deque([(0, 0)])  # 시작점 (0, 0)
    visited[0][0] = True
    distance[0][0] = 1  # 시작점도 카운트

    while queue:
        x, y = queue.popleft()

        # 출구에 도달했다면 거리 반환
        if x == N - 1 and y == M - 1:
            return distance[x][y]

        # 네 방향으로 이동 시도
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 범위 내에 있고
            if 0 <= nx < N and 0 <= ny < M:
                # 아직 방문하지 않았으며 이동 가능한 칸이라면
                if not visited[nx][ny] and maze[nx][ny] == '1':
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1

    # 출구까지 도달할 수 없는 경우
    return -1


def main():
    # 미로 입력 받기
    maze = []
    while True:
        try:
            line = input().strip()
            if not line:  # 빈 줄이 입력되면 입력 종료
                break
            maze.append(line)
        except EOFError:  # EOF(입력 종료)가 감지되면 입력 종료
            break

    # 미로가 비어있는 경우
    if not maze:
        print("미로가 입력되지 않았습니다.")
        return

    # 모든 행의 길이가 동일한지 확인
    if not all(len(row) == len(maze[0]) for row in maze):
        print("잘못된 미로 형식입니다. 모든 행의 길이가 같아야 합니다.")
        return

    # 시작점과 도착점이 1인지 확인
    if maze[0][0] != '1' or maze[-1][-1] != '1':
        print("시작점과 도착점은 1이어야 합니다.")
        return

    # 최단 경로 찾기
    result = find_maze_path(maze)

    # 결과 출력
    if result == -1:
        print("미로를 탈출할 수 없습니다.")
    else:
        print(result)


if __name__ == "__main__":
    main()