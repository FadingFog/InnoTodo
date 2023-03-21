import json

from aiokafka import AIOKafkaProducer

from app.config import settings


class KafkaClient:
    def __init__(self):
        self.producer = AIOKafkaProducer(bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS)

    async def send_one(self, data: dict):
        try:
            await self.producer.start()
            json_data = json.dumps(data).encode('utf-8')
            await self.producer.send_and_wait(settings.KAFKA_TOPIC, json_data)
        finally:
            await self.producer.stop()


kafka_client = KafkaClient()
