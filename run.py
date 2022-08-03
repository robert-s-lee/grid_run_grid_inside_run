import subprocess
from jsonargparse import CLI

def cmd(grid_key:str=None,grid_username:str=None):
  """create grid datastore.

  Args:
    grid_key = grid login --key
    grid_username = grid login --username
  """
  if not(grid_key is None) and not(grid_username is None):
    subprocess.run(f"grid login --key {grid_key} --username {grid_username}",shell=True)
  subprocess.run("grid datastore",shell=True)
  subprocess.run("grid datastore create --name test .",shell=True)
  subprocess.run("grid datastore",shell=True)

if __name__ == '__main__':
  CLI()