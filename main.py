# This entrypoint file to be used in development. Start by reading README.md
import password_cracker
from unittest import main

"""
res = password_cracker.crack_sha1_hash("53d8b3dc9d39f0184144674e310185e41a87ffd5", True) # superman
print(res)

res = password_cracker.crack_sha1_hash("da5a4e8cf89539e66097acd2f8af128acae2f8ae", True) # q1w2e3r4t5
print(res)

res = password_cracker.crack_sha1_hash("ea3f62d498e3b98557f9f9cd0d905028b3b019e1", True) # bubbles1
print(res)
"""

# Run unit tests automatically
main(module='test_module', exit=False)
