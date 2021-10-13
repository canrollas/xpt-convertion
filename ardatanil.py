import xport, csv
with xport.XportReader('AL_IGE_D.xpt') as reader:
    with open('out.csv', 'rb') as out:
        writer = csv.DictWriter(out, [f['name'] for f in reader.fields])
        for row in reader:
            writer.writerow(row)
