import hashlib

known_salts_file = open("known-salts.txt", "r")
known_salts = known_salts_file.read().splitlines()
known_salts_file.close()

top_passwords_file = open("top-10000-passwords.txt", "r")
top_passwords = top_passwords_file.read().splitlines()
top_passwords_file.close()

def crack_sha1_hash(hash, use_salts = False):
    salts = known_salts if use_salts else []
    payloads = generate_possible_payloads(top_passwords, salts)
    result = bruteforce_passwords(hash, payloads)
    if result == None:
      return "PASSWORD NOT IN DATABASE"
    else:
      if use_salts:
        return salt_lookup[result]
      else:
        return result

salt_lookup = {}

def generate_possible_payloads(passwords, salts):
  payloads = []
  for password in passwords:
    if(len(salts) > 0):
      for salt in salts:
        payloads.append(password + salt)
        payloads.append(salt + password)
        salt_lookup[password + salt] = password
        salt_lookup[salt + password] = password
    else:
      payloads.append(password)
  return payloads


def bruteforce_passwords(target_hash, passwords):
  for password in passwords:
    hash = hash_sha1(password)
    if target_hash == hash:
      return password
  return None


def hash_sha1(password):
  payload = bytes(password, "utf8")
  return hashlib.sha1(payload).hexdigest()