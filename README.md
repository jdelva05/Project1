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

## Benchmarking results
Execution Time:<br>
Hybrid QuickSort:<br>
100 elements: 0.000098s (approximately 0.1ms)<br>
500 elements: 0.000636s (approximately 0.64ms)<br>
1,000 elements: 0.00141s (approximately 1.41ms)<br>
5,000 elements: 0.00835s (approximately 8.35ms)<br>
10,000 elements: 0.0223s (approximately 22.3ms)<br>
50,000 elements: 0.2126s (approximately 213ms)<br>

Python's list.sort():<br>
100 elements: 0.0000119s (approximately 0.012ms)<br>
500 elements: 0.000082s (approximately 0.082ms)<br>
1,000 elements: 0.000111s (approximately 0.111ms)<br>
5,000 elements: 0.000618s (approximately 0.618ms)<br>
10,000 elements: 0.00134s (approximately 1.34ms)<br>
50,000 elements: 0.00832s (approximately 8.32ms)<br>

Memory Usage:<br>
Hybrid QuickSort:<br>
The memory consumption was negligible for most input sizes, with occasional spikes (0.0039MB or 3.9KB).
