#!/usr/bin/env python3
"""
Hypermedia pagination
"""

import csv
import math
from typing import Tuple, List, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing the start
    index and an end index corresponding to the
    range of indexes to return in a list for
    those particular pagination parameters.

    :param page: The page number.
    :param page_size: The number of items per page.
    :return: A tuple of (start_index, end_index).
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset: List[List[str]] = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset.

        :return: The dataset as a list of lists.
        """
        if self.__dataset is None:
            try:
                with open(self.DATA_FILE) as f:
                    reader = csv.reader(f)
                    dataset = [row for row in reader]
                self.__dataset = dataset[1:]
            except FileNotFoundError:
                self.__dataset = []

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Find the correct indexes to paginate dataset.

        :param page: The page number.
        :param page_size: The number of items per page.
        :return: A list of lists for the requested page.
        """
        assert isinstance(page, int) and page > 0, "Page number must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."
        csv_size = len(self.dataset())
        start, end = index_range(page, page_size)
        end = min(end, csv_size)
        if start >= csv_size:
            return []
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Return dataset as a dictionary with pagination metadata.

        :param page: The page number.
        :param page_size: The number of items per page.
        :return: A dictionary with pagination metadata and the page data.
        """
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page + 1 <= total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }

