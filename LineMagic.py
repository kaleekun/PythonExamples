# Author: KaLee

from IPython.core.magic import register_line_magic

@register_line_magic # I could call magic functions as if they are executables that can be run in a command prompt
def mymagic(args):
  print(type(args))      # --> Will be always a string, that needs to be parsed and worked with
  print(args.split())

%mymagic kalai selvan   # Usage as here.
