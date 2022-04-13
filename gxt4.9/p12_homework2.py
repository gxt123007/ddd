import json


def rebuild_num():
    with open("p13_test.json","r",encoding='utf-8') as f:
        data_list = json.load(f)
        new_data = []
        for item in data_list:
            tmp = tuple(item.values())
            new_data.append(tmp)
        return new_data


if __name__ == "__main__":
    print(rebuild_num())

