def get_formatted_name(first,last,middle=''):  # WE MUST ASSIGN A DEFAULT VALUE TO AVOID GETTING ERROR
    if middle:                                 # DEFAULT VALUES MUST BE AT THE END OF THE INPUT PARENTHESES !!!!!!!!!!!
        full_name = first + ' ' + middle + ' ' + last
        return full_name.title()
    else:
        full_name = first + ' ' + last
        return full_name.title()
