#!/usr/bin/env python3
""" Simple pagination """
import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset: List[List[str]] = []

    def dataset(self) -> List[List[str]]:
        """Cached dataset
        """
        if not self.__dataset:
            try:
                with open(self.DATA_FILE) as f:
                    reader = csv.reader(f)
                    self.__dataset = [row for row in reader][1:]  # Skip header row
            except FileNotFoundError:
                self.__dataset = []

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """Finds the correct indexes to paginate dataset and returns the page.
        
        :param page: The page number to retrieve.
        :param page_size: The number of items per page.
        :return: A list of lists representing the data for the requested page.
        """
        assert isinstance(page, int) and page > 0, "Page number must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        end = min(end, len(dataset))
        if start >= len(dataset):
            return []
        return dataset[start:end]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple containing start and end index for pagination.

    :param page: The page number to calculate indices for.
    :param page_size: The number of items per page.
    :return: A tuple of (start, end) indices.
    """
    return (page - 1) * page_size, page * page_size

