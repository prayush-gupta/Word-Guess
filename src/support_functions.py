import requests
import sys
import tty
import termios



def get_single_char():
  """Reads a single character from tty without Enter."""
  fd = sys.stdin.fileno()
  old_settings = termios.tcgetattr(fd)
  try:
      tty.setraw(sys.stdin.fileno()) # Set to raw mode
      ch = sys.stdin.read(1)        # Read exactly 1 char
  finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) # Reset
  return ch
