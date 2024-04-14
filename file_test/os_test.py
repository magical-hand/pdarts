import os

env_vars = os.environ

for name, value in env_vars.items():
    print(f"{name}: {value}")