from abc import ABC, abstractmethod
import time
import random

"""Module with the base implementation of a Sort class."""

class Search(ABC):
    """Abstract base class for sorting."""

    def __init__(self, items):
        self._items = items

    @abstractmethod
    def _search(self, value):
        """Returns the searched element contained
        in the `_items` property.
        Returns:
            index: The searched element.
        """
        pass

    def get_items(self):
        return self._items

    def _time(self, value):
        start_time = time.time()
        expected_output = self._search(value)
        end_time = time.time()
        return end_time - start_time
    
class LinSearch(Search):
  def __init__(self, arr):
    self.arr = arr

  def _search(self, value):
    for i in range(len(self.arr)):
      if self.arr[i] == value:
        return i
    return -1
  
class BinSearch(Search):
  def __init__(self, arr):
    self.arr = arr

  def _search(self, value):
    l = 0
    r = len(self.arr) - 1
    while l<=r:
      m = (l+r)//2
      if self.arr[m] == value:
        return m
      elif self.arr[m]<value:
        l = m + 1
      else:
        r = m - 1

    return -1

if __name__ == "__main__":
    data_sizes = [50, 500, 1000, 5000, 10000, 50000, 100000, 500000]
    lin_search_times = []
    bin_search_times = []

    for size in data_sizes:
        data = [random.randint(1, 1000) for i in range(size)]
        lin_search = LinSearch(data)
        # lin_search_index = lin_search._search(1001)
        # print(lin_search_index)
        lin_search_execution_time = lin_search._time(1001)
        # print(f"Linear Search time {size} :", lin_search_execution_time)
        lin_search_times.append("{0:.15f}".format(lin_search_execution_time*100))

        bin_search = BinSearch(sorted(data))
        # bin_search_index = bin_search._search(1001)
        # print(bin_search_index)
        bin_search_execution_time = bin_search._time(1001)
        # print(f"Binary Searching time {size} :", bin_search_execution_time)
        bin_search_times.append("{0:.15f}".format(bin_search_execution_time*10000))

print("Linear Search timings :: ", lin_search_times)
print("Binary Search timings :: ", bin_search_times)