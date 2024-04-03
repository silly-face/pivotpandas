from time import sleep
from random import uniform
from IPython.display import display, Image
import urllib.request

def printt(text: str) -> None:
  max_length = 65
  for line in text.split('\n'):
    cur_length = 0
    for word in line.strip():
      cur_length += len(word)
      if cur_length % max_length == 0:
          print()
      
      for i, x in enumerate(word):
        print(x, end='', flush=True)
        sleep(uniform(0.01, 0.05))
        
    print()
    sleep(uniform(.5, 0.8))

def show_image(url: str) -> None:
  with urllib.request.urlopen(url) as url:
    img = Image(url.read(), height=300, width=300)
    display(img)