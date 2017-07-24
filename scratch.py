def fn(x, limit):
    answers = []
    answers.append('x * y +/- 1')
    for y in range(2, limit+1):
        answers.append('{0} * {1} + 1 = {2} {3}'.format(x, y, x*y+1, 'even' if (x*y+1)%2==0 else '    '))
        answers.append('{0} * {1} - 1 = {2} {3}'.format(x, y, x*y-1, 'even' if (x*y+1)%2==0 else '    '))
    return answers

# for i, j in zip(fn(3, 10), fn(6, 10)):
#     print(i, '\t\t',  j)

for i in fn(6, 10):
	print(i)