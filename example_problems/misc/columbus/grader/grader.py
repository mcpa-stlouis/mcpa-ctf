"""
Grader file for Columbus problem
"""

def grade(autogen, key):
  if '1492' in key:
    return (True, 'Good work!')
  else:
    return (False, 'Nope')

"""
Hints:
  args: none

  returns:
    list of tuples [point value, hint]
    [("10", "Columbus sailed in?"), ("10", "Another hint")]
"""

def get_hints():
  return  [("10", "Columbus sailed in?"), ("10", "Another hint")]
