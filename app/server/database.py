from beanie import init_beanie
import motor.motor_asyncio
from decouple import config

MONGO_DETAILS = config("MONGO_DETAILS")

from app.server.models.product_review import ProductReview


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS, tls=True, tlsAllowInvalidCertificates=True)

    await init_beanie(database=client.reviews, document_models=[ProductReview])