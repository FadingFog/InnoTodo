from fastapi import FastAPI
from fastapi_signals import TaskMiddleware

from app.api.routes import routes
from app.kafka_client import KafkaClient

app = FastAPI()
app.add_middleware(TaskMiddleware)

kafka_client: KafkaClient


@app.on_event("startup")
async def init_kafka_client():
    global kafka_client
    kafka_client = KafkaClient()


@app.on_event("shutdown")
async def stop_kafka_client():
    await kafka_client.producer.stop()

app.include_router(routes, prefix='/api')
