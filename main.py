from fastapi import FastAPI
from fastapi_signals import TaskMiddleware

from app.api.routes import routes
from app.db import engine
from app.kafka_client import KafkaClient
from app.models.base import Base

app = FastAPI()
app.add_middleware(TaskMiddleware)

kafka_client = KafkaClient()


@app.on_event("startup")
async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def stop_kafka_client():
    await kafka_client.producer.stop()

app.include_router(routes, prefix='/api')
