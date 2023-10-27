# Hybrid and Adaptive Sorting Algorithms
Hybrid Algorithm

## Goals
1. Implementation
   
   Create and put into use a hybrid sorting algorithm that combines insertion sort and quicksort. For sub-arrays that are larger than a threshold size, the algorithm employs quicksort;    for sub-arrays that are smaller, it uses insertion sort.

2. Testing

   Use test cases to verify that the implemented hybrid sorting algorithm is correct.

3. Benchmarking

   Time Performance: For varying input sizes, compare the hybrid sorting algorithm's execution time to that of Python's built-in sorting algorithm,.sort().
   
   Memory Performance: Use the memory-profiler library to assess how much memory the hybrid sorting algorithm uses for various input sizes.
   
   Performance analysis: Examine the benchmarking experiment results to identify situations where the hybrid algorithm may perform better than the conventional sorting algorithm. The      execution time and memory usage metrics gathered during benchmarking will make this clear.

4. Summary

   To put it briefly, the project's objectives are to evaluate a hybrid sorting algorithm's performance in comparison to Python's built-in sorting function and investigate the 
   algorithm's efficiency (both in terms of execution time and memory usage).

## Algorithm Description
A hybrid algorithm that combines the Insertion Sort and QuickSort algorithms. The plan is to use Insertion Sort for smaller portions of the array (when the array size is less than a threshold) and QuickSort for larger portions of the array.
