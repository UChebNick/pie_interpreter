import uuid

def generate_random_string(length):
    return uuid.uuid4().hex[:length]