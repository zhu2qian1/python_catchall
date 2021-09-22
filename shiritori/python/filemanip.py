import csv

testdata = ".\\src\\testdata01.csv"


f = open(file=testdata, mode="rt", encoding="utf-8")
c = csv.reader(f)
dat = [row for row in c]
