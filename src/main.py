import fibonacci
import time


def get_times(implementation, samples=10):

	times = []
	for i in range(samples + 1):
		start = time.time()
		implementation(i)
		end = time.time()
		times.append((i, end - start))

	return times


if __name__ == '__main__':
	result_recursive = fibonacci.recursive(10)
	result_dynamic = fibonacci.dynamic(10)
	print(result_recursive)
	print(result_dynamic)
