#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any

Server = __import__('2-hypermedia_pagination').Server

class Server(Server):
    """Server class to paginate a database of popular baby names with deletion resilience."""

    def __init__(self):
        super().__init__()
        self.__indexed_dataset = None

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """
        Returns a dictionary with key-value pairs for pagination with deletion resilience.

        :param index: The starting index of the page
        :param page_size: Number of items per page
        :return: A dictionary with index, data, next_index, and page_size
        """
        assert isinstance(index, int)
        assert isinstance(page_size, int)
        
        dataset = self.indexed_dataset()
        data = []
        next_index = index
        
        for _ in range(page_size):
            while next_index not in dataset:
                next_index += 1
            data.append(dataset[next_index])
            next_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index
        }

