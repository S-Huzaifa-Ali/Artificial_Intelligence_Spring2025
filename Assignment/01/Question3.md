# Q3


## Agent Description:

The agent is an AI-powered chess program designed to play against human opponents. It evaluates the current board states, computes possible moves, and selects the best move based on pre-trained strategies.

## Characterization of its Environment:

- **Perceivability:** Yes. The agent has complete information about the chessboard, including the positions of all pieces at any given time.
- **Deterministic:** Yes. Chess is deterministic because each move has a known outcome with no randomness.
- **Episodic:** No. The game is sequential, making it non-episodic.
- **Static:** Yes. The board remains unchanged until a move is made.  
  The board state changes when a move is executed.
- **Continuous:** No. Chess is a discrete environment with a finite set of legal moves at any given time.

## Best Agent Architecture:

1. **Search Algorithms:** Minimax with Alpha-Beta Pruning for evaluating moves and selecting the best one by exploring future states.
2. **Heuristic Evaluation Functions:** These functions assign scores to board positions based on factors like material advantage, piece activity, king safety, etc.
3. **Reinforcement Learning:** Neural networks (Alpha Zero) to learn strategies from self-play.
