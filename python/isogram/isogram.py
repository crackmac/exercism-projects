def is_isogram(string):
    chars=[ char.lower() for char in string if char not in [' ', '-'] ]
    the_set=set(chars)
    unique_list=list(the_set)
    if len(unique_list) != len(chars):
        return(False)
    return(True)
 