import sys
import os


args = sys.argv
dep_file_name = "DEP"
to_install_file_name = "INST"


def install_deps(deps):
    pass


def deal(_with):
    pass




if os.path.isfile(dep_file_name):
    with open(dep_file_name) as f: install_deps(f.read().split("\n"))

else:
    print("No DEP file found.")
    exit()