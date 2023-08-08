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

    Example:
        >>> boxes1 = [[1], [2], [3], []]
        >>> canUnlockAll(boxes1)
        True

        >>> boxes2 = [[1, 3], [3, 0, 1], [2], [0]]
        >>> canUnlockAll(boxes2)
        False
    """
    # Create a set to keep track of opened boxes
    opened_boxes = set()
    
    # Start with the first box (box 0) opened
    opened_boxes.add(0)
    
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
boxes1 = [[1], [2], [3], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 3], [3, 0, 1], [2], [0]]
print(canUnlockAll(boxes2))  # Output: False
