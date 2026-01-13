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