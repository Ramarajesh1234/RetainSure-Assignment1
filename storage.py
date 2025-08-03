import random
import string
import re

url_store = {}

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def is_valid_url(url):
    regex = re.compile(
        r'^(http|https)://'
        r'(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?'
        r'(/|/\S+)?$'
    )
    return re.match(regex, url)
