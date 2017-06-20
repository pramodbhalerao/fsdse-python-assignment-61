def solution(list_of_nums):
    count_odd = 0
    count_even = 0
    d = {}
    for x in list_of_nums:
            if not x % 2:
        	     count_even+=1
            else:
        	     count_odd+=1
    d = { "ODD" : count_odd , "EVEN" : count_even}
    return d

my_list = [1, 2, 3, 5, 8, 9]
solution(my_list)
