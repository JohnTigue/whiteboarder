def get_favorite_color():
  return 'yellow'

def humanize_bytes(num, suffix='B'):
  """ Via # https://stackoverflow.com/a/1094933"""

  for unit in ['','K','M','G','T','P','E','Z']:
    if abs(num) < 1024.0:
      return "%3.1f%s%s" % (num, unit, suffix)
    num /= 1024.0
  return "%.1f %s%s" % (num, 'Yi', suffix)

    
