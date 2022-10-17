from beanie import init_beanie
import motor.motor_asyncio
from decouple import config

MONGO_DETAILS = config("MONGO_DETAILS")

from app.server.models.property import Property


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS, tls=True, tlsAllowInvalidCertificates=True)

    await init_beanie(database=client.properties, document_models=[Property])