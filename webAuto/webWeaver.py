from selenium import webdriver
from selenium.webdriver.common.by import By
from weaverSolver import *
import pyautogui

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

solution = find_shortest_path(startWord, endWord, 1)

for word in solution[1:]:
    pyautogui.typewrite(word)
    pyautogui.press('enter')

print(solution)

driver.quit()
