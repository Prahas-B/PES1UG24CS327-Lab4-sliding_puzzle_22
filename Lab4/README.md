# Scenario 22 — Sliding Puzzle (Lab 4: VibeCoding)

A terminal-based sliding puzzle written in Python. The player slides tiles into the blank space to restore the solved arrangement. This repo contains my fixed and extended version of the code originally provided in `SETAPESU26/22_sliding_puzzle`, completed using an LLM (ChatGPT) as a coding assistant.

**Name:** `<Prahas Bodanapati>`
**SRN:** `<PES1UG24CS327>`
**Section:** `<5F>`

---

## Project Structure

```
22_sliding_puzzle/
├── README.md
├── requirements.txt
├── main.py        # entry point
├── game.py        # interaction loop, timer, move tracking
├── puzzle.py      # board representation and movement rules
└── Lab-4/
    ├── before.mp4         # 10-second gameplay before changes
    ├── after.mp4          # 10-second gameplay after changes
    └── chat_history.pdf   # full LLM chat history
```

## How to Run

Requires Python 3.8+ and no external dependencies.

```bash
git clone https://github.com/<your-username>/22_sliding_puzzle.git
cd 22_sliding_puzzle
python main.py
```

## How to Play

1. Choose a board size when prompted: **3x3, 4x4, or 5x5**.
2. The board is displayed with one blank space.
3. Enter the number of the tile you want to slide into the blank. Only tiles directly next to the blank (up, down, left, right) can move.
4. The game shows your move count and elapsed time as you play.
5. When the tiles are in order, the game announces your win with the total moves and time, then ends.
6. Type the quit command at any time to exit.

---

## Original Problems and Fixes

### Task 1 — Guarantee solvable starting states
**Problem:** The original code created the starting board with a random shuffle. Roughly half of all random permutations of a sliding puzzle are unreachable from the solved state (parity problem), so some games were impossible to win.

**Fix:** The board now starts from the solved arrangement and is scrambled by applying many random *legal* blank-space moves (without immediately undoing the previous move). Every generated board is therefore reachable from the solved state. A freshly generated board is also never already solved.

### Task 2 — Complete puzzle lifecycle
**Problem:** The game did not detect when the puzzle was solved.

**Fix:** Added solved-state detection after each valid move. On completion, the game prints a congratulations message with total moves and time and ends cleanly. Commands entered after completion cannot change the board or the move count.

### Task 3 — Size, timer, and move modes
**Problem:** Only one board size was supported, and session values could be reset when the board was recreated.

**Fix:** Added 3x3, 4x4, and 5x5 modes with input validation. Moves and elapsed time are tracked consistently for every size, and recreating the board does not accidentally reset session values.

### Task 4 — Valid-action feedback
**Problem:** The game could report a successful slide, and count a move, even when no tile actually moved.

**Fix:** A move now returns whether it succeeded. Success feedback and the move counter update only when a tile actually slides into the blank. Invalid moves (non-adjacent tile, out-of-range number, bad input) show an error message and do not change the move count.

---

## Testing Performed

| Test | Result |
|------|--------|
| Generated many fresh boards for 3x3, 4x4, 5x5 and checked solvability | Pass |
| Confirmed fresh boards are never already solved | Pass |
| Solved a small board with known moves and verified win detection | Pass |
| Attempted impossible moves (non-adjacent, out of range) | Rejected, no move counted |
| Verified move count increases only on valid moves | Pass |
| Verified timer behaviour across all sizes | Pass |
| Tested invalid commands (letters, empty input, negative numbers) | Handled gracefully |
| Tested quit command | Exits cleanly |
| Tested that no commands change state after the game is won | Pass |

## Constraints Followed

- All game state is kept in memory. No CSV, JSON, SQLite, or other persistence.
- No unnecessary external dependencies.
- The original project structure was kept; code remains modular across `main.py`, `game.py`, and `puzzle.py`.

## LLM Usage

I used ChatGPT as a coding assistant. I first asked it to explain the existing code, then fixed and extended it one task at a time, testing the result after each step. The complete chat history is included in `Lab-4/chat_history.pdf`.

**Chat link:** `<paste your ChatGPT share link here>`

## Deliverables

- [x] Video of gameplay **before** changes (`Lab-4/before.mp4`)
- [x] Video of gameplay **after** changes (`Lab-4/after.mp4`)
- [x] Updated code
- [x] Complete LLM chat history (`Lab-4/chat_history.pdf`)
