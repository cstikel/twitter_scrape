import yaml

from yaml.loader import SafeLoader

with open('config.yaml', 'r') as f:
    data = list(yaml.load_all(f, Loader=SafeLoader))
    print(data)