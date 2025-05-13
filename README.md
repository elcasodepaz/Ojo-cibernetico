# 🧠 Ojo-Cibernético

<p align="center">
  <img src="https://github.com/elcasodepaz/Ojo-cibernetico/blob/main/images/menu1.png" alt="Menu Ojo-Cibernetico" />
</p>

<p align="center">
  <strong>🌐 Disponible En:</strong><br>
  <img src="https://github.com/elcasodepaz/Ojo-cibernetico/blob/main/images/kalinparrot.png" alt="Idiomas Disponibles" width="300" style="border: 3px solid blue;">
</p>

<p align="center">
  <a href="#instalación">
    <img src="https://dabuttonfactory.com/button.png?t=INSTALACIÓN&f=Open+Sans&ts=15&tc=000&hp=25&vp=10&c=5&bgt=unicolored&bgc=ffdf00" alt="Botón de Instalación">
  </a>
  <a href="#uso">
    <img src="https://dabuttonfactory.com/button.png?t=USO&f=Open+Sans&ts=15&tc=000&hp=25&vp=10&c=5&bgt=unicolored&bgc=00e2ff" alt="Botón de Uso">
  </a>
  <a href="#demo">
    <img src="https://dabuttonfactory.com/button.png?t=DEMO&f=Open+Sans&ts=15&tc=000&hp=25&vp=10&c=5&bgt=unicolored&bgc=ff0000" alt="Botón de Demo">
  </a>
</p>

---

## 🧪 Probado en

- Kali Linux
- Parrot OS
- Kali Nethunter
- Termux
- macOS Monterey v12.0.1

---

## 🔧 Instalación

### Linux / Parrot OS / Termux / macOS

> ⚠️ **IMPORTANTE**: Para evitar errores como `externally-managed-environment`, recomendamos usar un entorno virtual.

```bash
# 1. Clona el repositorio
git clone https://github.com/elcasodepaz/Ojo-cibernetico.git
cd Ojo-cibernetico/

# 2. Crea un entorno virtual
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instala las dependencias
pip install -r requirements.txt

# 4. Ejecuta la herramienta
python3 Ojo-cibernetico.py
