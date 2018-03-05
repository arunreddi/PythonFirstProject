# function to get unique values
def unique(list1):
    # initialize empty list
    unique_list=[]
    # loop elements
    for item in list1:
        # check if exist in unique_list or not
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# using list comprehension multiply all
# def comprtest():
#     list2=[10,5,15,20]
#     res=[x*2 for x in list2]
#     print(res)

list1=[5,2,2,1,3,6]
result=unique(list1)
# comprtest()
print(result)

