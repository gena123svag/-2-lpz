from collections import deque

maze = [
    "S . . # $",
    ". # $ . .",
    ". . # # .",
    ". $ . . E"
]

# Преобразуем в список списков
grid = [list(row.replace(' ', '')) for row in maze]
rows, cols = len(grid), len(grid[0])

def bfs():
    # найти старт
    start = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
                break
    # BFS с сохранением пути
    queue = deque([(start[0], start[1], [])])
    visited = set()
    visited.add((start[0], start[1]))
    while queue:
        r, c, path = queue.popleft()
        if grid[r][c] == 'E':
            return path + [(r,c)]
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
                if grid[nr][nc] != '#':
                    visited.add((nr,nc))
                    queue.append((nr, nc, path + [(r,c)]))
    return None

path = bfs()
print("Путь:", path)
# подсчёт сокровищ на пути (упрощённо)
treasures = 0
for r,c in path:
    if grid[r][c] == '$':
        treasures += 1
print("Сокровищ собрано:", treasures)