import os
import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class FileBrowserWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="File Browser")
        self.set_border_width(10)

        # Create a ListStore and specify the data types
        self.liststore = Gtk.ListStore(str, str, bool)
        self.populate_model(sys.path[0])  # specify your folder path here

        # Create a TreeViewColumn for the filename
        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("Filename", renderer_text, text=0)

        # Create a TreeViewColumn for the filesize
        renderer_text = Gtk.CellRendererText()
        column_text2 = Gtk.TreeViewColumn("Filesize", renderer_text, text=1)

        # Create a TreeViewColumn for the checkbox
        renderer_toggle = Gtk.CellRendererToggle()
        renderer_toggle.connect("toggled", self.on_cell_toggled)
        column_toggle = Gtk.TreeViewColumn("Check", renderer_toggle, active=2)

        # Create a TreeView and add the columns
        self.treeview = Gtk.TreeView(model=self.liststore)
        self.treeview.append_column(column_text)
        self.treeview.append_column(column_text2)
        self.treeview.append_column(column_toggle)

        # Create a button for printing the selected files
        button = Gtk.Button(label="Print Selected Files")
        button.connect("clicked", self.on_button_clicked)

        # Add the TreeView and the button to a vertical box
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box.pack_start(self.treeview, True, True, 0)
        self.box.pack_start(button, False, False, 0)
        self.add(self.box)

    def populate_model(self, folder_path):
        for filename in os.listdir(folder_path):
            filesize = os.path.getsize(os.path.join(folder_path, filename))
            self.liststore.append([filename, str(filesize), True])

    def on_cell_toggled(self, widget, path):
        self.liststore[path][2] = not self.liststore[path][2]

    def on_button_clicked(self, widget):
        for row in self.liststore:
            if row[2]:  # if the checkbox is checked
                print(f"Filename: {row[0]}, Filesize: {row[1]}")


win = FileBrowserWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
