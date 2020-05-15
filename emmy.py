#function part2 using *args#it does not have to be args all the time you can use any word you like but *must be there
#gathers remaining arguments as a tupple#
def sum_all_nums(*args):
    total=0
    for num in args:
        total+=num
    return total
print(sum_all_nums(2,3,5,6,7,10)) 
print(sum_all_nums(2,3))  

#keyword args..kwargs uses two **#gathers remaining arguments as a dictionary
def fav_colours(**kwargs):
    #print(kwargs)
    for person,colour in kwargs.items():
      print(f"{person}'s favourite colour is {colour}")
fav_colours(ruby="blue",jerry="purple",denviour="yellow",brandy="teal") 