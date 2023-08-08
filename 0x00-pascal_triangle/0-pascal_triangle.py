#!/usr/bin/python3
"""
Pascal's Triangle Generator
This module def a fnctn for generatn Pascal's Triangle based on given rows.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to a specified number of rows.

    Parameters:
        n (int): The number of rows to generate in Pascal's Triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle up to the nth row.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    # Run the test cases using pytest
    pytest.main([__file__])
