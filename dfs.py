def find_next(coordinates, maze):
    next_coordinates = []
    if coordinates[0] - 1 >= 0 and maze[coordinates[0] - 1][coordinates[1]] != 1:
        next_coordinates.append((coordinates[0] - 1, coordinates[1]))
    if coordinates[0] + 1 < len(maze) and maze[coordinates[0] + 1][coordinates[1]] != 1:
        next_coordinates.append((coordinates[0] + 1, coordinates[1]))
    if coordinates[1] + 1 < len(maze[0]) and maze[coordinates[0]][coordinates[1] + 1] != 1:
        next_coordinates.append((coordinates[0], coordinates[1] + 1))
    if coordinates[1] - 1 >= 0 and maze[coordinates[0]][coordinates[1] - 1] != 1:
        next_coordinates.append((coordinates[0], coordinates[1] - 1))
    return next_coordinates


def dfs(maze, stack, visited):
    start = (0, 0)
    goal = (3, 2)
    stack.append(start)
    while stack:
        print("\n")
        n = stack.pop()
        print(f"Popping {n}")
        print(f"Is {n} my goal?")
        if n == goal:
            print("DONE!")
            return
        print(f"No.")
        next_steps = find_next(n, maze)
        print(f"Next Steps: {next_steps}")
        for x in next_steps:
            print(f"Evaluating {x}")
            if x in visited:
                print(f"{x} already visited, skipping...")
                continue
            visited.add(x)
            stack.append(x)
            print(f"Visited nodes: {visited}")
            print(f"Stack: {stack}")

def main():
    stack = []
    visited = set()
    maze = [[0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0]]
    dfs(maze, stack, visited)

if __name__ == "__main__":
    main()
