#python arg file --> digunakan untuk secara langsung memasukkan argumen pada file melalui command prompt pemanggil 
#(argparse)      --> file python ini

import argparse
from datetime import datetime

def honorifikChoosen(curYear, callerYear):
    callerAge = curYear - callerYear
    return 'kakak' if callerAge < 30 else 'bapak'

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help = 'Masukkan Nama Anda')
parser.add_argument('-t', '--tanggallahir', required=True, help = 'Masukkan Tanggal Lahir Anda (DD-MM-YY)')
args = parser.parse_args()

curDate = datetime.now().year
honorifik = honorifikChoosen(curDate, int(args.tanggallahir.split('-')[-1]))

print("Terimakasih telah menggunakan panggildicoding.py pada tahun 2020 {} {}".format(honorifik, args.nama))
