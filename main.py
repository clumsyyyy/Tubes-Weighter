from keywords import calculateWeight
from merge_sort import merge_sort


array = []

print()

while (True):
    query_input = input("Masukkan query: ")
    if (query_input.lower() == "exit"):
        break
    if (len(query_input) != 0):
        array.append([query_input, calculateWeight(query_input)])
    
merge_sort(array)
nums = [elmt[1] for elmt in array]
max_weight = max(nums)
min_weight = min(nums)
hard_limit = int(min_weight + ((max_weight - min_weight) * (2 / 3)))
medium_limit = int(min_weight + ((max_weight - min_weight) * (1 / 3)))

print("\nUrutan pengerjaan yang sebaiknya dilakukan:\n")

for i in range(len(array)):
    if (array[i][1] >= hard_limit):
        print("IMPORTANT - ", end = "")
    elif (array[i][1] > medium_limit and array[i][1] < hard_limit):
        print("MODERATE - ", end = "")
    else:
        print("BACKLOG - ", end = "")
    print(array[i][0] + " - " + str(array[i][1]))
    
print()
