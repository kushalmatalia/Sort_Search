# Sort_Search
### Comparison of time complexities between different Sort (Bubble and Merge) and Search (Linear and Binary) algorithms

- **Sorting Algorithms considered** :

  - *Bubble Sort* - Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.
    - Time Complexity:  O(n2). However in practice, this optimized version might take less time as when array gets sorted, function would return.
    - Auxiliary Space: O(1)

  - *Merge Sort* - Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.
    - Time Complexity: O(n*log(n))
    - Auxiliary Space: O(n)
   
- **Searching Algorithms considered** :

  - *Linear Search* - Linear search in Python is one way to find items in a list. A sequential manner is used to find the requested element. Every element is checked about the value we're seeking. If both are equal, the element is found, and the process returns that element's index position.
    
    - Time Complexity : O(n)
    - Auxiliary Space: O(1) for iterative and O(n) for recursive.
   
  - *Binary Search* - Binary Search is a searching algorithm which is used to search an element from a sorted array. It cannot be used to search from an unsorted array. Binary search is an efficient algorithm and is better than linear search in terms of time complexity.
 
    - Time Complexity: O(log n)
    - Auxiliary Space: O(logn)


### Comparison of the time complexities of the above mentioned algorithms
**NOTE**: 
- For Sorting Algorithms, considering the normal or the worst case scenario for time complexity comparison.
- For Searching Algorithms, considering the normal or the worst case scenario for time complexity comparison, provided for Binary Search, the input data in sorted and time is calculated.
  - Also, the time can be adjusted by a factor of 100 if required, for the purpose of plotting and drawing inferences.

*Expected*
- Merge Sort to be better than Bubble Sort in normal and worst case scenario
- Binary Search to be better than Linear Search (when data is sorted) in normal and worst case scenario -> if data is not sorted, Binary Search is not applicable
