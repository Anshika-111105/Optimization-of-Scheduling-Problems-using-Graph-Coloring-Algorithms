import numpy as np

# Define number of exams and conflict matrix
n = 5
conflict_matrix = np.array([
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0]
])

# Graph coloring using greedy algorithm
def greedy_coloring(conflict_matrix, n):
    result = [-1] * n  # Store color assignment
    result[0] = 0  # Assign the first color to the first exam

    # Available colors array
    available = [False] * n

    for u in range(1, n):
        # Mark colors of adjacent vertices as unavailable
        for i in range(n):
            if conflict_matrix[u][i] == 1 and result[i] != -1:
                available[result[i]] = True
        
        # Find the first available color
        color = 0
        while color < n:
            if not available[color]:
                break
            color += 1
        
        # Assign the found color
        result[u] = color

        # Reset available colors for the next iteration
        available = [False] * n

    # Print color assignment
    for u in range(n):
        print(f"Exam {u} --->  Time Slot {result[u]}")

# Run the greedy algorithm
greedy_coloring(conflict_matrix, n)
