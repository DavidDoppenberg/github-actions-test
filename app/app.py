import os
import sys
import argparse


def error(text):
    '''Helper method to raise consistent errors.'''
    raise RuntimeError(f"Invalid config: {text} Please check your .env file.")

def read_env(key, optional=False):
    ''''Read environment variable. Raises error if not optional and not found.'''
    value = os.getenv(key)
    if value:
        value = value.strip()
    if not value: 
        value = None
    if not optional and value is None:
        error(f"Missing key '{key}'.")
    return value

# CLI 
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", required=False)
args = parser.parse_args()

# ENV
test_var = read_env("TEST_VAR", optional=True)
secret = read_env("SECRET", optional=True)

print("Hello!")
print("CLI variable:", args.port)
print("ENV variable:", test_var)
print("Secret:", secret)
