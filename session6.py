# -*- coding: utf-8 -*-

# %%

import json
import csv

# %%
with open("hello.txt") as file:
    for line in file:
        print(line)

# %%

letter = "Dear Whoever..."

with open("letter.txt", "w") as file:
    file.write(letter)

# %%

with open("data/data.csv") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row[2])

# %%

programs = [
    ["MCSBT", "Masters in CSBT"],
    ["MDBI", "Masters in DBI"]
]

with open("programs.csv", "w") as file:
    writer = csv.writer(file)

    for program in programs:
        writer.writerow(program)

# %%

with open("data/data.json") as file:
    entries = json.load(file)

    for entry in entries:
        print(entry["_id"])

        for tag in entry["tags"]:
            print(tag)

# %%

programs = {
    "MDBI": "Masters in DBI",
    "MCSBT": "Masters in CSBT"
}

with open("programs.json", "w") as file:
    json.dump(programs, file)


# %%


with open("data/luke.json") as file:
    luke = json.load(file)

    print(luke["name"])
    print(luke["hair_color"])
    print(luke["mass"])

# %%
import csv
import json

with open("data/data.csv") as csv_file:
    reader = csv.DictReader(csv_file)

    # convert all rows to a list
    data = list(reader)

    with open("converted.json", "w") as json_file:
        json.dump(data, json_file)

    

# %%
