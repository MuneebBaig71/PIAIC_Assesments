def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """

    print(f"first element of the list is '{lst[-1]}'")
def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst


lst = get_lst()
get_first_element(lst)