import subprocess
import os
from scraping.getFromPlayStore import *
from scraping.utils import *


def main():
    # IDs dos aplicativos na loja e no site
    app_ids = {
        "1": "br.gov.saude.acs",
        "2": "br.gov.saude.esusaps.vacinacao",
        "3": "br.gov.saude.ac",
        "4": "br.gov.saude.esusaps.gestao"
    }

    app_ids_site = {
        "1": "territorio",
        "2": "app_vacinacao",
        "3": "esus_ac",
        "4": "app_gestor"
    }

    escolha = None
    while escolha not in app_ids and escolha not in app_ids_site:
        print("Escolha um aplicativo para coletar avaliações:")
        for key, value in app_ids_site.items():
            print(f"{key}: {value}")

        escolha = input("Digite o número do aplicativo: ")

        if escolha not in app_ids and escolha not in app_ids_site:
            print("Escolha inválida. Por favor, tente novamente.")

    def run_scrapy_site():
        os.chdir('scraping/satisfacao')
        app = app_ids_site[escolha]
        command = f"scrapy crawl scraping -a app={app}"
        subprocess.run(command, shell=True)
        os.chdir('..')

    def run_scrapy_app():
        csv_path = '../scraping_output.csv'
        fetch_and_save_reviews(app_ids[escolha], csv_path)


    run_scrapy_site()
    run_scrapy_app()
    sat_level('../scraping_output.csv')
    date_type('../scraping_output.csv')

