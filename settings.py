import os.path

def get_project_root() -> str:
    current_file = os.path.abspath(__file__)
    project_root = os.path.dirname(current_file)
    return project_root


WEBSITE = 'https://www.saucedemo.com/'

# MAIN SETTINGS
ROOT_DIR = get_project_root()
print(ROOT_DIR)
DATABASE_DIR = os.path.join(ROOT_DIR, "data_base")

print(DATABASE_DIR)
FAKE_USERS_BASE = os.path.join(DATABASE_DIR, "users.json")