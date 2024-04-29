def weather_float(filename, idx, skip=1, step=1):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines[skip::step]:
            tokens = line.strip().split(",")
            if len(tokens)-1 >= idx:
                if tokens[idx] != '':
                    token = float(tokens[idx])
                else:
                    token = None
            dataset.append(token)
    return dataset

def weather_int(filename, idx, skip=1, step=1):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines[skip::step]:
            tokens = line.strip().split(",")
            if len(tokens)-1 >= idx:
                if tokens[idx] != '':
                    token = float(tokens[idx])
                else:
                    token = None
            dataset.append(token)
    return dataset

def weather_str(filename, idx, skip=1, step=1):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines[skip::step]:
            tokens = line.strip().split(",")
            if len(tokens)-1 >= idx:
                if tokens[idx] != '':
                    token = tokens[idx]
                else:
                    token = None
            dataset.append(token)
    return dataset

def dates(filename, skip=1, step=1):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines[skip::step]:
            tokens = line.split(",")
            years = int(tokens[0])
            months = int(tokens[1])
            days = int(tokens[2])
            dataset.append([years, months, days])
    return dataset

def date2str(date):
    return f"{date[0]}/{date[1]:02d}/{date[2]:02d}"

def callfile(filestation,URL):
    import requests
    with open(filestation,"w",encoding="UTF-8-sig") as f:
        res = requests.get(URL)
        res.encoding = "UTF-8"
        f.write(res.text)