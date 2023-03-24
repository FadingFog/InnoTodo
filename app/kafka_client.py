import json

from aiokafka import AIOKafkaProducer
from kafka.errors import KafkaConnectionError
from loguru import logger

from app.config import settings


class KafkaClient:
    def __init__(self):
        self.producer = AIOKafkaProducer(bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS)
        self.started = False

    async def send_one(self, data: dict) -> None:
        if not self.started:
            try:
                await self.producer.start()
            except KafkaConnectionError:
                return logger.info("Kafka is unavailable. Skipping sending statistics.")
        json_data = json.dumps(data).encode('utf-8')
        logger.debug("KafkaClient sent message: " + str(data))
        await self.producer.send_and_wait(settings.KAFKA_TOPIC, json_data)
