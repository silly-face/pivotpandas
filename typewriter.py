from time import sleep
from random import uniform
import sys

def printt(text: str) -> None:
  for line in text.split('\n'):
    for x in line.strip():
      sys.stderr.write(x)
      sleep(uniform(0.02, 0.1))
    print()
    sleep(uniform(.5, 0.8))

printt("Dit is best een lange tekst, maar dit zou ontzettend smooth moeten gaan. \n Geen idee waarom dit moeilijk werkt")