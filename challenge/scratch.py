def fn(x, limit):
    answers = []
    answers.append('x * y +/- 1 = coprimes')
    for y in range(2, limit+1):
        answers.append('{0} * {1} + 1 = {2} {3}'.format(x, y, x*y+1, 'even' if (x*y+1)%2==0 else '    '))
        answers.append('{0} * {1} - 1 = {2} {3}'.format(x, y, x*y-1, 'even' if (x*y+1)%2==0 else '    '))
    return answers

def coprimes(n):
	output = [2, 3]
	for m in range(1, n//6+1):
		output = output + [6*m-1] + [6*m+1]
	print(len(output))
	return output

# for i, j in zip(fn(3, 10), fn(6, 10)):
#     print(i, '\t\t',  j)

for i in fn(6, 100//6):
	print(i)

print(coprimes(10000))

# print(10000//6)
