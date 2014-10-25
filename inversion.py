#Computer number of inversions in a file
#Where the ith row of the number indicates the array position
#implement the divide and conquer algorithm described
#numberic integer should be output
#the file contains all of integers 1 - 100,000 inclusive
import pdb


''' Pseudo Code

COunt(array A, length n):
	if n=1, return 0
	else
		X= Count(A/2, n/2)
		Y = Count(A/2 (second half), n/2)
		Z = CountSplitInv(A,n)
	return x+y+Z
	for k=1 to n 
		if B(i) < C(j)
			D(k) = B(i)
			i++
		else [C(j) < B(i)]
				D(k) = B(j)
				j++'''

def merge_sort(arr):
	#Base case, length of array if 1
	n = len(arr)
	if n == 1 :
		return arr, 0
	else:
		first_half, inversions_1 = list(merge_sort(arr[: int(n/2)]))
		second_half, inversions_2 = list(merge_sort(arr[int(n/2):]))

		num_inversions = inversions_1 + inversions_2
		sorted_arr = [0]
		i, j = 0, 0
		

		for k in range(n):
			if i < len(first_half) and j < len(second_half):
				if first_half[i] < second_half[j]:
					sorted_arr.extend([first_half[i]])
					i += 1
				else:
					sorted_arr.extend([second_half[j]])
					j += 1
					num_inversions += len(first_half) - i
	

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
	


