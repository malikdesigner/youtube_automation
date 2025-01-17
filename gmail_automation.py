from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import random
import time
from unidecode import unidecode

# Path to your Chrome executable
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Chrome options
chrome_options = ChromeOptions()
chrome_options.binary_location = chrome_path  # Specify the path to chrome.exe
chrome_options.add_argument("--disable-infobars")

# Add proxy settings if needed
proxy_ip = "45.67.85.64"
proxy_port = "80"
chrome_options.add_argument(f'--proxy-server={proxy_ip}:{proxy_port}')

# Specify the user profile path
profile_number = "Profile 9"
chrome_options.add_argument(f'--user-data-dir=C:/Users/Naveed/AppData/Local/Google/Chrome/User Data')
chrome_options.add_argument(f'--profile-directory={profile_number}')

# WebDriver service
service = ChromeService()

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

french_first_names = [
    "Amélie", "Antoine", "Aurélie", "Benoît", "Camille", "Charles", "Chloé", "Claire", "Clément", "Dominique",
    "Élodie", "Émilie", "Étienne", "Fabien", "François", "Gabriel", "Hélène", "Henri", "Isabelle", "Jules",
    "Juliette", "Laurent", "Léa", "Léon", "Louise", "Lucas", "Madeleine", "Marc", "Margaux", "Marie",
    "Mathieu", "Nathalie", "Nicolas", "Noémie", "Olivier", "Pascal", "Philippe", "Pierre", "Raphaël", "René",
    "Sophie", "Stéphane", "Suzanne", "Théo", "Thomas", "Valentin", "Valérie", "Victor", "Vincent", "Yves",
    "Zoé", "Adèle", "Adrien", "Alexandre", "Alice", "Alix", "Anatole", "André", "Angèle", "Anne",
    "Baptiste", "Basile", "Bernard", "Brigitte", "Céleste", "Céline", "Christophe", "Cyril", "Denis", "Diane",
    "Édouard", "Éléonore", "Émile", "Félix", "Florence", "Georges", "Gérard", "Guillaume", "Hugo", "Inès",
    "Jacques", "Jean", "Jeanne", "Joséphine", "Julien", "Laure", "Lucie", "Maëlle", "Marcel", "Martine",
    "Maxime", "Michel", "Nina", "Océane", "Paul", "Perrine", "Quentin", "Romain", "Solène", "Thérèse"
]

french_last_names = [
    "Leroy", "Moreau", "Bernard", "Dubois", "Durand", "Lefebvre", "Mercier", "Dupont", "Fournier", "Lambert",
    "Fontaine", "Rousseau", "Vincent", "Muller", "Lefèvre", "Faure", "André", "Gauthier", "Garcia", "Perrin",
    "Robin", "Clement", "Morin", "Nicolas", "Henry", "Roussel", "Mathieu", "Garnier", "Chevalier", "François",
    "Legrand", "Gérard", "Boyer", "Gautier", "Roche", "Roy", "Noel", "Meyer", "Lucas", "Gomez",
    "Martinez", "Caron", "Da Silva", "Lemoine", "Philippe", "Bourgeois", "Pierre", "Renard", "Girard", "Brun",
    "Gaillard", "Barbier", "Arnaud", "Martins", "Rodriguez", "Picard", "Roger", "Schmitt", "Colin", "Vidal",
    "Dupuis", "Pires", "Renaud", "Renault", "Klein", "Coulon", "Grondin", "Leclerc", "Pires", "Marchand",
    "Dufour", "Blanchard", "Gillet", "Chevallier", "Fernandez", "David", "Bouquet", "Gilles", "Fischer", "Roy",
    "Besson", "Lemoine", "Delorme", "Carpentier", "Dumas", "Marin", "Gosselin", "Mallet", "Blondel", "Adam",
    "Durant", "Laporte", "Boutin", "Lacombe", "Navarro", "Langlois", "Deschamps", "Schneider", "Pasquier", "Renaud"
]

# Randomly select a first name and a last name
your_first_name = random.choice(french_first_names)
your_last_name = random.choice(french_last_names)

# Generate a random number
random_number = random.randint(1000, 9999)

# Retirer les accents des prénoms et nom de famille
your_first_name_normalized = unidecode(your_first_name).lower()
your_last_name_normalized = unidecode(your_last_name).lower()

your_username = f"{your_first_name_normalized}.{your_last_name_normalized}{random_number}"

your_birthday = "02 3 1989"  # dd m yyyy exp : 24 11 2003
your_gender = "1"  # 1:F 2:M 3:Not say 4:Custom
your_password = "x,nscldsj123...FDKZ"

# Human-like delay function
def human_delay(min_delay=1, max_delay=3):
    time.sleep(random.uniform(min_delay, max_delay))

def fill_form(driver):
    try:
        driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")

        # Fill in name fields
        first_name = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "firstName"))
        )
        last_name = driver.find_element(By.NAME, "lastName")

        first_name.clear()
        human_delay()
        first_name.send_keys(your_first_name)

        last_name.clear()
        human_delay()
        last_name.send_keys(your_last_name)

        # Click next button
        next_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-LgbsSe"))
        )
        next_button.click()

        # Wait for birthday fields to be visible
        day_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "day"))
        )

        # Fill in birthday
        birthday_elements = your_birthday.split()
        month_dropdown = Select(driver.find_element(By.ID, "month"))
        month_dropdown.select_by_value(birthday_elements[1])

        human_delay()
        day_field.clear()
        day_field.send_keys(birthday_elements[0])

        human_delay()
        year_field = driver.find_element(By.ID, "year")
        year_field.clear()
        year_field.send_keys(birthday_elements[2])

        # Select gender
        gender_dropdown = Select(driver.find_element(By.ID, "gender"))
        gender_dropdown.select_by_value(your_gender)

        human_delay()
        next_button.click()

        # Create custom email
        time.sleep(2)
        if driver.find_elements(By.ID, "selectionc4"):
            create_own_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "selectionc4"))
            )
            create_own_option.click()

        create_own_email = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "Username"))
        )
        username_field = driver.find_element(By.NAME, "Username")
        username_field.clear()
        username_field.send_keys(your_username)

        human_delay()
        next_button.click()

        # Enter and confirm password
        password_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "Passwd"))
        )
        password_field.clear()
        password_field.send_keys(your_password)

        human_delay()
        confirm_passwd_div = driver.find_element(By.ID, "confirm-passwd")
        password_confirmation_field = confirm_passwd_div.find_element(By.NAME, "PasswdAgain")
        password_confirmation_field.clear()
        password_confirmation_field.send_keys(your_password)

        human_delay()
        next_button.click()

        time.sleep(4)

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        driver.quit()

fill_form(driver)
