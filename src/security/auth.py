"""
Roadmap:
- Authentication layer
- Validates UI clients
- Supports token-based auth
"""


def verify_user(user_name: str, password: str) ->bool:
    key_pass = "admin"

    if user_name == key_pass and password == key_pass:
        return True
    else:
        return False
