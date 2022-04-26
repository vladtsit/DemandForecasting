import glob

file_count = 0
# count number of files in data directory
for filepath in glob.iglob(r'./data/*.csv', recursive=False):
    file_count = file_count + 1

print("# of CSV files is " + str(file_count))

if(file_count != 3):
    raise Exception("Number of CSV files does not match. Expected: 3. Actual: " + str(file_count))
