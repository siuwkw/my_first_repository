bplist00�_WebMainResource�	
^WebResourceURL_WebResourceFrameName_WebResourceData_WebResourceMIMEType_WebResourceTextEncodingName_Shttps://raw.githubusercontent.com/BrockDSL/github_for_researchers/master/analyze.pyPO�<html><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">#data analyze

from csv import reader
from statistics import mean

#Perform our analysis
#We will find the average of our tempurature readings
with open("data.txt",'r') as data_file:
    csv_reader = reader(data_file)
    header = next(csv_reader)
    total = []
    for row in csv_reader:
        total.append(int(row[1]))

print("Average tempurature readings :", mean(total))
</pre></body></html>Ztext/plainUUTF-8    ( 7 N ` v � � ���                           �