def filtr(data):
    return {key: " ".join(value[0]) for key, value in data.items() if
            ("(п/г 2)" not in " ".join(value[0]))
            and ('Зотова О.Н.' not in " ".join(value[0]))
            and ("(начальный курс)" not in " ".join(value[0]))
            and "Медведева Н.М." not in " ".join(value[0])
            and "Общая физическая подготовка" not in " ".join(value[0])}

def summator228(date):
    s = 0
    match date[5:7]:
        case "09":
            s+=0
        case "10" | "12":
            s+=30
        case "11":
            s+=31
    s+= int(date[8:])
    return s

