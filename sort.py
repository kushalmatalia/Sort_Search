from abc import ABC, abstractmethod
import time
import random

"""
sort.py file -> for accomodating the bubble, merge sorting algorithms
class Sort - is the parent/base class, having the abstract method of _sort, which is protected
           - this abstract method is to be utilized in other sub/children class which will inherit these methods and override the functionality
           - _time is another method, which we have updated in order to generically call the time module and calculate the time taken by the algorithm

class BubbleSort - is the child class for implementing bubble sort algorithm
class MergeSort - is the child class for implementing merge sort algorithm

dataset -> We are hard-coding the data sizes and randomly generating values between 1,100 and thus calculating the time taken for the particular data size
        - Have done the time analysis for both the algorithm and plotted the graph in 'sort.png'
"""

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

class MergeSort(Sort):

  def __init__(self, arr):
    self.arr = arr

  def _sort(self):
    if len(self.arr)>1:
        mid = len(self.arr)//2
        lefthalf = self.arr[:mid]
        righthalf = self.arr[mid:]

        left_sorter = MergeSort(lefthalf)
        right_sorter = MergeSort(righthalf)

        left_sorter._sort()
        right_sorter._sort()

        i=j=k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                self.arr[k]=lefthalf[i]
                i=i+1
            else:
                self.arr[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            self.arr[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            self.arr[k]=righthalf[j]
            j=j+1
            k=k+1
    return self.arr

if __name__ == "__main__":
  data_sizes = [50, 100, 500, 1000, 2000, 3000, 4000, 5000]
  bubble_sort_times = []
  merge_sort_times = []

  for size in data_sizes:
    data = [random.randint(1, 100) for i in range(size)]
    bub_sorting = BubbleSort(data)
    bub_execution_time = bub_sorting._time()
    # print(f"Bubble Sorting time {size} :", bub_execution_time)
    bubble_sort_times.append("{0:.15f}".format(bub_execution_time))

    merg_sorting = MergeSort(data)
    merg_execution_time = merg_sorting._time()
    # print(f"Merge Sorting time {size} :", merg_execution_time)
    merge_sort_times.append("{0:.15f}".format(merg_execution_time))

  print("Bubble Sort timings :: ", bubble_sort_times)
  print("Merge Sort timings :: ", merge_sort_times)