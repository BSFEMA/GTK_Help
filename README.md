# My question:  In the "Example_Glade.py + Example_Glade.glade" example, why does the ScrolledWindow not expand to full display the contents of the TreeView widget?  What do I need to do to correct this?

##

## Files

There are 2 programs that do the same thing here.

#1:  Example_GPT.py
* This was written by ChatGPT as an example to get me started.  This works and the TreeView is fully displayed.

#2:  Example_Glade.py + Example_Glade.glade
* This was written by me using Glade for the UI.  This works, but the ScrolledWindow is not expanded to fully display the contents of the TreeView widget.

##

## Screenshots:
Example_GPT.py  (after launching it)
* ![screenshot](https://github.com/BSFEMA/GTK_Help/blob/master/Example_GPT.png?raw=true)

Example_Glade.py  (after launching it)
* ![screenshot](https://github.com/BSFEMA/GTK_Help/blob/master/Example_Glade.png?raw=true)

Example_Glade.py  (after launching it, then manually expanding the window)
* ![screenshot](https://github.com/BSFEMA/GTK_Help/blob/master/Example_Glade_(Manually_Expanded).png?raw=true)

##

## Notes:
I realize that I can remove the ScrolledWindow and just have the TreeView in my Glade example, which would then full display the TreeView.  While this is almost what I want, I would still like to have a ScrolledWindow in order to get scrollbars in case there is a lot of data or the filenames are really large and would scroll off the screen.  Ultimately, this was just an example, and I'm looking to create something with more columns which may necessitate a horizontal scrollbar.

## Any suggestions on what I'm doing wrong in Glade or if there is a way to set the ScrolledWindow size based on the fully displayed TreeView size or any other solutions would be most appreciated. 