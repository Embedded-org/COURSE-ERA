"""
Project for Week 3 of "Python Data Analysis".
Read and write CSV files using a dictionary of dictionaries.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv

def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Ouput:
      A list of strings corresponding to the field names in
      the given CSV file.
    """


    table = []
    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=separator, quotechar=quote)
        k=0
        for row in csvreader:
            if(k>0):
                break
            k=k+1
            for data in row:
                table.append(data)
    print(table)
    return table


def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """

    table = []
    with open(filename,newline='') as csvfile:
        csvreader = csv.DictReader(csvfile,delimiter=separator, quotechar=quote)
        for row in csvreader:
            table.append(row)
    return table



def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    table = {}
    with open(filename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile,fieldnames=keyfield,delimiter=separator, quotechar=quote)
        for row in csvreader:
            table[row[keyfield]] = row
    return table


def read_csv(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries containing the table to write.
    """
    with open(filename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile,fieldnames=keyfield,delimiter=separator, quotechar=quote,quoting=csv.QUOTE_MINIMAL)
        list1=[]
        k=-1
        for data in csvreader:
            k=k+1
            table={}
            for value in data:
                table[value] = data[value]
            #print(table)
            if(k>0):
                list1.append(table)
    return list1





#def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
def write_csv_from_list_dict(filename, table, fieldnames,separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
     """

    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=separator, quotechar=quote,quoting=csv.QUOTE_NONNUMERIC)
            writer.writeheader()
            for data in table:
                writer.writerow(data)
    except IOError:
        print("I/O error")


list1=read_csv_fieldnames("hightemp.csv",",","-")
fieldnames = ['City','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
#table1 = read_csv_as_nested_dict("hightemp.csv",fieldnames,",","-")
table = read_csv("hightemp.csv",fieldnames,',', '"')
write_csv_from_list_dict("data9.csv",table,fieldnames,',', '"') 
