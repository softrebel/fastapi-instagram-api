import os
import motor.motor_asyncio


client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_URL"))
db = client.SinaDb


