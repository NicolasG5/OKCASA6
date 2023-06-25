from django.contrib.auth.hashers import BasePasswordHasher

from django.contrib.auth.hashers import BasePasswordHasher

class PlainTextPasswordHasher(BasePasswordHasher):
    algorithm = 'plain_text'

    def salt(self):
        return ''

    def encode(self, password, salt):
        return password

    def verify(self, password, encoded):
        return password == encoded

    def safe_summary(self, encoded):
        return {'algorithm': self.algorithm, 'hash': encoded}

def make_password(password):
    hasher = PlainTextPasswordHasher()
    return hasher.encode(password, None)