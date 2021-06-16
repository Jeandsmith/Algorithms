def my_sqrt(N: int) -> int:
	# x_(n + 1) = 1/2(x_(n) + N / x_(n))

	x_cur = 1;
	res = 0.01
	w = x_cur 

	while w > res:
		x_next = .5 * (x_cur + N / x_cur)
		w = abs(x_next - x_cur)
		x_cur = x_next
	return x_cur

print (my_sqrt(args[0]))
	