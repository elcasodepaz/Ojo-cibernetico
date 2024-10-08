#!/usr/bin/python
# << Translated BY cyb3rREY3z >>
#                                                                         !!!!!Solo para Uso Etico!!!!!

# IMPORT MODULE

import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr

Bl = '\033[30m'  # VARIABLE BUAT WARNA CUYY
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'


# utilities

# decorator for attaching run_banner to a function
def is_option(func):
    def wrapper(*args, **kwargs):
        run_banner()
        func(*args, **kwargs)


    return wrapper


# FUNCTIONS FOR MENU
@is_option
def IP_Track():
    ip = input(f"{Wh}\n Ingrese la direccion IP objetivo : {Gr}")  # INPUT IP ADDRESS
    print()
    print(f' {Wh}++++++ {Gr}Mostrar informacion de direcciones IP {Wh}++++++')
    req_api = requests.get(f"http://ipwho.is/{ip}")  # API IPWHOIS.IS
    ip_data = json.loads(req_api.text)
    time.sleep(2)
    print(f"{Wh}\n IP objetivo   :{Gr}", ip)
    print(f"{Wh} Tipo de IP      :{Gr}", ip_data["type"])
    print(f"{Wh} Paiz            :{Gr}", ip_data["country"])
    print(f"{Wh} Codigo de paiz  :{Gr}", ip_data["country_code"])
    print(f"{Wh} Ciudad          :{Gr}", ip_data["city"])
    print(f"{Wh} Continente      :{Gr}", ip_data["continent"])
    print(f"{Wh} Codigo Continente  :{Gr}", ip_data["continent_code"])
    print(f"{Wh} Region          :{Gr}", ip_data["region"])
    print(f"{Wh} Codigo de Region:{Gr}", ip_data["region_code"])
    print(f"{Wh} Latitud         :{Gr}", ip_data["latitude"])
    print(f"{Wh} Longitud        :{Gr}", ip_data["longitude"])
    lat = int(ip_data['latitude'])
    lon = int(ip_data['longitude'])
    print(f"{Wh} Mapas           :{Gr}", f"https://www.google.com/maps/@{lat},{lon},8z")
    print(f"{Wh} UE              :{Gr}", ip_data["is_eu"])
    print(f"{Wh} Codigo Postal   :{Gr}", ip_data["postal"])
    print(f"{Wh} Codigo Llamada  :{Gr}", ip_data["calling_code"])
    print(f"{Wh} Capital         :{Gr}", ip_data["capital"])
    print(f"{Wh} Fronteras       :{Gr}", ip_data["borders"])
    print(f"{Wh} Bandera del Pais:{Gr}", ip_data["flag"]["emoji"])
    print(f"{Wh} ASN             :{Gr}", ip_data["connection"]["asn"])
    print(f"{Wh} ORG             :{Gr}", ip_data["connection"]["org"])
    print(f"{Wh} ISP             :{Gr}", ip_data["connection"]["isp"])
    print(f"{Wh} Dominio         :{Gr}", ip_data["connection"]["domain"])
    print(f"{Wh} ID              :{Gr}", ip_data["timezone"]["id"])
    print(f"{Wh} ABBR            :{Gr}", ip_data["timezone"]["abbr"])
    print(f"{Wh} DST             :{Gr}", ip_data["timezone"]["is_dst"])
    print(f"{Wh} Offset          :{Gr}", ip_data["timezone"]["offset"])
    print(f"{Wh} UTC             :{Gr}", ip_data["timezone"]["utc"])
    print(f"{Wh} Hora Actual     :{Gr}", ip_data["timezone"]["current_time"])


@is_option
def phoneGW():
    User_phone = input(
        f"\n {Wh}Ingrese el numero de telefono objetivo {Gr}Ex [+6281xxxxxxxxx] {Wh}: {Gr}")  # INPUT NUMBER PHONE
    default_region = "ID"  # DEFAULT NEGARA INDONESIA

    parsed_number = phonenumbers.parse(User_phone, default_region)  # VARIABLE PHONENUMBERS
    region_code = phonenumbers.region_code_for_number(parsed_number)
    jenis_provider = carrier.name_for_number(parsed_number, "en")
    location = geocoder.description_for_number(parsed_number, "id")
    is_valid_number = phonenumbers.is_valid_number(parsed_number)
    is_possible_number = phonenumbers.is_possible_number(parsed_number)
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region,
                                                                                with_formatting=True)
    number_type = phonenumbers.number_type(parsed_number)
    timezone1 = timezone.time_zones_for_number(parsed_number)
    timezoneF = ', '.join(timezone1)

    print(f"\n {Wh}========== {Gr}Mostrar informacion, numeros de telefono {Wh}==========")
    print(f"\n {Wh}Ubicacion          :{Gr} {location}")
    print(f" {Wh}Codigo de Region     :{Gr} {region_code}")
    print(f" {Wh}Zona Horaria         :{Gr} {timezoneF}")
    print(f" {Wh}Operador             :{Gr} {jenis_provider}")
    print(f" {Wh}Numero Valido        :{Gr} {is_valid_number}")
    print(f" {Wh}Numero Posible       :{Gr} {is_possible_number}")
    print(f" {Wh}Formato Internacional:{Gr} {formatted_number}")
    print(f" {Wh}Formato Movil        :{Gr} {formatted_number_for_mobile}")
    print(f" {Wh}Numero Original      :{Gr} {parsed_number.national_number}")
    print(f" {Wh}Formato E.164        :{Gr} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
    print(f" {Wh}codigo de Pais       :{Gr} {parsed_number.country_code}")
    print(f" {Wh}Numero local         :{Gr} {parsed_number.national_number}")
    if number_type == phonenumbers.PhoneNumberType.MOBILE:
        print(f" {Wh}Tipo             :{Gr} This is a mobile number")
    elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
        print(f" {Wh}Tipo             :{Gr} Este es un numero de linea fija")
    else:
        print(f" {Wh}Tipo                 :{Gr} Otro tipo de numero")


@is_option
def TrackLu():
    try:
        username = input(f"\n {Wh}Ingrese el nombre de usuario : {Gr}")
        results = {}
        social_media = [
            {"url": "https://www.facebook.com/{}", "name": "Facebook"},
            {"url": "https://www.twitter.com/{}", "name": "Twitter"},
            {"url": "https://www.instagram.com/{}", "name": "Instagram"},
            {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
            {"url": "https://www.github.com/{}", "name": "GitHub"},
            {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
            {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
            {"url": "https://www.youtube.com/{}", "name": "Youtube"},
            {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
            {"url": "https://www.behance.net/{}", "name": "Behance"},
            {"url": "https://www.medium.com/@{}", "name": "Medium"},
            {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
            {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
            {"url": "https://www.periscope.tv/{}", "name": "Periscope"},
            {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
            {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
            {"url": "https://www.stumbleupon.com/stumbler/{}", "name": "StumbleUpon"},
            {"url": "https://www.ello.co/{}", "name": "Ello"},
            {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.telegram.me/{}", "name": "Telegram"},
            {"url": "https://www.weheartit.com/{}", "name": "We Heart It"}
        ]
        for site in social_media:
            url = site['url'].format(username)
            response = requests.get(url)
            if response.status_code == 200:
                results[site['name']] = url
            else:
                results[site['name']] = (f"{Ye}Usuario no fue encontrado {Ye}!")
    except Exception as e:
        print(f"{Re}Error : {e}")
        return

    print(f"\n {Wh}========== {Gr}Mostrar informacion del nombre de usuario {Wh}==========")
    print()
    for site, url in results.items():
        print(f" {Wh}[ {Gr}+ {Wh}] {site} : {Gr}{url}")


@is_option
def showIP():
    respone = requests.get('https://api.ipify.org/')
    Show_IP = respone.text

    print(f"\n {Wh}========== {Gr}Mostrar informacion de tu IP {Wh}==========")
    print(f"\n {Wh}[{Gr} + {Wh}] Tu direccion Ip : {Gr}{Show_IP}")
    print(f"\n {Wh}==============================================")


# OPTIONS
options = [
    {
        'num': 1,
        'text': 'Rastreador de IP',
        'func': IP_Track
    },
    {
        'num': 2,
        'text': 'Muestra tu IP',
        'func': showIP

    },
    {
        'num': 3,
        'text': 'Rastreador de Numeros Telefonicos',
        'func': phoneGW
    },
    {
        'num': 4,
        'text': 'Rastreador de Nombres Usuario',
        'func': TrackLu
    },
    {
        'num': 0,
        'text': 'Salir',
        'func': exit
    }
]


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux
    else:
        _ = os.system('clear')


def call_option(opt):
    if not is_in_options(opt):
        raise ValueError('Option not found')
    for option in options:
        if option['num'] == opt:
            if 'func' in option:
                option['func']()
            else:
                print('No function detected')


def execute_option(opt):
    try:
        call_option(opt)
        input(f'\n{Wh}[ {Gr}+ {Wh}] {Gr}Presione Enter Para Continuar')
        main()
    except ValueError as e:
        print(e)
        time.sleep(2)
        execute_option(opt)
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Salir')
        time.sleep(2)
        exit()


def option_text():
    text = ''
    for opt in options:
        text += f'{Wh}[ {opt["num"]} ] {Gr}{opt["text"]}\n'
    return text


def is_in_options(num):
    for opt in options:
        if opt['num'] == num:
            return True
    return False


def option():
    # BANNER TOOLS
    clear()
    stderr.writelines(f"""

          ________Paz_Para_Mi_Hente___________
            ┌─┐┬ ┬┌┐ ┌─┐┬─┐╦═╗╔═╗╔═╗╦  ┌┬┐    
            │  └┬┘├┴┐├┤ ├┬┘╠╦╝║╣ ╠═╣║  │││    
            └─┘ ┴ └─┘└─┘┴└─╩╚═╚═╝╩ ╩╩═╝┴ ┴ 
         ____________Venezuela_________________
       {Wh}[ + ] cyberREALm + cyberREYez  [ + ]
    """)

    stderr.writelines(f"\n\n\n{option_text()}")


def run_banner():
    clear()
    time.sleep(1)
    stderr.writelines(f"""{Wh}
         
    {Wh}============================================================
    {Wh}{Gr}   Ojo Cibernetico + Rastrear Ip's, Telefonos y usuarios {Wh}
    {Wh}                               Follow Me On X {Gr}@CyberEy3z {Wh}
    {Wh}=============================================================
        """)
    time.sleep(0.5)


def main():
    clear()
    option()
    time.sleep(1)
    try:
        opt = int(input(f"{Wh}\n [ + ] {Gr}Seleccione Una Opcion : {Wh}"))
        execute_option(opt)
    except ValueError:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Porfavor, introduzca El Numero')
        time.sleep(2)
        main()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Salir')
        time.sleep(2)
        exit()
