from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from weaverSolver import WeaverSolver
import pyautogui
import time
import sys

def init_webdriver(headless):
    chrome_options = Options()
    if headless:
        print("running in headless mode")
        chrome_options.add_argument("--headless")
    else:
        print("running in headed mode")
    print("initializing WebDriver...")
    try:
        driver = webdriver.Chrome(options=chrome_options)
        print("WebDriver initialized successfully")
    except Exception as e:
        print(f"Error initializing WebDriver: {e}")
        raise
    return driver

def scrape_start_end(driver):
    start_word_row = driver.find_element(By.CLASS_NAME, 'startWordRow') # get elements by class name
    end_word_row = driver.find_element(By.CLASS_NAME, 'endWordRow')

    # string together characters in block to get the start and end words
    startWord = (''.join([i.text for i in start_word_row.find_elements(By.CLASS_NAME, 'block')])).lower()
    endWord = (''.join([i.text for i in end_word_row.find_elements(By.CLASS_NAME, 'block')])).lower()

    return startWord, endWord

def automate_solution(solution):
    for i, word in enumerate(solution[1:]):
        pyautogui.typewrite(word)
        pyautogui.press('return')

def main(args):

    headless = False
    if (len(args) > 1 and args[1].lower() == "true"): # determine if the user wants headless mode or not
        headless = True

    driver = init_webdriver(headless=headless)
    print("Loading Webpage...\n")
    driver.get('https://wordwormdormdork.com/')

    start_word, end_word = scrape_start_end(driver=driver)

    print(f'Start Word: {start_word}\nEnd Word: {end_word}\n')
    
    word_length = len(start_word) # get the length of words
    solver = WeaverSolver(word_length=word_length) # init solver
    solution = solver.find_shortest_path(start=start_word, end=end_word) # solve word

    if not headless:
        automate_solution(solution=solution)
    
    print(*solution, sep=' -> ')
    
    if not headless:
        time.sleep(5) # wait a couple seconds before quiting driver

    driver.quit() # quit the webdriver and exit the program

if __name__ == "__main__":
    main(sys.argv)