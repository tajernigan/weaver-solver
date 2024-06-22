from selenium import webdriver
from selenium.webdriver.common.by import By
from selenuim.webdriver.common.keys import Keys
from weaverSolver import *
import pyautogui
import time

# Initialize a web driver 
driver = webdriver.Chrome()
driver.get('https://wordwormdormdork.com/') 

start_word_row = driver.find_element(By.CLASS_NAME, 'startWordRow')
end_word_row = driver.find_element(By.CLASS_NAME, 'endWordRow')

startWord = (''.join([i.text for i in start_word_row.find_elements(By.CLASS_NAME, 'block')])).lower()
endWord = (''.join([i.text for i in end_word_row.find_elements(By.CLASS_NAME, 'block')])).lower()

print("start word:", startWord)
print("end word:", endWord)

time.sleep(60)

if len(startWord) != 4:
    driver.quit()
    raise RuntimeError("This program only supports weaver puzzles of 4 letter words")

solution = find_shortest_path(startWord, endWord, 1)

for i, word in enumerate(solution[1:]):
    currentblock = driver.find_element(By.XPATH, f'//*[@id="game-container"]/div[3]/div[1]/div[2]/div[1]/div[{i+1}]')
    currentblock.send_keys(word + Keys.RETURN)


print(solution[1:])

time.sleep(3) # wait a couple seconds before quiting driver

driver.quit()
