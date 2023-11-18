#!/usr/bin/python3
"""Rotate a 2d matrix in-place"""


def rotate_2d_matrix(matrix: list):
    """Rotate 2d matric in-place"""
    rotate = {}
    length = len(matrix)
    for row in matrix:
        length -= 1
        rotate[length] = [*row]
    for row in matrix:
        for index, _ in enumerate(row):
            row[index] = rotate[index].pop(0)
