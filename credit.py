
import functools
list_1 = [5  , 5  , 4  , 1 ,  8  , 0  , 8 ,  9  , 2  , 3   ,7 ,  9 ,  5  , 2 ,  4  , 0]
temp_list = []

for i, x in enumerate(list_1):
    temp_list = list_1
#    new_list = filter(lambda elem : list_1.index(elem) % 2 == 0, list_1)
# for x in new_list:
#     print(x)
# split the items into an array. if the array has more than 1 element then the digit is over ten. sum the digits casting them to int 


#from the rightmost digit, which is the check digit, moving left, double the value of every other digit
#[10, 5, 8, 1, 16, 0, 16, 9, 4, 3, 14, 9, 10, 2, 8, 0]
    if ((i%2) == 0 ):
       temp_list[i] = list_1[i] * 2

#if product of this doubling operation is greater than 9 (e.g., 7 * 2 = 14), then sum the digits of the products
#1   5   8   1   7   0   7   9   4   3   5   9   1   2   8   0
summation = 0 
for indx,elem in enumerate(temp_list):
    #print(indx)
    if (elem >= 10):
        temp_list[indx] = 0
        for digit in str(elem):
            temp_list[indx] += int(digit)
            
#take the sum of all the digits
total = functools.reduce(lambda agg, item : agg + item, temp_list)   
#if and only if the total modulo 10 is equal to 0 then the number is valid
if ( total % 10 == 0 ):
    print((total % 10 == 0))
    