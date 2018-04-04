"""
*What is this pattern about?
This pattern is used when creating an object is costly (and they are
created frequently) but only a few are used at a time. With a Pool we
can manage those instances we have as of now by caching them. Now it
is possible to skip the costly creation of an object if one is
available in the pool.
A pool allows to 'check out' an inactive object and then to return it.
If none are available the pool creates one to provide without wait.
*What does this example do?
In this example queue.Queue is used to create the pool (wrapped in a
custom ObjectPool object to use with the with statement), and it is
populated with strings.
As we can see, the first string object put in "yam" is USED by the
with statement. But because it is released back into the pool
aftwerwards it is reused by the explicit call to sample_queue.get().
Same thing happens with "sam", when the ObjectPool created insided the
function is deleted (by the GC) and the object is returned.
*Where is the pattern used practically?
*References:
http://stackoverflow.com/questions/1514120/python-implementation-of-the-object-pool-design-pattern
https://sourcemaking.com/design_patterns/object_pool
*TL;DR80
Stores a set of initialized objects kept ready to use.
"""
import queue


class ObjectPool(object):

  def __init__(self, queue, autoget=False):
    self._queue = queue
    self._item = self._queue.get() if autoget else None

  def __enter__(self):
    if self._item is None:
      self._item = self._queue.get()
    return self._item

  def __exit__(self, exc_value, exc_type, traceback):
    if self._item is not None:
      self._queue.put(self._item)
      self._item = None

  def __del__(self):
    if self._item is not None:
      self._queue.put(self._item)
      self._item = None


def main():
  sample_q = queue.Queue()
  sample_q.put('one')
  obj_pool = ObjectPool(sample_q, autoget=True)
  with obj_pool as pool:
    print(pool)

  def test_pool(sample_q):
    sample_q.put('two')
    obj_pool = ObjectPool(sample_q, autoget=True)
    print('Inside function ', obj_pool._item)

  test_pool(sample_q)

  obj_pool1 = ObjectPool(sample_q, autoget=True)
  obj_pool2 = ObjectPool(sample_q, autoget=True)
  print('Outside function - obj', obj_pool1._item)
  print('Outside function - obj', obj_pool2._item)


if __name__ == '__main__':
  main()
