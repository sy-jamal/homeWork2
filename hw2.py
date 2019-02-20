import os;
print("started")
for root, dirs, files in os.walk("./factbook.json-master"):
    for file in files:
        if file.endswith(".json"):
            file_abs_path = os.path.abspath(file)
            cmd_line = "mongoimport --jsonArray --db test --collection docs --file "+ file_abs_path
            os.system(cmd_line)