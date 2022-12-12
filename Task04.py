""" Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
    Входные и выходные данные хранятся в отдельных текстовых файлах.       """

import re


def compress(dt):
    compressed_data = list()
    while len(dt) > 0:
        char = dt[0]
        result = re.match(f'{char}+', dt)
        compressed_data.append(f'{result.end()}{char}')
        dt = dt[result.end():]
    dt = ''.join(compressed_data)
    result = re.finditer(r"(1.)(1.)+", dt)
    span = list(map(lambda x: x.span(), result))
    for i in range(len(span)):
        result = re.finditer(r"(1.)(1.)+", dt)
        span = list(map(lambda x: x.span(), result))
        temp = format_data(dt[span[0][0]:span[0][1]])
        dt = dt.replace(dt[span[0][0]:span[0][1]], temp)
    return dt


def format_data(slice):
    temp = list(slice.replace('1', ''))
    temp.insert(0, str(-(slice.count('1'))))
    temp = ''.join(temp)
    return temp


def unpack(data):
    result_data = list()
    while len(data) > 0:
        try:
            result = re.match(r"\d.", data)
            start, stop = result.span()
            result_data.append(f"{int(data[start:stop][0]) * data[start:stop][1]}")
            data = data[stop:]
        except:
            result = re.match(r"-\d[a-z\s]{2,}", data)
            start, stop = result.span()
            result_data.append(f"{data[start+2:stop]}")
            data = data[stop:]
    return ''.join(result_data)


input_data = open('input.txt', 'r').readline()
data = compress(input_data)
print(f"Исходная строка: {input_data:^93}")
open('out.txt', 'w').write(data)
print(f"Закодированная строка: {data:^72}")
encoding_data = unpack(open('out.txt', 'r').readline())
print(f"Раскодированная строка: {encoding_data}")
print(f"Соответствие раскодированной строки к оригиналу: {input_data == encoding_data}")






