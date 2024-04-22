def weather_float(filename, idx):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines[1:]:
            tokens = line.split(",")
            token = float(tokens[idx])
            dataset.append(token)
    return dataset

def weather_int(filename, idx):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines[1:]:
            tokens = line.split(",")
            token = int(tokens[idx])
            dataset.append(token)
    return dataset

def dates(filename):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines[1:]:
            tokens = line.split(",")
            years = int(tokens[0])
            months = int(tokens[1])
            days = int(tokens[2])
            dataset.append([years, months, days])
    return dataset

def date2str(date):
    return f"{date[0]}/{date[1]:02d}/{date[2]:02d}"