import csv
csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)
with open('us-500.csv', 'rb') as f:
    reader = csv.reader(f, dialect='mydialect')
    for row in reader:
        print row
