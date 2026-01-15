import csv
from tabulate import tabulate

filename = 'designs.csv'

designs = []
with open(filename, mode='r', newline='') as file:
    reader = csv.DictReader(file)
    designs = [row for row in reader]

designs.sort(key = lambda x: int(x['#output']))

table_data = [list(row.values()) for row in designs]

headers = designs[0].keys()

print(tabulate(table_data, headers=headers, tablefmt="grid"))
# for design in designs:
#     print(design)


min_out = int(designs[0]['#output'])
max_out = int(designs[-1]['#output'])

num_bucket = 16

bucket_width = (len(designs) + num_bucket-1) // num_bucket

# print(bucket_width)

selected_designs = []

for i in range (num_bucket):
    l = i*bucket_width
    r = l + bucket_width

    designs_in_bucket_i = designs[l: r]

    max_size_design = max(designs_in_bucket_i, key=lambda x : int(x['#and']))

    selected_designs.append(max_size_design)

    # print (i, len(designs_in_bucket_i), max_size_design)


outfile = 'selected_designs.csv'

with open(outfile, mode='w', newline='') as file:
    fieldnames = ['design', '#input', '#output', '#latch', '#and', '#level']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerows(selected_designs)



print('#'*100)
print(f'{"SELECTED DESIGNS":^50}')

table_data = [list(row.values()) for row in selected_designs]

print(tabulate(table_data, headers=headers, tablefmt="grid"))