"""
# Python Version: 3.5
# Creator - GGbits
# Set: 2
# Challenge: 12
# https://cryptopals.com/sets/2/challenges/11
#
# Description:


ECB cut-and-paste
Write a k=v parsing routine, as if for a structured cookie. The routine should take:

foo=bar&baz=qux&zap=zazzle
... and produce:

{
  foo: 'bar',
  baz: 'qux',
  zap: 'zazzle'
}
(you know, the object; I don't care if you convert it to JSON).

Now write a function that encodes a user profile in that format, given an email address. You should have something like:

profile_for("foo@bar.com")
... and it should produce:

{
  email: 'foo@bar.com',
  uid: 10,
  role: 'user'
}
... encoded as:

email=foo@bar.com&uid=10&role=user
Your "profile_for" function should not allow encoding metacharacters (& and =). Eat them, quote them, whatever you want
to do, but don't let people set their email address to "foo@bar.com&role=admin".

Now, two more easy functions. Generate a random AES key, then:

Encrypt the encoded user profile under the key; "provide" that to the "attacker".
Decrypt the encoded user profile and parse it.
Using only the user input to profile_for() (as an oracle to generate "valid" ciphertexts) and
the ciphertexts themselves, make a role=admin profile.
"""
from collections import OrderedDict
from random import randint
from challenge11 import random_aes_key
from challenge10 import encrypt_ecb, decrypt_ecb
from challenge7 import encrypt_aes_128_ecb, decrypt_aes_128_ecb


def parse_variable_string(url_string):
    """
    Takes in url string and turns it into an object
    :param url_string: variable portion of url
    :return: variables [dic]
    """
    variable_dic = OrderedDict()
    variable_list = url_string.split("&")
    for s in variable_list:
        temp_list = s.split("=")
        variable_dic[temp_list[0]] = temp_list[1]
    return variable_dic


def ordered_dictionary_to_variable_string(dic):
    variable_strings = []
    for k, v in dic.items():
        variable_strings.append("=".join([k, v]))
    return "&".join(variable_strings)


def create_profile(email_address):
    """
    Create fake user profile
    :param email_address: email address of profile
    :return: variable_string
    """
    parsed_email = email_address
    for c in ['&', "="]:
        if c in email_address:
            parsed_email = parsed_email.replace(c, "")

    profile_dic = OrderedDict([('email', parsed_email), ('uid', str(randint(0, 10))), ('role', 'user')])
    return ordered_dictionary_to_variable_string(profile_dic)


def encrypt_profile(profile_string):
    """
    Encrypts profile string using aes key and ECB
    :param profile_string: variable string of profile
    :return: encrypted_profile [bytes string]
    """
    key = random_aes_key(16)
    encrypted_profile = encrypt_ecb(profile_string.encode(), key)
    return encrypted_profile, key


def decrypt_profile(encrypted_profile, key):
    return binary_remove_whitespace(decrypt_ecb(encrypted_profile, key)).decode()


def binary_remove_whitespace(string):
    return string.replace(b"\x04", b"")


if __name__ == '__main__':
    print(parse_variable_string("foo=bar&baz=qux&zap=zazzle"))
    profile = create_profile("mark@test.com")
    print(profile)
    encrypt_info = encrypt_profile(profile)
    print(encrypt_info)
    decrypt_info = decrypt_profile(encrypt_info[0], encrypt_info[1])
    print(decrypt_info)
