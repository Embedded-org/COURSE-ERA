"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""
IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    len1 = len(line1)
    len2 = len(line2)
    if len1 > len2:
        for var in range(len2):
            if line1[var] != line2[var]:
                return(var)
        return (len2)
    elif len1 < len2:
        for var in range(len1):
            if line1[var] != line2[var]:
                return(var)
        return(len1)
    else:
        for var in range(len1):
            if line1[var] != line2[var]:
                return(var)
    return IDENTICAL


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    index = singleline_diff(line1, line2)
    if line1.find("\n") != -1 or line1.find("\r") != -1:
        return ""
    elif line2.find("\n") != -1 or line2.find("\r") != -1:
        return ""
    else:
        if idx == IDENTICAL or (idx > index and index != -1):
            return ""
        else:
            list1 = []
            list1.append(line1)
            list1.append('\n')
            for var in range(idx):
                list1.append('=')
            list1.append('^')
            list1.append('\n')
            list1.append(line2)
            list1.append('\n')
            return("".join(list1))


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    len1 = len(lines1)
    len2 = len(lines2)
    if len1 > len2:
        for line in range(len2):
            index = singleline_diff(lines1[line], lines2[line])
            if index != IDENTICAL:
                return((line, index))
        return((len2, 0))
    elif len1 < len2:
        for line in range(len1):
            index = singleline_diff(lines1[line], lines2[line])
            if index != IDENTICAL:
                return((line, index))
        return((len1, 0))
    else:
        for line in range(len1):
            index = singleline_diff(lines1[line], lines2[line])
            if index != IDENTICAL:
                return((line, index))
        return (IDENTICAL, IDENTICAL)

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    datafile1 = open(filename, "rt")
    string1 = []
    for line in datafile1.readlines():
        line = line.strip()
        string1.append(line)
    datafile1.close()
    return string1

def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    list1 = get_file_lines(filename1)
    list2 = get_file_lines(filename2)
    len1 = len(list1)
    len2 = len(list2)
    tup1, tup2 = multiline_diff(list1, list2)
    if tup1 == len1:
        list1.append('')
    elif tup1 == len2:
        list2.append('')
    if(tup1 == IDENTICAL and tup2 == IDENTICAL):
        return("No differences\n")
    else:
        string1 = singleline_diff_format(list1[tup1], list2[tup1], tup2)
        list3 = []
        list3.append("Line ")
        list3.append(str(tup1))
        list3.append(':\n')
        string2 = "".join(list3)
        return(string2+string1)


print(file_diff_format('the_idiot.txt','the_idiot1.txt'))
