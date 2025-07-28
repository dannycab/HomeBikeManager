
# In-memory API key store for demo (should be replaced in production)
api_keys = {}

def get_user_from_api_key(key: str):
    for user, k in api_keys.items():
        if k == key:
            return user
    return None
