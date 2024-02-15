from dotenv import dotenv_values
import os

config = dotenv_values(".env")

print(config["DOMAIN"])
print(config["ADMIN_EMAIL"])
print(config["ROOT_URL"])

print(os.getenv("DOMAIN")) # this returns NONE because .env is not os environment
