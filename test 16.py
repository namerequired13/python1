

def find_common_elements (list1, list2):
    return list(set(list1) & set(list2))

List1 = [10,20,3,0,5,100]
List2 = [0,10,33,120]
print(find_common_elements(List1, List2))