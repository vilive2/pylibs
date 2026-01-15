from aigutils import count_outputs, get_design_ps
import os
import csv

abc_bin_path = "../abc/abc"
folder = "../hwmcc13-multi"
designs = []

for file in os.listdir(folder):
  if file.endswith(".aig"):
    try:
      ps = get_design_ps(folder+'/'+file, abc_bin_path)
      ps['design'] = file
      designs.append(ps)
    except Exception as e:
      print(e)
      print(file)


outfile = 'designs.csv'

with open(outfile, mode='w', newline='') as file:
  fieldnames = ['design', '#input', '#output', '#latch', '#and', '#level']
  writer = csv.DictWriter(file, fieldnames=fieldnames)

  writer.writeheader()

  writer.writerows(designs)



