from app.decorator import logger1

@logger1('test1.json')
def tester(x, y, z, a=0, b=1, c=2):
    return x + y + z + a + b + c

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': [],
}

@logger1('test1.json')
def show_list(doc_list, dir_dict):
    res = []
    for info_doc in doc_list:
        res.append(f'{info_doc["type"]} "{info_doc["number"]}" "{info_doc["name"]}"')
    res2 = dir_dict
    return res, res2


@logger1('test.json')
def summator(x, y):
    return x + y


if __name__ == '__main__':
    tester(3, 4, 2)
    show_list(documents, directories)


    three = summator(1, 2)
    five = summator(2, 3)

    result = summator(three, five)

    print('result: ', result)
    print('result type: ', type(result))
