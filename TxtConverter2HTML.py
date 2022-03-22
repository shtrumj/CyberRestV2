import pandas as pd

files = ["output/domains.txt", "output/ip.txt", "output/md5.txt","output/sha256.txt","output/sha1.txt"]

for file in files:
    inputFile =  file[:-4]
    OutputFile = inputFile + '.html'
    print(inputFile)
    read_file = pd.read_csv (file)
    read_file.to_html(OutputFile, index=None)