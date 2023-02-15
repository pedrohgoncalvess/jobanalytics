preference = {'pedro':'18','rafael':'20'}

#preference.update({'pedro':'20'})
nomes = list(preference.keys())
for nome in nomes:
    value = preference[nome]
    print(value.find('1'))
