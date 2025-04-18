import csv


def csv_read(f, delimiter=';'):
    reader = csv.reader(f, delimiter=delimiter)
    header = next(reader)
    return [row for row in reader]


def csv_write(f, data):
    headers = list(data[0])
    writer = csv.DictWriter(f, fieldnames=headers, delimiter=";")
    writer.writerows(data)
