from faunadb.client import FaunaClient
from app.config import FAUNA_SECRET

client = FaunaClient(secret=FAUNA_SECRET)

collections = [
    # "users"
]
