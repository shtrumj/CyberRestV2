import downloader
import jsonParser
import re

files = ["output/domains.txt", "output/ip.txt", "output/md5.txt","output/sha256.txt","output/sha1.txt"]
downloader.downloadcyber()
jsonParser.parser()
def removparenthesesfromip(sourcefile , dest_file):
    with open(sourcefile) as f:
        input = f.read()
        pattern = re.sub(r"[\([{})\]]", "", input)
        with open(dest_file, 'w') as my_file:
         my_file.write(pattern)
removparenthesesfromip("output/ip_temp.csv","output/ip.txt")
removparenthesesfromip("output/domains_temp.txt","output/domains.txt")

def countLines(filename):
    with open(filename, 'r') as fp:
      for count, line in enumerate(fp):
        pass
    print('file ' , filename, 'has Total Lines', count + 1)
for file in files:
    countLines(file)
