import csv, datetime
from collections import Counter


with open(city_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    starts = []
    ends = []
    for row in reader:
        starts.append(row['Start Station'])
        ends.append(row['End Station'])

    start_count = Counter(starts)
    end_count = Counter(ends)

    popular_start = start_count.most_common(1)[0][0]
    popular_end = end_count.most_common(1)[0][0]

return(popular_start,popular_end)
