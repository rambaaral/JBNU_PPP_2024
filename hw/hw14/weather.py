def weather_list(filename, idxlen):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:

        lines = f.readlines()
        for line in lines:
            tokens = line.strip().split(",")
            if len(tokens)-1 >= idxlen:
                if not '' in tokens:
                    dataset.append(tokens)
    return dataset

def weather_float(list, idx, name=True):
    dataset = []
    if name == True:
        for i in range(len(list)):
            if i != 0:
                dataset.append(float(list[i][idx]))
    else:
        for i in range(len(list)):
            dataset.append(float(list[i][idx]))
    return dataset

def weather_int(list, idx, name=True):
    dataset = []
    if name == True:
        for i in range(len(list)):
            if i != 0:
                dataset.append(int(list[i][idx]))
    else:
        for i in range(len(list)):
            dataset.append(int(list[i][idx]))
    return dataset

def weather_str(list, idx, name=True):
    dataset = []
    if name == True:
        for i in range(len(list)):
            if i != 0:
                dataset.append(str(list[i][idx]))
    else:
        for i in range(len(list)):
            dataset.append(str(list[i][idx]))
    return dataset

def dates(list, year_idx=0 , month_idx=1, day_idx=2, name=True):
    dataset = []
    if name == True:
        for i in range(len(list)):
            if i != 0:
                years = int(list[i][year_idx])
                months = int(list[i][month_idx])
                days = int(list[i][day_idx])
                dataset.append([years, months, days])
    else:
        for i in range(len(list)):
            years = int(list[i][year_idx])
            months = int(list[i][month_idx])
            days = int(list[i][day_idx])
            dataset.append([years, months, days])
    return dataset

def date2str(date):
    return f"{date[0]}/{date[1]:02d}/{date[2]:02d}"

def callfile(filestation,URL):
    import requests
    with open(filestation,"w",encoding="UTF-8-sig") as f:
        res = requests.get(URL)
        res.encoding = "UTF-8"
        f.write(res.text.replace("\r", ""))