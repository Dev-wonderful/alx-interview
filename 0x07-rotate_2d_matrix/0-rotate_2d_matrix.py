#!/usr/bin/env python3
"""Rotate a 2d matrix in-place"""
from typing import List


def rotate_2d_matrix(matrix: List[List]):
    """Rotate 2d matric in-place"""
    rotate = {}
    length = len(matrix)
    for row in matrix:
        length -= 1
        rotate[length] = [*row]
    for row in matrix:
        for index, _ in enumerate(row):
            row[index] = rotate[index].pop(0)
