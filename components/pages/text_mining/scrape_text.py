
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import csv

def scrape_kickstarter(url):
    try:
        # Configurer le navigateur Selenium
        options = Options()
        options.headless = True  # Ne pas afficher la fenêtre du navigateur
        driver = webdriver.Chrome(options=options)

        # Ouvrir la page
        driver.get(url)

        # Attendre que la page se charge (ajustez le temps si nécessaire)
        sleep(3)

        # Récupérer le titre de la page
        title = driver.title

        # Extraire le contenu (ici, nous récupérons tous les paragraphes)
        paragraphs = driver.find_elements(By.TAG_NAME, 'p')
        content = "\n\n".join([p.text for p in paragraphs])

        # Fermer le navigateur
        driver.quit()

        return {"title": title, "content": content}
    except Exception as e:
        return f"Erreur lors du scraping : {e}"

def save_to_csv(data, filename="data/kickstarter.csv"):
    # Enregistrer le contenu dans un fichier CSV
    with open(filename, mode="w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Content"])
        writer.writerow([data["title"], data["content"]])



