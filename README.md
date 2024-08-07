# Ojo-Cibernetico
<p align="center"><img src="https://imgur.com/S1nOVCU.png"></p>

<p align="center">
    <a href="https://twitter.com/CyberEy3z">
      <img src="https://img.shields.io/badge/-TWITTER-black?logo=twitter&style=for-the-badge">
    </a>
    </a>
</p>

<p align="center">
  <br>
  <b>Disponible en</b>
  <br>
  <img src="https://imgur.com/1gjFW9H.png  ">
</p>

<p>
  <a style="margin-right: 10px;" href="https://github.com/elcasodepaz/Ojo-Cibernetico#instalaciónn">
    <img src="https://dabuttonfactory.com/button.png?t=INSTALL&f=Open+Sans&ts=15&tc=000&hp=25&vp=10&c=5&bgt=unicolored&bgc=00e2ff">
  </a>
  <a style="margin-right: 10px;" href="https://github.com/elcasodepaz/Ojo-Cibernetico#usage">
    <img src="https://dabuttonfactory.com/button.png?t=USAGE&f=Open+Sans&ts=15&tc=000&hp=25&vp=10&c=5&bgt=unicolored&bgc=00e2ff">
  </a>
  <a href="https://github.com/elcasodepaz/Ojo-Cibernetico#demo">
    <img src="https://dabuttonfactory.com/button.png?t=DEMO&f=Open+Sans&ts=15&tc=000&hp=25&vp=10&c=5&bgt=unicolored&bgc=00e2ff">
  </a>
</p>

Herramienta útil para rastrear la ubicación o el número de móvil, por lo que esta herramienta se puede llamar OSINT (Inteligencia de Fuentes Abiertas) o también recopilación de información. Estas herramientas permiten a los usuarios obtener datos sobre una persona o un dispositivo a partir de información disponible públicamente en internet.

Algunas de las funcionalidades que pueden ofrecer incluyen:


* Geolocalización: Permiten determinar la ubicación exacta de un dispositivo móvil utilizando GPS, redes Wi-Fi o torres de telefonía celular.

* Búsqueda de números de teléfono: Facilitan la búsqueda de información asociada a un número de teléfono, como el nombre del propietario, dirección y otros datos relevantes.

* Análisis de redes sociales: Pueden recopilar información de perfiles públicos en redes sociales, ayudando a construir un perfil más completo de una persona.

* Monitoreo de actividad en línea: Algunas herramientas permiten rastrear la actividad en línea de un individuo, incluyendo publicaciones, comentarios y otras interacciones en diversas plataformas.

* Alertas de cambios de información: Ofrecen la posibilidad de recibir notificaciones cuando hay cambios en la información pública relacionada con un número de teléfono o una ubicación específica.

* Visualización de ubicación en mapas: También pueden mostrarte la ubicación utilizando la API de mapas. Todo lo que tienes que hacer es copiar y pegar el enlace o hacer clic derecho y abrir el enlace para ver la ubicación en un mapa interactivo.
  

**Automatic IP Address Reconnaissance** is performed after the above information is received.

**This tool is a Proof of Concept and is for Educational Purposes Only, Seeker shows what data a malicious website can gather about you and your devices and why you should not click on random links and allow critical permissions such as Location etc.**

## How is this Different from IP GeoLocation

* Other tools and services offer IP Geolocation which is NOT accurate at all and does not give location of the target instead it is the approximate location of the ISP.

* Seeker uses HTML API and gets Location Permission and then grabs Longitude and Latitude using GPS Hardware which is present in the device, so Seeker works best with Smartphones, if the GPS Hardware is not present, such as on a Laptop, Seeker fallbacks to IP Geolocation or it will look for Cached Coordinates.  

* Generally if a user accepts location permsission, Accuracy of the information recieved is **accurate to approximately 30 meters**

* Accuracy depends on multiple factors which you may or may not control such as :
  * Device - Won't work on laptops or phones which have broken GPS
  * Browser - Some browsers block javascripts
  * GPS Calibration - If GPS is not calibrated you may get inaccurate results and this is very common

## Templates

Available Templates : 

* NearYou
* Google Drive (Suggested by @Akaal_no_one)
* WhatsApp (Suggested by @Dazmed707)
* Telegram
* Zoom (Made by @a7maadf)
* Google reCAPTCHA (Made by @MrEgyptian)

Create your own template ! 
Steps to let you create your template is described in this [how-to](./createTemplate.md)

Once your template is ready, **do not forget to propose it to the community via a PR (pull request)**

## probado en :

* Kali Linux
* Parrot OS
* BlackArch Linux
* Kali Nethunter
* Termux
* OSX - Monterey v.12.0.1

## Installation

### Kali Linux / Parrot OS / Termux

```
git clone https://github.com/elcasodepaz/Ojo-Cibernetico.git
cd Ojo-Cibernetico/
pip3 install -r requirements.txt
python3 Ojo-Cibernetico.py
```

### OSX
```bash
git clone https://github.com/elcasodepaz/Ojo-Cibernetico.git
cd Ojo-cibernetico/
pip3 install -r requirements.txt
python3 Ojo-Cibernetico.py
````

## Usage
Mostrar el menu ```Rastreador IP```

<img src="https://imgur.com/1r1haff.png" />

on the IP Track menu, you can combo with the seeker tool to get the target IP
<details>
<summary>:zap: Install Seeker :</summary>
- <strong><a href="https://github.com/thewhiteh4t/seeker">Get Seeker</a></strong>
</details>

Mostrar el menu ```Rastreador de Teléfonos```

<img src="https://imgur.com/8vvSM8o.png" />

on this menu you can search for information from the target phone number

Display on the menu ```Username Tracker```

<img src="https://imgur.com/EtceBhk.png"/>
on this menu you can search for information from the target username on social media

<details>
<summary>:zap: Author :</summary>
- <strong><a href="https://github.com/HunxByts">HunxByts</a></strong>
</details>
```


## Demo

**YouTube**

<a href="https://odysee.com/@thewhiteh4t:2/seeker_v126_demo:e">
  <img src="https://thumbnails.odycdn.com/optimize/s:1024:768/quality:85/plain/https://thumbs.odycdn.com/5ce9ed06e0ce8a995987dba0949dbc9a.webp">
</a>
