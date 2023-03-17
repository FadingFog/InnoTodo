import os

from dotenv import load_dotenv

load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+asyncpg://postgres:postgres@localhost:5432')

RABBIT_HOST = os.getenv('RABBIT_HOST', 'rabbitmq')
RABBIT_PORT = os.getenv('RABBIT_PORT', 5672)
RABBIT_QUEUE = os.getenv('RABBIT_QUEUE', 'statistics_queue')

KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'statistics')
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9093')
