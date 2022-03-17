import downloader
import jsonParser
import re

files = ["output/domains.csv", "output/ip.csv", "output/md5.csv","output/sha256.csv","output/sha1.csv"]
downloader.downloadcyber()
jsonParser.parser()
def removparenthesesfromip(sourcefile , dest_file):
    with open(sourcefile) as f:
        input = f.read()
        pattern = re.sub(r"[\([{})\]]", "", input)
        with open(dest_file, 'w') as my_file:
         my_file.write(pattern)
removparenthesesfromip("output/ip_temp.csv","output/ip.csv")
removparenthesesfromip("output/domains_temp.csv","output/domains.csv")

def countLines(filename):
    with open(filename, 'r') as fp:
      for count, line in enumerate(fp):


        pass
    print('file ' , filename, 'has Total Lines', count + 1)
for file in files:
    countLines(file)
