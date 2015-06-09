#Fix errors

from subprocess import Popen, PIPE
from threading import Thread
from queue import Queue, Empty

io_q = Queue()

def stream_watcher(identifier, stream):
  for line in stream:
    io_q.put((identifier, line))
  if not stream.closed():
    stream.close()

proc = Popen('/home/dshikhar/Documents/my-code/python3/subprocess-module/', stdout=PIPE, stderr=PIPE)

thread(target=stream_watcher, name='stdout-watcher',
        args=('STDOUT', proc.stdout)).start()
Thread(target=stream_watcher, name='stderr-watcher',
        args=('STDERR', proc.stderr)).start()

def printer():
  while True:
    try:
      item = io_q.get(True, 1)
    except Empty:
      if proc.poll() is not None:
        break
      else:
        identifier, line = item
        print (identifier + ':', line)

Thread(target = printer, name = 'printer').start()
