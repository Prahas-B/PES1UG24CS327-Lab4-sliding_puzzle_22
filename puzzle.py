import random


class Puzzle:
    def __init__(self, size=4):
        self.size = size
        self.board = self.make_board()

    def make_board(self):
        # Start with the solved board
        tiles = list(range(1, self.size * self.size)) + [0]

        board = [
            tiles[r * self.size:(r + 1) * self.size]
            for r in range(self.size)
        ]

        # Scramble using legal blank-tile moves.
        previous_move = None
        opposite = {
            "w": "s",
            "s": "w",
            "a": "d",
            "d": "a"
        }

        scramble_moves = self.size * self.size * 20

        for _ in range(scramble_moves):
            r, c = next(
                (r, c)
                for r in range(self.size)
                for c in range(self.size)
                if board[r][c] == 0
            )

            legal_moves = []

            if r > 0:
                legal_moves.append("w")

            if r < self.size - 1:
                legal_moves.append("s")

            if c > 0:
                legal_moves.append("a")

            if c < self.size - 1:
                legal_moves.append("d")

            # Avoid immediately undoing the previous move.
            if previous_move is not None:
                legal_moves = [
                    move
                    for move in legal_moves
                    if move != opposite[previous_move]
                ]

            move = random.choice(legal_moves)

            dr, dc = {
                "w": (-1, 0),
                "s": (1, 0),
                "a": (0, -1),
                "d": (0, 1)
            }[move]

            nr, nc = r + dr, c + dc

            board[r][c], board[nr][nc] = (
                board[nr][nc],
                board[r][c]
            )

            previous_move = move

        # A freshly scrambled board must not be solved.
        solved_board = [
            list(range(r * self.size + 1, (r + 1) * self.size))
            for r in range(self.size)
        ]
        solved_board[-1][-1] = 0

        if board == solved_board:
            # Make one legal move from the solved state.
            board[-1][-1], board[-1][-2] = (
                board[-1][-2],
                board[-1][-1]
            )

        return board

    def blank_pos(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == 0:
                    return r, c

    def move(self, direction):
        r, c = self.blank_pos()

        dr, dc = {
            "w": (-1, 0),
            "s": (1, 0),
            "a": (0, -1),
            "d": (0, 1)
        }[direction]

        nr, nc = r + dr, c + dc

        if not (0 <= nr < self.size and 0 <= nc < self.size):
            return False

        self.board[r][c], self.board[nr][nc] = (
            self.board[nr][nc],
            self.board[r][c]
        )

        return True

    def is_solved(self):
        solved_board = [
            list(range(r * self.size + 1, (r + 1) * self.size))
            for r in range(self.size)
        ]

        solved_board[-1][-1] = 0

        return self.board == solved_board

    def solved(self):
        return self.is_solved()
