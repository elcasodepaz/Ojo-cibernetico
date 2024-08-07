  1 #!/usr/bin/python$
  2 # << Translated BY cyb3rREY3z >>$
  3 #                                                                         !!!!!Solo para Uso Etico!!!!!$
  4 $
  5 # IMPORT MODULE$
  6 $
  7 import json$
  8 import requests$
  9 import time$
 10 import os$
 11 import phonenumbers$
 12 from phonenumbers import carrier, geocoder, timezone$
 13 from sys import stderr$
 14 $
 15 Bl = '\033[30m'  # VARIABLE BUAT WARNA CUYY$
 16 Re = '\033[1;31m'$
 17 Gr = '\033[1;32m'$
 18 Ye = '\033[1;33m'$
 19 Blu = '\033[1;34m'$
 20 Mage = '\033[1;35m'$
 21 Cy = '\033[1;36m'$
 22 Wh = '\033[1;37m'$
 23 $
 24 $
 25 # utilities$
 26 $
 27 # decorator for attaching run_banner to a function$
 28 def is_option(func):$
 29     def wrapper(*args, **kwargs):$
 30         run_banner()$
 31         func(*args, **kwargs)$
 32 $
 33 $
 34     return wrapper$
 35 $
 36 $
 37 # FUNCTIONS FOR MENU$
 38 @is_option$
 39 def IP_Track():$
 40     ip = input(f"{Wh}\n Ingrese la direccion IP objetivo : {Gr}")  # INPUT IP ADDRESS$
Ghost.py                                                                                                                     40,86          Top
-- VISUAL --                                                                                                                        40 
