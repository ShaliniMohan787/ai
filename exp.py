import random

# Expectimax for a simple dice vs safe option game

def expectimax(state, depth, player):
    """
    state: current node ("root", "chance", or terminal value)
    depth: depth limit
    player: "max" or "chance"
    """
    if depth == 0 or isinstance(state, (int, float)):
        return state  # terminal utility
    
    if player == "max":
        # Choices: roll or safe option
        roll_value = expectimax("roll", depth-1, "chance")
        safe_value = 6
        return max(roll_value, safe_value)
    
    elif player == "chance" and state == "roll":
        # Roll a fair die
        outcomes = [1, 2, 3, 4, 5, 6]
        return sum(expectimax(o, depth-1, "max") for o in outcomes) / 6

# Run expectimax
value = expectimax("root", depth=2, player="max")
print("Best expected value:", value)
