from tkinter import *

class Toolbar:
  def __init__(
    self,
    master,
    root,
    on_add_new_node,
    on_remove_node,
    on_size_click,
    on_root_click,
    on_min_click,
    on_max_click,
    on_print_click,
    on_reset_click
  ):
    # validate inputs
    vcmd = master.register(self.validate_num)
    self.vcmd = vcmd

    self.make_entry_field(
      root,
      label='Add node',
      btn_label='Add',
      submit_handler=on_add_new_node,
      row=0,
      column=0
    )

    self.make_entry_field(
      root,
      label='Remove node',
      btn_label='Remove',
      submit_handler=on_remove_node,
      row=3,
      column=0
    )

    # Size
    size_btn = Button(root, text="Size", command=on_size_click)
    size_btn.grid(row=1, column=2, sticky="WENS") 

    # Root
    root_btn = Button(root, text="Root", command=on_root_click)
    root_btn.grid(row=2, column=2, sticky="WENS") 

    # Min
    min_btn = Button(root, text="Min", command=on_min_click)
    min_btn.grid(row=3, column=2, sticky="WENS") 

    # Max
    max_btn = Button(root, text="Max", command=on_max_click)
    max_btn.grid(row=1, column=3, sticky="WENS") 

    # Print
    print_btn = Button(root, text="Print", command=on_print_click)
    print_btn.grid(row=2, column=3, sticky="WENS") 

    # Reset
    reset_btn = Button(root, text="Reset", command=on_reset_click)
    reset_btn.grid(row=3, column=3, sticky="WENS") 

  def make_entry_field(
    self,
    root,
    label,
    btn_label,
    submit_handler,
    row,
    column,
  ):
    root.grid_columnconfigure(column, pad=20)
    Label(root, text=label).grid(row=row, column=column, sticky="W")
    entry = Entry(root, validate='all', validatecommand=(self.vcmd, '%P'), width=10)
    entry.grid(row=row+1, column=column, sticky="W")
    btn = Button(
      root,
      text=btn_label,
      command=self.on_entry_submit(entry, submit_handler),
    )
    btn.grid(row=row+2, column=column, sticky="W")

  def validate_num(self, P):
    if str.isdigit(P) or P == '':
        return True
    else:
        return False
  
  def on_entry_submit(self, entry, callback):
    def handle():
      entry_value = entry.get()
      if entry_value:
        callback(int(entry_value))
        entry.delete(0, END)
      
    return handle
