import json
import pyautogui
import time
import subprocess
import webbrowser
import random
import string
from pyautogui import click, write


search_string = ''


def load_data_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data


def generate_random_string(length=5):
    """Generates a random string of uppercase and lowercase letters and digits."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def search_google():
    global search_string
    time.sleep(1)
    click(scale_coordinates(395, 122))
    
    
    random_str = generate_random_string()  
    search_string = random_str
    write(search_string)
    
    pyautogui.press('enter')
    time.sleep(2)


def scale_coordinates(x, y):
    """
    Converts given coordinates (x, y) from a 1366x768 resolution to the current screen resolution.
    :param x: The x-coordinate to be converted.
    :param y: The y-coordinate to be converted.
    :return: Scaled x and y coordinates based on the current screen resolution.
    """
    screen_width, screen_height = pyautogui.size()

    base_width = 1366
    base_height = 768

    ratio_x = screen_width / base_width
    ratio_y = screen_height / base_height

    scaled_x = int(x * ratio_x)
    scaled_y = int(y * ratio_y)

    return scaled_x, scaled_y

def perform_action(email, password):
    global search_string
    subprocess.run(["start", "msedge", "--in", "https://rewards.bing.com/welcome"], shell=True)

    time.sleep(5)
    pyautogui.hotkey('win', 'up')
    click(scale_coordinates(1212, 124))
    time.sleep(3)

    write(email)
    time.sleep(1)
    click(scale_coordinates(101, 478))
    time.sleep(2)
    click(scale_coordinates(801, 478))
    time.sleep(2)

    write(password)

    click(scale_coordinates(801, 515))
    time.sleep(2)

    click(scale_coordinates(695, 493))
    time.sleep(2)

    pyautogui.hotkey('ctrl', 't')
    
    random_str = generate_random_string()
    search_string = random_str
    write(search_string)
    pyautogui.press('enter')

    for i in range(10):
        search_google()

    pyautogui.hotkey('ctrl', 'shift', 'w')


def main():
    file_path = 'data.json'  
    data = load_data_from_json(file_path)

    for entry in data:
        email = entry.get('email')
        password = entry.get('password')
        
        perform_action(email, password)
        time.sleep(2)
        

if __name__ == '__main__':
    main()
