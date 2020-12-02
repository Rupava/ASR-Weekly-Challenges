from PIL import Image
from collections import Counter
from selenium import webdriver

img_path = input("Enter your image path: ") 
url = "https://coolors.co/"
img = Image.open(img_path)
size = w,h = img.size
data = img.load()
colors = []
hex_list = []
color_names = []
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

for x in range (w):
    for y in range (h):
        color = data[x,y]
        hex_color = (''.join([hex(c)[2:].rjust(2,'0') for c in color]))
        colors.append(hex_color)

color_count = (Counter(colors))
hex_list = (list(color_count.keys()))

for x in range(len(hex_list)):
    driver.get(url + hex_list[x])
    color_names.append(driver.find_element_by_id("color-picker-page_preview_name").text)   

print('________________________________')
print('Your colors- ')
for x in range(len(color_names)): 
    print(hex_list[x] +': '+ color_names[x])
print('________________________________')

k=input("press close to exit") 