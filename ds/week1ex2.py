k = int(raw_input())
l = raw_input()
l = l.split(' ')
this_sum, max_sum = 0, 0
reset = False
start = int(l[0])
end = int(l[-1])
for i in xrange(k):
    int_num = int(l[i])
    this_sum += int_num
    if this_sum > max_sum:
        max_sum = this_sum
        if reset:
            start = int_num
        end = int_num
        reset = False
    elif this_sum < 0:
        this_sum = 0
        reset = True
    elif int_num == 0 and max_sum == 0:
        start = 0
        end = 0
        reset = False

print max_sum, start, end
