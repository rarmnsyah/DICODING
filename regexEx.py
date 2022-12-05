#file python sebagai contoh penggunaan regex

import re
#regex (regular expression), yaitu library searching berdasarkan pola tertentu yang telah ditentukan

pola = '^a...s$' #hal ini berarti kita mencari kata dengan awalan a dan akhiran s | titik berarti panjang kata, dalam konteks pola kali ini terdapat 5 huruf

string_test = ['abysss', 'abrws', 'mantap']

hasil = [re.match(pola, string) for string in string_test]
# hasil = re.match(pola, string_test[0])

print(hasil) #None, match, None