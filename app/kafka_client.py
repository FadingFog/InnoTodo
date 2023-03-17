import json

from aiokafka import AIOKafkaProducer

from app import config


class KafkaClient:
    def __init__(self):
        self.producer = AIOKafkaProducer(bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS)

    async def send_one(self, data: dict):
        try:
            await self.producer.start()
            json_data = json.dumps(data).encode('utf-8')
            await self.producer.send_and_wait(config.KAFKA_TOPIC, json_data)
        finally:
            await self.producer.stop()


kafka_client = KafkaClient()
