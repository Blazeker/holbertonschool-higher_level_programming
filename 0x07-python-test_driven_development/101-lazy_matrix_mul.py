#!/usr/bin/python3
""" Matrix multiplication using numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Return multiplication of two matrices"""
    return np.matmul((m_a, m_b))
