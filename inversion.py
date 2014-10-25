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
		return arr
	else:
		print(n)
		#if n ==2:
			#pdb.set_trace()
		first_half = list(merge_sort(arr[: int(n/2)]))
		print("first %s" %first_half)
		second_half = list(merge_sort(arr[int(n/2):]))
		print("second%s" %second_half)
		sorted_arr = [0]
		i, j = 0, 0
		

		for k in range(n):
			print("Sorted %s" %sorted_arr)
			if i < len(first_half) and j < len(second_half):
				print("Entering")

				print(first_half[i])
				print(second_half[j])
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
		
		return sorted_arr[1:]


if __name__ == '__main__':

	num_inversions = 0

	test_1 = [5, 6, 7, 5, 6, 2, 3, 1, 9, 0, 0, 2]

	print(merge_sort(test_1))
	print(num_inversions)


