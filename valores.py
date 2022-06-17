from bs4 import BeautifulSoup
import requests
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')

   
def GenerarPlantilla():
    return render_template("index.html",euribor_hoy=ObtenerEuribor(),gasolina95_hoy=ObtenerGasolina95(),gasolina98_hoy=ObtenerGasolina98())

def ObtenerEuribor():
    url = "https://www.expansion.com/mercados/euribor.html"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    rows = soup.find("div", attrs={"class": "col-4 izquierda"}).find_all("td")
    euribor_hoy = rows[7].get_text()

    return euribor_hoy

def ObtenerGasolina95():
    url = "https://gasolinabarata.info/precio-gasolina/"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    rows = soup.find("div", attrs={"class": "bloqueGasolina precioGasolina"}).find_all("div")
    gasolina95_hoy = rows[2].get_text()

    return gasolina95_hoy

def ObtenerGasolina98():
    url = "https://gasolinabarata.info/precio-gasolina/"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    rows = soup.find("div", attrs={"class": "bloqueGasolina precioGasolina"}).find_all("div")
    gasolina98_hoy = rows[5].get_text()

    return gasolina98_hoy


if __name__ == '__main__':
    app.run(host="localhost", port=9566)
