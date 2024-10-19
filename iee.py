from collections import deque

# Helper function to parse the input string


def parse_box(box_str):
    red = int(box_str[0])  # Number of red marbles
    black = int(box_str[2])  # Number of black marbles
    return red, black

# Helper function to check if a state is valid


def is_valid_state(red_left, black_left, red_right, black_right):
    return red_left > black_left and red_right > black_right


def min_moves_to_transfer(left_box, right_box, max_transfer_limit):
    # Parse the left and right box strings
    red_left, black_left = parse_box(left_box)
    red_right, black_right = parse_box(right_box)

    # Edge case: If left box already violates the constraint
    if not is_valid_state(red_left, black_left, red_right, black_right):
        return 0

    # BFS setup: Queue contains (red_left, black_left, red_right, black_right, moves)
    queue = deque([(red_left, black_left, red_right, black_right, 0)])
    # To avoid revisiting states
    visited = set([(red_left, black_left, red_right, black_right)])

    while queue:
        r_left, b_left, r_right, b_right, moves = queue.popleft()

        # Check if all marbles are moved to the right box
        if r_left == 0 and b_left == 0:
            return moves

        # Explore possible moves
        for r_move in range(0, max_transfer_limit + 1):
            # Ensure total moved <= max_transfer_limit
            for b_move in range(0, max_transfer_limit + 1 - r_move):
                if r_move == 0 and b_move == 0:
                    continue  # We must move at least one marble

                # Move marbles from left to right
                new_r_left = r_left - r_move
                new_b_left = b_left - b_move
                new_r_right = r_right + r_move
                new_b_right = b_right + b_move

                # Check if this new state is valid
                if 0 <= new_r_left <= r_left and 0 <= new_b_left <= b_left:
                    if is_valid_state(new_r_left, new_b_left, new_r_right, new_b_right):
                        new_state = (new_r_left, new_b_left,
                                     new_r_right, new_b_right)
                        if new_state not in visited:
                            visited.add(new_state)
                            queue.append(
                                (new_r_left, new_b_left, new_r_right, new_b_right, moves + 1))

                # Move marbles from right to left
                new_r_left = r_left + r_move
                new_b_left = b_left + b_move
                new_r_right = r_right - r_move
                new_b_right = b_right - b_move

                # Check if this new state is valid
                if 0 <= new_r_right <= r_right and 0 <= new_b_right <= b_right:
                    if is_valid_state(new_r_left, new_b_left, new_r_right, new_b_right):
                        new_state = (new_r_left, new_b_left,
                                     new_r_right, new_b_right)
                        if new_state not in visited:
                            visited.add(new_state)
                            queue.append(
                                (new_r_left, new_b_left, new_r_right, new_b_right, moves + 1))

    # If no solution is found, return 0
    return 0


# Example usage
left_box = "2R2B"
right_box = "0R0B"
max_transfer_limit = 2

result = min_moves_to_transfer(left_box, right_box, max_transfer_limit)
print(result)
