import time
from puzzle import Puzzle


class SlidingPuzzle:
    def __init__(self):
        self.size = self.get_board_size()

        self.puzzle = Puzzle(self.size)
        self.moves = 0
        self.started = time.monotonic()
        self.completed = False

    def get_board_size(self):
        while True:
            print("Select board size:")
            print("1. 3x3")
            print("2. 4x4")
            print("3. 5x5")

            choice = input("Enter choice (1-3): ").strip()

            if choice == "1":
                return 3
            elif choice == "2":
                return 4
            elif choice == "3":
                return 5
            else:
                print("Invalid choice. Please enter 1, 2, or 3.\n")

    def display(self):
        print()

        for row in self.puzzle.board:
            print(" ".join(f"{x or ' ':>2}" for x in row))

        elapsed = int(time.monotonic() - self.started)

        print("Moves:", self.moves, " Time:", elapsed, "s")

    def run(self):
        print(
            "\nSliding Puzzle — "
            "W/A/S/D moves the tile into the blank. Q quits."
        )

        while True:
            self.display()

            if self.completed:
                return

            key = input("> ").strip().lower()

            if key == "q":
                return

            # Bad input
            if key not in "wasd":
                print("Invalid input. Please use W, A, S, or D.")
                continue

            # Attempt the move
            if self.puzzle.move(key):
                # Only successful moves reach here
                self.moves += 1
                print("Move successful!")

                if self.puzzle.is_solved():
                    elapsed = int(time.monotonic() - self.started)

                    self.completed = True

                    print()
                    print("Congratulations! You solved the puzzle!")
                    print("Total moves:", self.moves)
                    print("Time:", elapsed, "s")

                    return
            else:
                # Invalid move: board edge / no adjacent tile
                print("Invalid move. No tile can slide in that direction.")
