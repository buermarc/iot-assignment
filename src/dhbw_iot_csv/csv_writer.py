import json
import csv as csv_mod

class CsvWriter:
    csv_writer = None
    fieldnames = None
    f = None

    #  Initialisierung
    def __init__(self, fieldnames):
        CsvWriter.fieldnames = fieldnames
        f = open('csv_log', 'w')
        CsvWriter.f = f
        CsvWriter.csv_writer =  csv_mod.DictWriter(f,fieldnames)
        CsvWriter.csv_writer.writeheader()

    def __del__(self):
        CsvWriter.f.close()

    #  line: ist die bereits formatierte Zeile, die nur noch geschrieben wird.
    def write_line(line):
        '''
        line = json.dumps(line)
        for x in CsvWriter.fieldnames:
            line.replace(x,'')
        '''
        CsvWriter.csv_writer.writerow(line)
        CsvWriter.f.flush()

