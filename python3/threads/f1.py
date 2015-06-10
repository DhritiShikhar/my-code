import threading

def heron(a):
  """Calculates square root of a"""
  eps = 0.0000001
  old = 1
  new = 1
  while True:
    old, new = new, (new + a/new) / 2.0
    print (old, new)
    if abs(new-old) < eps:
      break
  return new

threading.Thread(heron, (99,)).start()
threading.Thread(heron, (999,)).start()
threading.Thread(heron, (1733,)).start()

c = input("Press a key to quit.")
