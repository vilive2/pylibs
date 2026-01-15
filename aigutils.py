import re
import subprocess

def count_outputs(aig_file, abc_bin_path):
    """Return number of primary outputs (properties) in the AIG file using ABC."""
    cmd = f'read {aig_file}; print_io;'
    result = subprocess.run(
        [abc_bin_path, "-c", cmd],
        capture_output=True,
        text=True
    )

    po = result.stdout.splitlines()[3]
    # print(po)
    po = re.findall(r"\((.*?)\)", po)
    # print(po)
    if po == []:
      return 0
    return int(po[0])

def get_design_ps (aig_file, abc_bin_path):
  """Return dictionary of ps commad on a design in the AIG file using ABC."""
  cmd = f'read {aig_file}; ps;'
  result = subprocess.run(
      [abc_bin_path, "-c", cmd],
      capture_output=True,
      text=True
  )

  res = result.stdout.split('\n')[-2].split(':')[-1]
  # print(res)
  
  nums = re.findall(r'\d+', res)
  num_input = int(nums[1])
  num_output = int(nums[2])
  num_latches = int(nums[3])
  num_ands = int(nums[4])
  num_levels = int(nums[5])

  return {
    '#input': num_input,
    '#output': num_output,
    '#latch': num_latches,
    '#and': num_ands,
    '#level': num_levels
  }

  

# print (get_design_ps ("../hwmcc13-multi/6s372.aig", "../abc/abc"))