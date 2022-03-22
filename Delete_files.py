import os
dir_name = '/Users/jonathan/PycharmProjects/CyberRestV2/output'

test = os.listdir(dir_name)
for item in test:
    if item.endswith(".html"):
        os.remove(os.path.join(dir_name, item))