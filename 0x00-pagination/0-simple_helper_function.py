#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, ...]:
    """Return a tuple of size two containing a start index and an end index"""
    res = []
    start_index = (page - 1) * page_size
    end_index = page * page_size

    res.append(start_index)
    res.append(end_index)
    return tuple(res)
