def list_comprehension_numbers(my_list_1):

    from functools import reduce

    odd_list = list(filter(lambda x: x % 2 == 1, my_list_1))
    even_list = list(filter(lambda x: x % 2 == 0, my_list_1))
    squared_list = list(map(lambda x: x ** 2, my_list_1))
    cubed_list = list(map(lambda x: x ** 3, my_list_1))
    divided_by_three = list(map(lambda x: round(x / 3, 2), my_list_1))
    # sum_of_elements = sum(map(lambda x: x, my_list_1))
    sum_of_elements = reduce(lambda num_1, num_2 : num_1 + num_2, my_list_1)

    return odd_list, even_list, squared_list, cubed_list, divided_by_three, sum_of_elements
    
odd_list, even_list, squared_list, cubed_list, divided_by_three, sum_of_elements = list_comprehension_numbers([i for i in range(11)])

print("ODD LIST :", odd_list, "\nEVEN LIST :", even_list, "\nSQUARED LIST :", squared_list,
      "\nCUBED LIST :", cubed_list, "\nLIST (DIVIDED BY 3) :", divided_by_three,
        "\nSUM OF ELEMENTS :", sum_of_elements)


def list_comprehension_strings(my_list_2):

    upper_case_string = [word.upper() for word in my_list_2]
    length_of_words = [len(word) for word in my_list_2]
    reverse_string = [word[::-1] for word in my_list_2]
    filtered_string_a_included = [word for word in my_list_2 if 'a' in word]

    return upper_case_string, length_of_words, reverse_string, filtered_string_a_included

upper_case_string, length_of_words, reverse_string, filtered_string_a_included = list_comprehension_strings(["apples", "bananas", "pear", "cherry", "strawberry",
                                                                                                             "orange", "mango", "litchi", "blue berry"])

print("UPPER CASE STRING :", upper_case_string, "\nLENGTH OF WORDS :", length_of_words, "\nREVERSE STRING :", reverse_string, "\nFILTERED STRING (WITH 'A') :", filtered_string_a_included)