from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from weaverSolverBDBFS import find_shortest_path, backTrack
import pyautogui
import json
import time

# functions for trying to send keys using 
def try_send(driver, by, value, wait_time, keys):
    try:
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((by, value))).send_keys(keys)
    except Exception as e:
        print(f"Element not found or not interactable within {wait_time} seconds")

# Initialize a web driver 
driver = webdriver.Chrome()
driver.get('https://wordwormdormdork.com/') 

start_word_row = driver.find_element(By.CLASS_NAME, 'startWordRow')
end_word_row = driver.find_element(By.CLASS_NAME, 'endWordRow')

startWord = (''.join([i.text for i in start_word_row.find_elements(By.CLASS_NAME, 'block')])).lower()
endWord = (''.join([i.text for i in end_word_row.find_elements(By.CLASS_NAME, 'block')])).lower()

print("start word:", startWord)
print("end word:", endWord)

if len(startWord) != 4:
    driver.quit()
    raise RuntimeError("This program only supports weaver puzzles of 4 letter words")

with open('src/files/graph.json', 'r') as infile:
    map = json.load(infile)

solution = find_shortest_path(startWord, endWord, map)

for i, word in enumerate(solution[1:]):
    pyautogui.typewrite(word)
    pyautogui.press('return')


print(solution[1:])

time.sleep(3) # wait a couple seconds before quiting driver

driver.quit()
