import uuid
from heap.node import Node
from heap.utils import * 

class Heap:
  root = None
  size = 0 
  levels = 0

  def root_key(self):
    if self.root:
      return self.root.key
    
    return None

  def add(self, key):
    node = Node(uuid.uuid4(), key)

    if not self.root:
      self.root = node 
      self.size = 1
      self.levels = 1
    else:
      insert(self.root, node, self.levels, 0)
      self.size += 1
      self.levels = math.floor(math.log2(self.size + 1))
      correct_heap(self.root)
      
      if key < self.root.key:
        self.root = node

  def draw(self, canvas, init_pos):
    draw(
      self.root,
      None,
      init_pos,
      1,
      { 'canvas': canvas, 'tree_size': self.size }
    )
  
  def to_string(self):
    return {
      'in_order': traverse_in_order(self.root),
      'pre_order': traverse_pre_order(self.root),
      'post_order': traverse_post_order(self.root)
    }