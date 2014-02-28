#! /usr/bin/python
"""
Adds or removes window decorations from the specified window.
If the first argument begins with "0x", it is assumed to be a
hex-ID, otherwise a window name.
"""
import argparse
from os import path
from os import system as run
args = argparse.ArgumentParser(description='All up in your python, parsing your arguments.')
args.add_argument('window', help='Enter window name/title/ID')
args.add_argument('decor',type=int,help='0 = Decorations off, 1 = Decorations on.')
arg = args.parse_args()
def show_help():
	print ("fix_decor.py\r\n")
	print ("Usage:")
	print ("    fix_decor.py [window] [status]")
	print ("Where:")
	print ("    [window] May be the window name/title, or a hex window ID.")
	print ("             ID is assumed if argument begins with '0x'.")
	print ("    [status] = 0 for decorations off, 1 for on.\r\n")
try:
	import gtk.gdk
#	import whatthefuck
except ImportError:
	print ("\r\nCannot find python-gtk installed on this system.\r\n")
	print ("Seeing as how it's written in python, and how its whole purpose is to")
	print ("manipulate window elements drawn by GTK, you might see how that could")
	print ("be kind of an important thing to have installed.\r\n")
	print ("So use whatever package manager you like to use, for whichever distro")
	print ("or flavor you're currently smoking and go install it. Now. Right Now.")
	print ("Yes, I mean right now. No, don't go get a snack first, the chips will")
	print ("wait for you, really they will. Do it now. You have no excuse not to.\r\n")
	print ("Should probably also make sure you've got wmctrl installed as long as")
	print ("you're at it. Most distros come with it, but since you didn't already")
	print ("have python-gtk installed I'm forced to assume that there's something")
	print ("really wrong with you and your system.\r\n")
	exit()
import subprocess #from commands import get_ret_info
def get_ret_info(cmd):
	pipa = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, universal_newlines=True)  
	gigo = "".join(pipa.stdout.readlines()) 
	wtf = pipa.returncode
	if wtf is None: wtf = 0
	return wtf, gigo
if arg.window[0:2] == "0x":
	id = arg.window
else:
	id = get_ret_info('wmctrl -l | grep %s ' % arg.window)[1].split(' ')[0]
try:
	id=int(id,0) #get integer from hex ID
	w = gtk.gdk.window_foreign_new( id)
	if arg.decor == 0 or arg.decor == 1:
		w.set_decorations(arg.decor) # 0 disables decoration, 1 enables
		gtk.gdk.window_process_all_updates()
		gtk.gdk.flush()
	else:
		print ("Invalid Syntax.\r\n")
		show_help()
except:
	print ("Error:\r\n")
	show_help()
	
