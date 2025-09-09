import requests
from bs4 import BeautifulSoup
import re
import os

BASE_URL = "https://www.coes.org.pe/Portal/browser/vistadatos"

def get_header():
    header = {
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://www.coes.org.pe",
        "Referer": "https://www.coes.org.pe/Portal/PostOperacion/Informes/EvaluacionMensual",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    } 
    return header

def get_data(url):
    data = {
        "baseDirectory": "Post Operación/Informes/Evaluación Mensual/",
        "url": url,
        "indicador": "S",
        "initialLink": "Evaluación Mensual",
        "orderFolder": "D"
    }
    return data

def obtain_html(url, headers, data, output_file=None):
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        html_content = response.text

        # Saving the html obtained - Just to debug
        if output_file:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(html_content)
            print(f"HTML guardado en: {os.path.abspath(output_file)}")

        return html_content
    else:
        print("Error:", response.status_code, response.text)
        return None


def obtain_year(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    year_number = []
    # Searching all <a elements in the HTML doc
    links = soup.find_all("a", class_="infolist-link")

    for link in links:
        
        texto = link.get_text(strip=True)
        if texto.isdigit():
            year_number.append(int(texto))
        else:
            id_attr = link.get("id", "")
            match = re.search(r"\b(20\d{2})\b", id_attr)  
            if match:
                year_number.append(int(match.group(1)))
    return year_number


def obtain_months(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    months = []

    links = soup.find_all("a", class_="infolist-link")
    for link in links:
        onclick_attr = link.get("onclick", "")
        if "openBlob" in onclick_attr:
            match = re.search(r"openBlob\('([^']+)", onclick_attr)
            if match:
                months.append(match.group(1))  # Example: Operación/Programa de Mantenimiento/Programa Mensual/2025/01_ENERO/
    return months

def download_xlsx_files(html_content, headers, output_dir="output_files"):
    os.makedirs(output_dir, exist_ok=True)
    soup = BeautifulSoup(html_content, "html.parser")

    rows = soup.find_all("tr", class_="selector-file-contextual")
    for row in rows:
        file_id = row.get("id", "")
        if file_id.endswith(".xlsx"):
            filename = os.path.basename(file_id)
            print(f"Descargando: {filename}")

            # Construir URL de descarga
            download_url = "https://www.coes.org.pe/Portal/browser/download"
            params = {"url": file_id}

            response = requests.get(download_url, headers=headers, params=params)

            if response.status_code == 200:
                filepath = os.path.join(output_dir, filename)
                with open(filepath, "wb") as f:
                    f.write(response.content)
                print(f"Guardado en {filepath}")
            else:
                print(f"Error {response.status_code} al descargar {filename}")

if __name__ == "__main__":
    headers = get_header()
    data = get_data("Post Operación/Informes/Evaluación Mensual/")
    
    # Obtain the main HTML doc
    html = obtain_html(BASE_URL, headers, data, "initial.html")
    year_list = obtain_year(html)

    ## Accesing to each year folder
    for year in year_list:
        data_per_anio = get_data(f"Post Operación/Informes/Evaluación Mensual/{year}/")
        html_per_anio = obtain_html(BASE_URL, headers, data_per_anio)

        ## Accesing to each month folder
        
        months_list = obtain_months(html_per_anio)
        for month in months_list:
            data_per_month = get_data(month)
            html_per_month = obtain_html(BASE_URL, headers, data_per_month)

            # Paso 4: descargar los excels de ese mes
            download_xlsx_files(html_per_month, headers, output_dir=f"output_files/{year}")
>>>>>>> downloading_data_for_all_months
