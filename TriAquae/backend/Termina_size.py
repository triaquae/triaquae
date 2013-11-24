# Utility functions for getting the terminal size (credit to Chuck
# Blake for the original code; see
# http://pdos.csail.mit.edu/~cblake/cls/cls.py).

def ioctl_GWINSZ(fd): #### TABULATION FUNCTIONS
  try: ### Discover terminal width
    import fcntl, termios, struct
    cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
  except:
    return None
  return cr

def terminal_size():
  ### decide on *some* terminal size
  # try open fds
  cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
  if not cr:
    # ...then ctty
    import os
    try:
      fd = os.open(os.ctermid(), os.O_RDONLY)
      cr = ioctl_GWINSZ(fd)
      os.close(fd)
    except:
      pass
  if not cr:
    # env vars or finally defaults
    try:
      import os
      env = os.environ
      cr = (env['LINES'], env['COLUMNS'])
    except:
      cr = (25, 80)
  # reverse rows, cols
  return int(cr[1]), int(cr[0])
#print terminal_size()
#print terminal_size()[1]
