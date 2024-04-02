def binary_search(List_of_integers, Targeted_value_to_search):
    first_index = 0
    length = len(List_of_integers)
    last_index = length - 1

    while first_index <= last_index:
        mid_index = (first_index + last_index) // 2


        if List_of_integers[mid_index] == Targeted_value_to_search:
            return (mid_index)

        elif List_of_integers[mid_index] < Targeted_value_to_search:
            first_index = mid_index + 1

        else:
            last_index = mid_index - 1

        return -1
           
    


List_of_integers = list(map(int, input("Enter the integers: ").split()))
Targeted_value_to_search = int(input ('Enter the Targeted Value to be searched: '))
Result = binary_search(List_of_integers, Targeted_value_to_search)
print (Result)
    
    
    
if Result != -1:
        print (f'Targeted Value {Targeted_value_to_search} found at index {Result}')

else:
        print (f'Targeted Value {Targeted_value_to_search} not found in the list.')
   




    