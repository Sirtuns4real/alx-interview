#!/usr/bin/python3

"""
Unlock Boxes
This module defines a function to determine if all the boxes can be opened based on keys.
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened based on provided keys.

    Parameters:
        boxes (list): A list of lists where each inner list represents the keys in a box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    # Create a set to keep track of opened boxes
    opened_boxes = set()
    opened_boxes.add(0)  # Start with the first box (box 0) opened
    
    # Create a queue for BFS traversal
    queue = [0]
    
    while queue:
        current_box = queue.pop(0)
        
        # Iterate through keys in the current box
        for key in boxes[current_box]:
            # If the key opens a new box and the box is not already opened
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)
                queue.append(key)
    
    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)

# Test cases
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 5], [2], [5, 2], [3], [4, 1], [3, 5]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[4, 6], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False

boxes4 = [[0]]
print(canUnlockAll(boxes4))  # Output: True

boxes5 = [[10, 3, 8, 9, 6, 5, 8, 1], [8, 5, 3, 7, 1, 8, 6], [5, 1, 9, 1], [], [6, 6, 9, 4, 3, 2, 3, 8, 5], [9, 4], [4, 2, 5, 1, 1, 6, 4, 5, 6], [9, 5, 8, 8], [6, 2, 8, 6]]
print(canUnlockAll(boxes5))  # Output: True

boxes6 = [[7, 5], [1, 10, 7], [9, 6, 10], [7, 9], [2], [7, 3], [7, 9, 10, 10, 8, 9, 2, 5], [7, 2, 2, 4, 4, 2, 4, 8, 7], [4, 2, 9, 6, 6, 5, 5]]
print(canUnlockAll(boxes6))  # Output: False
