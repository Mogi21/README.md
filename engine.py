import math
import random

# ---------------------------------------------------------
# 1. THE ADVANCED MINIMAX AI (Your refactored player_ai3)
# ---------------------------------------------------------
def minimax_agent(board_state: List[List[int]], valid_moves: List[int], player_id: int, state_memory: Any) -> Tuple[int, Any]:
    if state_memory is None:
        grid_size = len(board_state)
        target = min(5, grid_size) if sum(len(col) for col in board_state) < 3 else 4
        state_memory = {'turn_count': 0, 'target': target}
    
    state_memory['turn_count'] += 1
    target = state_memory['target']
    opponent = 3 - player_id
    
    # 1. Immediate Win / Block
    for move in valid_moves:
        if _simulate_and_check(board_state, move, player_id, target): return move, state_memory
    for move in valid_moves:
        if _simulate_and_check(board_state, move, opponent, target): return move, state_memory
            
    # 2. Opening strategy
    if state_memory['turn_count'] <= 2:
        center = len(board_state) // 2
        return (center if center in valid_moves else valid_moves[0]), state_memory
    
    # 3. Minimax Deep Search
    depth = 6 if len(board_state) <= 4 else 4
    best_score = -math.inf
    best_move = valid_moves[0]
    
    for move in valid_moves:
        new_board = _apply_move(board_state, move, player_id)
        score = _minimax(new_board, depth - 1, False, player_id, opponent, -math.inf, math.inf, target)
        if score > best_score:
            best_score = score
            best_move = move
            
    return best_move, state_memory

def _minimax(board: List[List[int]], depth: int, maximizing: bool, player: int, opponent: int, alpha: float, beta: float, target: int) -> float:
    if _detect_sequence(board, target, player): return 1000 + depth
    if _detect_sequence(board, target, opponent): return -1000 - depth
    
    moves = [i for i, col in enumerate(board) if len(col) < len(board)]
    if depth == 0 or not moves:
        score = 0
        center = len(board) // 2
        for c, col in enumerate(board):
            for val in col:
                if val == player: score += (5 - abs(c - center))
                elif val == opponent: score -= (5 - abs(c - center))
        return score
    
    if maximizing:
        max_eval = -math.inf
        for move in moves:
            eval_score = _minimax(_apply_move(board, move, player), depth - 1, False, player, opponent, alpha, beta, target)
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha: break
        return max_eval
    else:
        min_eval = math.inf
        for move in moves:
            eval_score = _minimax(_apply_move(board, move, opponent), depth - 1, True, player, opponent, alpha, beta, target)
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if beta <= alpha: break
        return min_eval

def _apply_move(board: List[List[int]], move: int, player: int) -> List[List[int]]:
    new_board = [col.copy() for col in board]
    new_board[move].append(player)
    return new_board

def _simulate_and_check(board: List[List[int]], move: int, player: int, target: int) -> bool:
    return _detect_sequence(_apply_move(board, move, player), target, player)

def _detect_sequence(board: List[List[int]], target: int, player: int) -> bool:
    n_cols = len(board)
    for c in range(n_cols):
        for r in range(len(board[c])):
            if board[c][r] != player: continue
            for dc, dr in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                streak = 1
                nc, nr = c + dc, r + dr
                while 0 <= nc < n_cols and 0 <= nr < len(board[nc]) and board[nc][nr] == player:
                    streak += 1
                    if streak >= target: return True
                    nc += dc
                    nr += dr
    return False


# ---------------------------------------------------------
# 2. RANDOM AGENT (For quick testing)
# ---------------------------------------------------------
def random_agent(board_state: List[List[int]], valid_moves: List[int], player_id: int, state_memory: Any) -> Tuple[int, Any]:
    return random.choice(valid_moves), state_memory


# ---------------------------------------------------------
# 3. HUMAN AGENT (If you want to play manually)
# ---------------------------------------------------------
def human_agent(board_state: List[List[int]], valid_moves: List[int], player_id: int, state_memory: Any) -> Tuple[int, Any]:
    while True:
        try:
            move = int(input(f"Choose a column {valid_moves}: "))
            if move in valid_moves:
                return move, state_memory
            print("Invalid column. Please choose from the available options.")
        except ValueError:
            print("Invalid input. Please enter a number.")
