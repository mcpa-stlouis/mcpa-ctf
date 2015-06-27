from hashlib import sha1


def grade(autogen, key):
    secretkey = "my_key_here"
    n = autogen.instance
    flag = sha1((str(n) + secretkey).encode('utf-8')).hexdigest()
    if flag.lower() in key.lower().strip():
        return True, "Correct!"
    else:
        return False, "Try Again."

def get_hints():
  return  [("10", "Think colors"), ("10", "Sometimes things can be the same color")]
