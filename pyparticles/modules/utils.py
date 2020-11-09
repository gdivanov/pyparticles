import yaml
from collections import OrderedDict


def process_yaml(file_path: str,
                 read_write_type: str):

    with open(file_path, read_write_type) as yaml_file:
        try:
            yaml_dict = OrderedDict(yaml.safe_load(yaml_file))
            return yaml_dict

        except yaml.YAMLError as exc:
            print(exc)