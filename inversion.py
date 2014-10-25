#Utilizes the mergesort algorithm to calculate number of inversion
#Program takes large file of numbers, and sorts with merge sort
#Also calculates number of inversions, or when numbers needed 
#to be swapped during sorting recursively

#the file contains all of integers 1 - 100,000 inclusive



def merge_sort(arr):
	#Base case, length of array if 1
	n = len(arr)
	if n == 1 :
		return arr, 0
	else:
		#apply sort to sub arrays, return number of inversions and arrays
		first_half, inversions_1 = list(merge_sort(arr[: int(n/2)]))
		second_half, inversions_2 = list(merge_sort(arr[int(n/2):]))

		num_inversions = inversions_1 + inversions_2
		sorted_arr = [0]
		i, j = 0, 0
		
#correctly merge the two smaller sub arrays
		for k in range(n):
			if i < len(first_half) and j < len(second_half):
				if first_half[i] < second_half[j]:
					sorted_arr.extend([first_half[i]])
					i += 1
				else:
					sorted_arr.extend([second_half[j]])
					j += 1
					num_inversions += len(first_half) - i
	
#append any additional elements in subarrays
		if len(first_half) == i:
			sorted_arr.extend(second_half[j:])
		else:
			sorted_arr.extend(first_half[i:])
		
		return sorted_arr[1:], num_inversions


if __name__ == '__main__':

	#reads in text file with integers and creates list
	import csv
	integer_list = list()

	with open('IntegerArray.txt', encoding = 'utf-8') as f:
		for line in f:
			integer_list.append(int(line.strip()))


	print(merge_sort(integer_list)[1])
	


