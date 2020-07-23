def recursive(n):

	if n <= 1:
		return n

	return recursive(n - 1) + recursive(n - 2)


def dynamic(n, memo={0: 0, 1: 1}):

	try:
		return memo[n]
	except KeyError:
		memo[n] = dynamic(n - 1, memo) + dynamic(n - 2, memo)
		return memo[n]
