<!-- LOGO -->
<div align="center" id="top">
<img src="logo.png" alt="image" border="0" width="50px">
  <h1 align="center">federica-bot</h1>
  <p align="center">
    Revolutionize Your Financial Tracking: Federica Bot Seamlessly Transfers Transaction Data from Your Emails Directly to Your BudgetBakers Wallet!
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de contenidos</summary>
  <ol>
    <li>
      <a href="#sobre-el-proyecto">Sobre el Proyecto</a>
    </li>
    <li>
      <a href="#ejecutar-localmente">Ejecutar localmente 🚀</a>
    </li>
    <li>
      <a href="#construido-con">Construido Con</a>
    </li>
  </ol>
</details>
<hr>

## Sobre el proyecto
Federica Bot is your automated aide designed to transition financial information from your emails directly to your BudgetBakers Wallet account. With a keen eye for detecting transaction details within emails, Federica Bot extracts and registers this data into your wallet, making financial tracking seamless and hassle-free.
<hr>

## Ejecutar localmente
**Se requiere tener instalado [Python](https://www.python.org/downloads/)**

1. **Instalar Git**
   Si aún no tiene Git instalado, puede descargarlo e instalarlo desde [aquí](https://git-scm.com/).
2. **Clonar el repositorio e ingresar a la carpeta**
   Abra una terminal y ejecute el siguiente comando para clonar el repositorio:
   ```
   git clone https://github.com/Jamir-boop/federica-bot.git
   ```
   Luego, navegue hasta la carpeta del proyecto:
   ```
   cd federica-bot
   ```
3. **Crear un entorno virtual de Python (venv)**
   Ejecute el siguiente comando para crear un entorno virtual:
   ```
   python3 -m venv myenv
   ```
   o si está en Windows:
   ```
   py -m venv myenv
   ```

4. **Activar el entorno virtual**
   En sistemas Unix o MacOS, ejecute:
   ```
   source myenv/bin/activate
   ```
   En Windows, ejecute:
   ```
   .\myenv\Scripts\activate
   ```
5. **Instalar las dependencias**
   Una vez activado el entorno virtual, instale las dependencias necesarias con el siguiente comando:
   ```
   pip install -r requirements.txt
   ```
6. **Configurar variables de entorno**
   Asegúrese de configurar las variables de entorno necesarias como `EMAIL` y `WALLET_PASSWORD` en un archivo `.env`.

7. **Ejecutar el bot**
   Finalmente, ejecute el bot con el siguiente comando:
   ```
   python main.py
   ```

Y eso es todo, ahora debería tener una instancia local de Federica Bot en funcionamiento.
<p align="right">(<a href="#top">ir al inicio</a>)</p>
<hr>

## Construido con
-   Python
-   Selenium.py
-   ...

<p align="right">(<a href="#top">ir al inicio</a>)</p>
