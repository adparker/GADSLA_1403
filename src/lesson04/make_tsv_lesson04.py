# Code from:
# https://github.com/adparker/GADSLA_1403/wiki/ETL-Tutorial-01--Amazon-Movie-Reviews
# Assumes that movies.small.txt is in the current directory.
# Usage:
#  $ python make_tsv_lesson04.py > outfile.tsv

import csv
import datetime
import sys 

# Open and read in the file.
fh = open('movies.small.txt')
lines = fh.readlines()
fh.close()

# Clean up the lines.
cleanlines = [ line.strip() for line in lines ]
cleanlines = []
for line in lines:
    cleaned = line.strip()
    cleanlines.append(cleaned)

# Group them into lists.
list_of_lists = []
group = []
for line in cleanlines:
    if line != '':
        # Add to the current group
        group.append(line)
    else:
        # Starting a new group.
        # Append the group to the grouped lines and then
        list_of_lists.append(group)
        # Point 'group' to a newly created list.
        # This does not affect the list we just appended to groupedlines
        group = []

# Create a list of dictionaries.
list_of_dicts = []
for group in list_of_lists:
    # Create a new dict for each group.
    group_dict = {}
    for line in group:
        # Split on ': ' once, giving me two pieces.
        longkey, value = line.split(': ', 1)
        # Get the second part of product/productId
        shortkey = longkey.split('/')[1]
        group_dict[shortkey] = value
    # We finished the group. Save it into the list_of_dicts.
    list_of_dicts.append(group_dict)

# Modify the dictionaries in place.
# Convert timestamps.

for review in list_of_dicts:
    # Convert to float
    review['score'] = float(review['score'])
    # Convert to readable time
    int_timestamp = int(review['time'])
    datetime_obj = datetime.datetime.fromtimestamp(int_timestamp)
    str_iso_datetime = datetime_obj.isoformat()
    review['time'] = str_iso_datetime

# Modify in place some more!!
# Convert helpfulness to a float and get the number of helpful votes.
for review in list_of_dicts:
    helpful_str, numberof_str = review['helpfulness'].split('/')
    helpful_int = int(helpful_str)
    numberof_int = int(numberof_str)
    if numberof_int == 0: # Why is this needed?
        numberof_int = 1.0
    review['helpfulness'] = float(helpful_int)/numberof_int
    review['helpful'] = helpful_int
    review['total'] = numberof_int

list_of_keys = list_of_dicts[0].keys()

writer = csv.DictWriter(sys.stdout, # Write to standard out
                        list_of_keys, # Print out all columns
                        delimiter='\t',    # delimiter (separator)
                        quotechar='\\',
                        extrasaction='ignore')  # ignore columns in the dict if the are skipped

# Write the header
writer.writeheader()   

for review in list_of_dicts:
    writer.writerow(review)
