import math

def insert(root, node, complete_levels, curr_level):
  if not root:
    return False

  # if on last complete level
  if curr_level == complete_levels - 1:
    if root.left == None:
      node.parent = root
      root.left = node
      return True

    if root.right == None:
      node.parent = root
      root.right = node
      return True
    
    return False
  
  if insert(root.left, node, complete_levels, curr_level + 1):
    return True
  
  return insert(root.right, node, complete_levels, curr_level+1)

def fix_heap(root, should_fix):
  if not root or (not root.left and not root.right):
    return

  prev_root_parent = root.parent
  if root.left and should_fix(root, root.left):
    root.left.substitute_with_parent()
    fix_heap(prev_root_parent, should_fix)
  elif root.right and should_fix(root, root.right):
    root.right.substitute_with_parent()
    fix_heap(prev_root_parent, should_fix)
  else:
    fix_heap(root.left, should_fix)
    fix_heap(root.right, should_fix)


def draw_heap(root, rel_side, parent_pos, curr_depth, static_params):
  if not root:
    return

  canvas, tree_size = static_params['canvas'], static_params['tree_size']

  horizontal_offset = (tree_size * 50) / math.pow(curr_depth, 2)
  vertical_offset = 50

  new_pos = { 'y': parent_pos['y'] + vertical_offset, 'x': None }

  if curr_depth == 1:
    new_pos = parent_pos
  elif rel_side == 'left':
    new_pos['x'] = parent_pos['x'] - horizontal_offset 
  else:
    new_pos['x'] = parent_pos['x'] + horizontal_offset
  
  canvas.create_text(new_pos['x'], new_pos['y'], text=root.key, font=24)
  if curr_depth != 1:
    canvas.create_line(
      parent_pos['x'],
      parent_pos['y'] + 10,
      new_pos['x'],
      new_pos['y'] - 10
    )

  if not root.left and not root.right:
    return

  if root.left:
    draw_heap(root.left, 'left', new_pos, curr_depth+1, static_params)

  if root.right:
    draw_heap(root.right, 'right', new_pos, curr_depth+1, static_params)

def traverse_in_order(root):
  if not root:
    return ''
  
  if not root.left and not root.right:
    return str(root.key) + ' '
  
  return traverse_in_order(root.left) + str(root.key) + ' ' + traverse_in_order(root.right)

def traverse_pre_order(root):
  if not root:
    return ''
  
  if not root.left and not root.right:
    return str(root.key) + ' '
  
  return str(root.key) + ' ' + traverse_pre_order(root.left) + traverse_pre_order(root.right)

def traverse_post_order(root):
  if not root:
    return ''
  
  if not root.left and not root.right:
    return str(root.key) + ' '
  
  return traverse_post_order(root.left) + traverse_post_order(root.right) + str(root.key) + ' '
