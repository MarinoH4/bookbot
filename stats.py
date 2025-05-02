def get_num_words(text):
    words = text.split()
    return len(words)

def count_character(text):
    text_l = text.lower()
    d = {}
    for car in text_l:
        if car in d:
            d[car] += 1
        else:
            d[car] = 1
    return d

def other_dict(text):
    car_dict = count_character(text)
    list_car = []
    for x in car_dict:
        d={}
        d["char"] = x
        d["num"] = car_dict[x]
        list_car.append(d)
    return sorted(list_car, key=lambda x: x["num"], reverse=True)