import time
from puzzle import Puzzle


class SlidingPuzzle:
    def __init__(self):
        self.size = 4
        self.puzzle = Puzzle(self.size)
        self.moves = 0
        self.started = time.monotonic()
        self.completed = False

    def display(self):
        print()
        for row in self.puzzle.board:
            print(" ".join(f"{x or ' ':>2}" for x in row))
        print(
            "Moves:",
            self.moves,
            " Time:",
            int(time.monotonic() - self.started),
            "s"
        )

    def run(self):
        print("Sliding Puzzle — W/A/S/D moves the tile into the blank. Q quits.")

        while True:
            self.display()

            if self.completed:
                return

            key = input("> ").strip().lower()

            if key == "q":
                return

            if key not in "wasd":
                print("Use W/A/S/D.")
                continue

            if self.completed:
                continue

            if self.puzzle.move(key):
                self.moves += 1

                # Check immediately after every successful move
                if self.puzzle.is_solved():
                    elapsed = int(time.monotonic() - self.started)
                    self.completed = True

                    print()
                    print("🎉 Congratulations! You solved the puzzle!")
                    print("Total moves:", self.moves)
                    print("Time:", elapsed, "s")
                    return
            else:
                print("That move is not possible.")
