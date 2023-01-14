"""
CMSC 14100, Autumn 2022
Homework #4

We will be using anonymous grading, so please do NOT include your name
in this file

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

# Exercise 1
def prefix_distance(u, v):
    '''
    Computes the prefix distance of u and v. The prefix distance is the total
    number of characters that do not belong to the longest common prefix shared
    by u and v.

    For example, the prefix distance of "morning" and "mourning" is 11, since
    the longest common prefix of the two strings is "mo".

    Input:
        u (str): first input string
        v (str): second input string

    Output: prefix distance of u and v (int)
    '''
    idx = 0
    matches = 0
    while idx < min(len(u), len(v)):
        if u[idx] == v[idx]:
            matches = matches + 1
            idx += 1
        else:
            break

    do_not_belong = len(u) + len(v) - (2 * matches)

    return do_not_belong

# Exercise 2
def suffix_distance(u, v):
    '''
    Computes the suffix distance of u and v. The suffix distance is the total
    number of characters that do not belong to the longest common suffix shared
    by u and v.

    For example, the suffix distance of "morning" and "mourning" is 5, since
    the longest common suffix of the two strings is "rning".

    Input:
        u (str): first input string
        v (str): second input string

    Output: suffix distance of u and v (int)
    '''
    idx = -1
    matches = 0
    while idx >= -1 * (min(len(u), len(v))):
        if u[idx] == v[idx]:
            matches = matches + 1
            idx -= 1
        else:
            break

    do_not_belong = len(u) + len(v) - (2 * matches)

    return do_not_belong

#Exercise 3
def total_badness(text, width):
    '''
    Returns the total 'badness' of a given text based on the number of
    characters that exceed or fall short of the given width after text is
    split up. This is calculated by adding the cubes of the numerical value of
    falling short or exceeding the line width for all lines except the last one.

    Input:
        text (str): text to be split
        width (int): width to split text by

    Output:
        Total badness (int) as cube of characters that fall short or exceed
        width limit
    '''
    splitted = split_lines(text, width)
    cumulative = 0

    for i in range (0, len(splitted)-1):
        cumulative += abs(len(splitted[i])-width)**3

    return cumulative

# Exercise 4
def split_lines(text, width):
    '''
    Splits up the text based on the provided width and returns a list that has
    lines split up with width at most the given width such that no word
    is broken up between lines.

    For example, given "There is a fox hunting in the dark forest." split with a
    width of 8, the output would be:
    ["There is", "a fox", "hunting", "in the", "dark", "forest."]

    Input:
        text (str): text to be split
        width (int): width to split text by

    Output:
        List of text split up by length at most given width
    '''
    split = text.split()
    cumulative_size = 0
    splitted = []
    current = ""
    print(split)
    for i,each in enumerate(split):
        print("current word:", each)
        
        if (len(each) == width):
            splitted.append(each)
            print("appended1:", current)
            cumulative_size = 0
            current = ""
            
        elif len(current) != 0:
            print ("testing: ", current,  each)
            if (cumulative_size + len(each) + 1 <= width):
                current += " " + each
                cumulative_size += len(each) + 1
            else:
                splitted.append(current)
                print("appended2:", current)
                current  = ""
                cumulative_size = 0
                
        elif len(current) == 0:
            current += each
            cumulative_size += len(each)
        print(current)
                
    return splitted
    
print(split_lines("Hi my name is Md.", 5))

# Exercise 5
def arrange_lines(text, width, blanks_visible=False):
    '''
    Transforms a given text after splitting lines based on width by adding
    blanks (_) if width of line is < given width and blanks_visible parameter is
    True. Then adds a new line where next line begins.

    Input:
        text (str): Text to be split and arranged
        width (int): Width to split by before arranging

        blanks_visible (boolean): Whether to display blanks if line width <
        given width

    Output (String):
        Text that is split up based on the given width such that lines are of
        length at most given width and words are not split between lines
        in which if blanks_visible = True and line width < given width, empty
        spaces are filled with "_" and new lines (r"\n") are added after each
        line
    '''

    splitted = split_lines(text, width)
    cumulative_text = ""

    for i,each in enumerate(splitted):
        if blanks_visible:
            if len(each) < width:
                for _ in range(width-len(each)):
                    each += "_"
                cumulative_text += each + ("\n" if i != len(splitted)-1 \
                    else "")
            else:
                cumulative_text += each + ("\n" if i != len(splitted)-1 \
                    else "")
        else:
            if i != len(splitted)-1:
                cumulative_text += each + "\n"
            else:
                cumulative_text += each

    return cumulative_text

# print(arrange_lines("Hello World, my name is Md Hossian and I am writing this because I want to split this text into width of 20.", 20, True))

# Exercise 6
def optimal_width(text, min_width=0, max_width=80):
    '''
    Computes the optimal width based on given max and min width that will return
    text split greedily into lines with the least 'badness' number

    Input:
        text (str): Text to be split and badness calculated
        min_width (int): Minimum bound of width to test badness of
        max_width (int): Maximum bound of width to test badness of

    Output (int):
        The width that will have the least 'badness'
    '''
    minimum_badness = total_badness(text, min_width)
    optimal  = min_width

    for i in range (min_width, max_width + 1):
        if total_badness(text, i) < minimum_badness:
            optimal = i
            minimum_badness = total_badness(text, i)

    return optimal
