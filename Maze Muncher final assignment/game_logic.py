def try_move(maze, row, col, direction):
    if direction == 'up':
        new_row = row - 1
    elif direction == 'down':
        new_row = row + 1
    elif direction == 'left':
        new_col = col - 1
    elif direction == 'right':
        new_col = col + 1

    if new_row < 0 or new_row >= len(maze):
        return row, col
    if new_col < 0 or new_col >= len(maze[new_row]):
        return row, col

    if maze [new_row][new_col] == '#':
        return row, col
    return new_row, new_col

def collect_dot_if_present(maze, row, col):
    if maze[row][col] == 'o':
        row_text = maze[row]
        new_row_text = row_text[:col] + '.' + row_text[col+1:]
        maze[row] = new_row_text
        return True
    return False

def count_remaining_dots(maze):
    total = 0
    for row in maze:
        total += row.count('o')
    return total

def move_enemy_toward_player(enemy_row, enemy_col, player_row, player_col, maze):
    new_row, new_col = enemy_row, enemy_col

    if player_row < enemy_row:
        new_row -= 1
    elif player_row > enemy_row:
        new_row += 1
    elif player_col < enemy_col:
        new_col -= 1
    elif player_col > enemy_col:
        new_col += 1

    if maze[new_row][new_col] == '#':
        return enemy_row, enemy_col
    return new_row, new_col


def check_collision(player_row, player_col, enemy_row, enemy_col):
    return player_row == enemy_row and player_col == enemy_col

def check_win(maze):
    return count_remaining_dots(maze) == 0
