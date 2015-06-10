#!/usr/bin/python3

#Shows if a number is prime number or not 

import threading

class PrimeNumber(threading.Thread):
  def __init__(self, number):
    threading.Thread.__init__(self)
    self.Number = number

  def run(self):
    counter = 2
    while counter*counter < self.Number:
      if self.Number % counter == 0:
        print ("%d is a prime number because %d = %d * %d" %(self.Number, self.Number, counter, self.Number/counter)) 
      counter = counter + 1
      print ("%d is a prime number" %(self.Number))

threads = []

while True:
  input = long(input("number: "))
  if input < 1:
    break
  threads = PrimeNumber(input)
  threads += [thread]
  thread.start()

for x in threads:
  x.join()
        
