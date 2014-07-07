# -*- coding: utf-8 -*-

import random

def ls(a, s):
    found = False
    i = 0
    while i < len(a) and not found:
        if a[i] == s:
            found = True
        i += 1
    return found

if __name__ == "__main__":
    array = []
    for i in range(random.randint(0, 8)):
        array.append(random.randint(0, 13))

    value = input(u"Введите число: ")
    g = ls(array, value)

    if g:
        print "Элемент найден"
    else:
        print "Элемент не найден"

    print array