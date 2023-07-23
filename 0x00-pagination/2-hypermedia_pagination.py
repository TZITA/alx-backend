#!/usr/bin/env python3
"""Hypermedia pagination"""
import csv
import math
from typing import Tuple, List, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, ...]:
    """Return a tuple of size two containing a start index and an end index"""
    res = []
    start_index = (page - 1) * page_size
    end_index = page * page_size

    res.append(start_index)
    res.append(end_index)
    return tuple(res)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns data from a particular page of a file"""
        res = []
        if not (isinstance(page, int) and isinstance(page_size, int) and
                page > 0 and page_size > 0):
            raise AssertionError

        index = index_range(page, page_size)
        data = self.dataset()
        try:
            for i in range(index[0], index[1]):
                res.append(data[i])
        except IndexError:
            return []
        return res

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Returns dict from a particular page of a file"""
        res = {}
        total_pages = math.ceil(len(self.dataset())/page_size)
        res["page_size"] = page_size
        res["page"] = page
        res["data"] = self.get_page(page, page_size)
        res["total_pages"] = total_pages
        if 1 < page < total_pages:
            res["next_page"] = page + 1
            res["prev_page"] = page - 1
        elif page == 1:
            res["next_page"] = page + 1
            res["prev_page"] = None
        elif page >= total_pages:
            res["next_page"] = None
            res["prev_page"] = page - 1
            res["page_size"] = 0

        return res
