k = int(raw_input())
l = raw_input()
l = l.split(' ')
this_sum, max_sum = 0, 0
for i in xrange(k):
    this_sum += int(l[i])
    if this_sum > max_sum:
        max_sum = this_sum
    elif this_sum < 0:
        this_sum = 0
print max_sum
