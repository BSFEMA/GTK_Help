import os
import sys
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk as gtk


class Main():
    def __init__(self):
        # Setup Glade Gtk
        self.builder = gtk.Builder()
        self.builder.add_from_file(os.path.join(sys.path[0], "Example_Glade.glade"))  # Looking where the python script is located
        self.builder.connect_signals(self)
        # Get UI components
        window = self.builder.get_object("main_window")
        window.connect("delete-event", gtk.main_quit)
        window.set_title('File Browser')
        window.show()
        #
        scroll_window = self.builder.get_object("scroll_window")
        scroll_window.set_vexpand(True)
        scroll_window.set_hexpand(True)
        scroll_window.set_propagate_natural_width(True)
        scroll_window.set_propagate_natural_height(True)
        # Create a TreeViewColumn for the original filename
        renderer_text1 = gtk.CellRendererText()
        column_text1 = gtk.TreeViewColumn("Filename", renderer_text1, text=0)
        column_text1.set_sizing(gtk.TreeViewColumnSizing.AUTOSIZE)
        column_text1.set_resizable(True)
        # Create a TreeViewColumn for the new filename
        renderer_text2 = gtk.CellRendererText()
        column_text2 = gtk.TreeViewColumn("Filesize", renderer_text2, text=1)
        column_text2.set_sizing(gtk.TreeViewColumnSizing.AUTOSIZE)
        column_text2.set_resizable(True)
        # Create a TreeViewColumn for the checkbox
        renderer_toggle = gtk.CellRendererToggle()
        renderer_toggle.connect("toggled", self.on_cell_toggled)
        column_toggle = gtk.TreeViewColumn("Check", renderer_toggle, active=2)
        column_toggle.set_sizing(gtk.TreeViewColumnSizing.AUTOSIZE)
        column_toggle.set_resizable(True)
        # Create a TreeView and add the columns
        tree_grid = self.builder.get_object("tree_grid")
        tree_grid.append_column(column_text1)
        tree_grid.append_column(column_text2)
        tree_grid.append_column(column_toggle)
        #
        self.populate_model(sys.path[0])

    def on_cell_toggled(self, widget, path):
        liststore1 = self.builder.get_object("liststore1")
        liststore1[path][2] = not liststore1[path][2]

    def populate_model(self, folder_path):
        liststore1 = self.builder.get_object("liststore1")
        for filename in os.listdir(folder_path):
            filesize = os.path.getsize(os.path.join(folder_path, filename))
            liststore1.append([str(filename), str(filesize), True])


if __name__ == '__main__':
    main = Main()
    gtk.main()