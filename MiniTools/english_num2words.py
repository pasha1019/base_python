import pprint


from num2words import num2words

dict_spelling = {}
for i in range(1,1000):
    dict_spelling[i] = num2words(i)
pprint.pprint(dict_spelling, sort_dicts=True)
