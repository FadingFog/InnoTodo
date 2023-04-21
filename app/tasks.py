import datetime
import enum


class ActionEnum(str, enum.Enum):
    LIST_CREATE = "list_create"
    LIST_DELETE = "list_delete"
    NOTE_CREATE = "note_create"
    NOTE_DELETE = "note_delete"
    NOTE_MARKED_DONE = "note_marked_done"
    NOTE_MARKED_UNDONE = "note_marked_undone"


async def statistics_handler(user_id: int, action: str):
    from main import kafka_client

    data = {
        'user_id': user_id,
        'action': action,
        'timestamp': str(datetime.datetime.utcnow())
    }

    await kafka_client.send_one(data)
