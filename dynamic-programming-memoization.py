# Memoization example on fibonachi sequence
# Technique of storing previously calculated data to reference in the present call

# Memoization: "Memorize" calculated values so they are not recalculated without need in the future
def fib(n, memo = {}):
	
	print("call")
	if n == 0 or n == 1: return n

	if n not in memo:
		memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
	return memo[n]

# Bottoms up: Instead of using recursion, using an iterative method to solve a problem 

if __name__ =="__main__":
	print(fib(6))