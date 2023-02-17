text = 'Requisitos' \
       'aws' \
       'python' \
       'django' \
       'mysql' \
       'postgresql' \
       'Beneficios' \
       'VR' \
       'VA' \
       'Auxilio Homeoffice'

split1 = 'Requisitos'
split2 = 'Beneficios'

texto = text.split(split1)[1].split(split2)
print(texto)
