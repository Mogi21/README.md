# Connect-N AI Engine

A generalized, high-performance Connect-N engine featuring a custom adversarial AI agent. 

Unlike traditional Connect-4, this engine supports dynamic grid sizes and variable win conditions (e.g., Connect-5 on a 7x7 grid). The project demonstrates standard software engineering patterns and classical AI game theory algorithms, packaged in an interactive notebook format.

## Features
* **Variable Game State Engine:** Decoupled architecture allowing for dynamic board scaling and rule adjustments.
* **Minimax with Alpha-Beta Pruning:** The primary AI agent uses a recursive minimax algorithm optimized with alpha-beta pruning to drastically reduce the search space.
* **Adaptive Search Depth:** The agent scales its search depth dynamically based on board size and the current turn phase (early game vs. late game) to ensure moves execute efficiently.
* **Positional Heuristics:** Includes a lightweight heuristic evaluation function prioritizing center control and immediate threat neutralization.

## How to Run

This project is built as an interactive Jupyter Notebook. You can run the engine directly in your browser using Google Colab.

1. Open the `.ipynb` file in this repository.
2. Click the **"Open in Colab"** badge (if using a browser extension) or import the notebook into Google Colab.
3. Run the cells sequentially to initialize the engine, load the agents, and start a match.
4. Modify the `ConnectNEngine` parameters in the final cell to test different board sizes and win conditions.

## Agent Types
* **Minimax Agent:** The core AI that uses alpha-beta pruning and heuristics.
* **Random Agent:** A baseline opponent for rapid testing.
* **Human Agent:** Allows manual play against the AI via standard CLI inputs.

## Future Improvements
* Implementation of Transposition Tables (Zobrist Hashing) for memory caching.
* Expanding test coverage for core engine logic.
