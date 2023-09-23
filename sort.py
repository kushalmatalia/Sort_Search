from abc import ABC, abstractmethod
import time
import random

"""Module with the base implementation of a Sort class."""

class Sort(ABC):
    """Abstract base class for sorting."""

    def __init__(self, items):
        self._items = items

    @abstractmethod
    def _sort(self):
        """Returns the sorted version of the elements contained
        in the `_items` property.
        Returns:
            List: The sorted elements.
        """
        pass

    def get_items(self):
        return self._items

    def _time(self):
        start_time = time.time()
        expected_output = self._sort()
        # print("Sorted Array :: ", expected_output)
        end_time = time.time()
        return end_time - start_time
    
class BubbleSort(Sort):

  def __init__(self, arr):
    self.arr = arr

  def _sort(self):
    n = len(self.arr)
    for i in range(n):
      for j in range(0, n-i-1):
        if self.arr[j] > self.arr[j+1]:
          self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
    return self.arr


if __name__ == "__main__":
  data_sizes = [50, 100, 500, 1000, 2000, 3000, 4000, 5000]
  bubble_sort_times = []

  for size in data_sizes:
    data = [random.randint(1, 100) for i in range(size)]
    bub_sorting = BubbleSort(data)
    bub_execution_time = bub_sorting._time()
    # print(f"Bubble Sorting time {size} :", bub_execution_time)
    bubble_sort_times.append(bub_execution_time)

  print("Bubble Sort timings :: ", bubble_sort_times)