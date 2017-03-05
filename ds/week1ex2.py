k = int(raw_input())
l = raw_input()
l = l.split(' ')
this_sum, max_sum = 0, 0
reset = False
start = int(l[0])
end = int(l[-1])
tmp_start = None
for i in xrange(k):
    int_num = int(l[i])
    this_sum += int_num
    if this_sum > max_sum:
        max_sum = this_sum
        if reset:
            start = int_num
        if tmp_start is not None:
            start = tmp_start
        end = int_num
        reset = False
    elif this_sum < 0:
        this_sum = 0
        reset = True
        tmp_start = None
    elif int_num >= 0 and reset == True:
        tmp_start = int_num
        reset = False
if max_sum == 0 and '0' in l:
    print 0, 0, 0
else:
    print max_sum, start, end
