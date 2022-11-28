"""
Pseudocode:
Put test cases in the main function

Create a function skip_tuples:
    Create a variable for a new tuple
    Consider each element of the inputted tuple:
        If the index of the element is even (it starts with 0):
            Append it into the new tuple
    Return that new tuple once every element of the old tuple has been considered

Setting up the main function
"""

def main():
    # Test Cases Below
    print(skip_tuples((1, 2, 3, 4, 5))) # Returns: (1, 3, 5)
    print(skip_tuples(("a", "b", "c","d", "e", "f", "g"))) #Returns: ('a', 'c', 'e', 'g')
    print(skip_tuples((("a", "c"), ("b", "d"), ("e", "z")))) # Returns: (('a', 'c'), ('e', 'z'))
    print(skip_tuples(())) # Returns: ()

def skip_tuples(tuple):
    """
    tuple: any defined tuple
    returns: a new tuple, only containing every other element of the inputted tuple
    """
    new_tuple = ()
    for i in range(len(tuple)):
        if i % 2 == 0:
            new_tuple += (tuple[i],)
    return new_tuple

if __name__ == "__main__":
    main()