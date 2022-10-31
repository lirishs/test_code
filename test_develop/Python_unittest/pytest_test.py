import yaml
import os

data_list = [3,4,5,6,734,3]

with open("document.stream",mode="w") as f:
    yaml.safe_dump_all(data_list,f)