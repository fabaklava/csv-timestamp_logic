import csv
from dateutil.parser import parse
rows = []
with open('overlap_timestamp-sample.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        else:
            A = parse(row[4])
            B = parse(row[5])
            C = parse(row[6])
            D = parse(row[7])
            if B < A:
                rows.append([row[1], row[4]])
            if D < C:
                rows.append([row[1], row[4]])
with open('result.csv', mode='w',newline='') as result_file:
    i = 0
    employee_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(['TicketID','A Value'])
    while i < len(rows):
        employee_writer.writerow(rows[i])
        i += 1
