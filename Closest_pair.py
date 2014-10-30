''' Create a class point with an x and y coordinate
write mergesort definition
write split and sort definition
1) make two copies of arrays, split
recursive call in subarrays
function that calculates Euclidiean distance'''
import math
import operator
import pdb
import copy
import random



class Point(object):
	def __init__(self, x_coord, y_coord):
		self.x = x_coord
		self.y = y_coord



def Euclidian_distance(point_a, point_b):
	return math.sqrt(math.pow((point_a.x - point_b.x), 2) + math.pow((point_a.x - point_b.x),2))


def mergesort(input_array, attribute):
	#Base case
	if len(input_array) == 1:

		final_output = [copy.deepcopy(input_array[0])]
		return final_output

	
	else:
		#split point
		mid_index = math.floor(len(input_array)/2)

		final_index, first_index, second_index = 0, 0, 0
		final_output = list()
		first_half = input_array[:mid_index]
		second_half = input_array[mid_index:]

		sorted_first_half = mergesort(first_half, attribute)
		sorted_second_half = mergesort(second_half, attribute)


		#Combine the two arrays in sorted order
		
		f = operator.attrgetter(attribute)

		while first_index < len(sorted_first_half) and second_index <  len(sorted_second_half):
			
			if f(sorted_first_half[first_index]) < f(sorted_second_half[second_index]):
				final_output.append(copy.deepcopy(sorted_first_half[first_index]))
				first_index += 1
			else:
				final_output.append(copy.deepcopy(sorted_second_half[second_index]))
				second_index += 1
			final_index += 1


		if first_index <= len(first_half)-1 or second_index <= len(second_half)-1:
			if first_index <= len(sorted_first_half)-1:
				new= [copy.deepcopy(x) for x in sorted_first_half[first_index:]]	
			else:
				new = [copy.deepcopy(x) for x in sorted_second_half[second_index:]]
			final_output.extend(new)

	return final_output


def split_sort(input_array, delta):
	#double for loop, for each element in array
	best_delta = delta
	best_pair = (None, None)
	for i in range(max(0, len(input_array) - 1)):
		for j in range(max(0, i - 8), min(i+8, len(input_array)-1)):
			if i == j:
				pass
			else:

				d = Euclidian_distance(input_array[i], input_array[j])
				if d < best_delta:
					best_delta = d
					best_pair = (input_array[i], input_array[j])
	return best_delta, best_pair 

def brute_force(input_array):
	if len(input_array) < 2:
		return None, (None, None)
	distances = [(Euclidian_distance(x, y), (x, y)) for x in input_array for y in input_array[x.index:] if not(x.x==y.y and y.x==y.y)]
	sorted_distances = sorted(distances, key = operator.itemgetter(0))
	return sorted_distances[0]


def closest_points(input_array):
	#base case, 2 points, calculate distance and return it


	if len(input_array) <=3:
		delta, best_pair = brute_force(input_array)
		return delta, best_pairs
	#create a copy of array, split into 2 subsorted arrays
	else:	
		input_array_x = mergesort(copy.deepcopy(input_array), 'x')
		input_array_y = mergesort(copy.deepcopy(input_array), 'y')
		midpoint = int(len(input_array)/2)
		first_x = copy.deepcopy(input_array_x[:midpoint])
		first_y = copy.deepcopy(input_array_y[:midpoint])
		second_x = copy.deepcopy(input_array_x[midpoint:])
		second_y = copy.deepcopy(input_array_y[midpoint:])
		##pdb.set_trace()
		#first = list(first_x + first_y)
		#second = list(second_x.extend(second_y))

		

		first_delta, first_pair = closest_points(first_x + first_y)
		second_delta, second_pair = closest_points(second_x  + second_y)
		#pdb.set_trace()
		temp_best = min(first_delta, second_delta)
		split_array = [x for x in input_array if abs(x.x - input_array[midpoint].x) < temp_best]

		split_delta, split_pair = split_sort(split_array)

		if split_pair[0] is None:
			if first_delta < second_delta:
				return first_delta, first_pair
			return second_delta, second_delta
		return split_delta, split_pair
		

if __name__ == '__main__':
	input_list = [Point(random.randint(-100, 100), random.randint(-100, 100)) for x in range(10)]
	for i in range(len(input_list)):
	
		print("mergesort %s " %input_list[i].x)
	
	sorted_x = mergesort(input_list, 'x')

	for i in range(len(input_list)):
		print("mergesort %s " %sorted_x[i].x)



