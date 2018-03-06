import json


def load_data(filepath):
    with open(filepath, 'r', encoding="Latin-1") as file_handler:
        data1 = json.load(file_handler)
        return data1

from barselon import load_data

def get_biggest_bar(data):
    data=load_data("bar.txt")
    parametres= data["features"][2]["properties"]["Attributes"]["SeatsCount"]
    print(parametres)


def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    print(get_biggest_bar(load_data("bar.txt")))
