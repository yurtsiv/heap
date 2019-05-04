import uuid
from heap.node import Node
from heap.utils import * 

class Heap:
  def __init__(self):
    self._root = self.min = self.max = None
    self.size = self.complete_levels = 0
    self._max_heap = False 
    self.keys = []

  def toggle_max_heap(self):
    self._max_heap = not self._max_heap

    # to avoid fixing
    self.keys.sort(reverse=self._max_heap)
    self._root = None
    self.size = 0
    self.complete_levels = 0

    for key in self.keys:
      self._insert(self._create_node(key))
      self._handle_size_increase()
  
  def _handle_size_increase(self):
    self.size += 1
    self.complete_levels = math.floor(math.log2(self.size + 1))

  def _create_node(self, key):
    return Node(uuid.uuid4(), key)
  
  def _insert(self, node):
    if not self._root:
      self._root = node 
    else:
      insert(self._root, node, self.complete_levels, 0)

  # checks if heap is incorrect
  def _should_fix(self, root, child):
    if self._max_heap:
      # in max-heap root must be greater than its child
      return child.key > root.key 
    
    # in min-heap root must be smaller than its child
    return root.key > child.key

  def add(self, key):
    self.keys.append(key)
    node = self._create_node(key)
    self._insert(node)

    self._handle_size_increase()
    fix_heap(self._root, self._should_fix)

    if not self.max and not self.min:
      self.max = self.min = key
    elif key > self.max:
      self.max = key
    elif key < self.min:
      self.min = key

    if self._should_fix(self._root, node):
      self._root = node

  def draw(self, canvas, init_pos):
    draw_heap(
      self._root,
      None,
      init_pos,
      1,
      { 'canvas': canvas, 'tree_size': self.size }
    )
  
  def to_string(self):
    return {
      'in_order': traverse_in_order(self._root),
      'pre_order': traverse_pre_order(self._root),
      'post_order': traverse_post_order(self._root)
    }