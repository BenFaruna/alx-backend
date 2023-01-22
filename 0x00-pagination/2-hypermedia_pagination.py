#!/usr/bin/env python3
"""module implementing the Server class with its methods"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function returns a tuple containing a start index and an end index
corresponding to the range of indexes to return in a list for those
particular pagination parameters"""
    start = ((page - 1) * page_size)
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """initialize the class"""
        self.__dataset = None
        self.dataset()

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
        """function returns the data at a particular page and returns a list"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        return self.__dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """function returns the data at a particular page using hypermedia"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        total_page = math.ceil(len(self.__dataset) / page_size)
        next_page = None if page >= total_page else page + 1
        prev_page = None if page == 1 else page - 1
        data = self.__dataset[start:end]
        return {
            'page_size': len(data), 'page': page, 'data': data,
            'next_page': next_page, 'prev_page': prev_page,
            'total_pages': total_page
        }
