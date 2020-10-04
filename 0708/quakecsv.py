import csv

with open('all_week.csv', errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    depths, mags = [], []
    for row in reader:
        depths.append(float(row['depth']))
        mags.append(float(row['mag']))

print(f"总次数: {len(mags)}")
