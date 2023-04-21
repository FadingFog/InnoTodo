from app.utils import token_helper


def test_get_token_payload_return_payload(create_token):
    data = {"user_id": 1}
    encoded_jwt = create_token(data)

    payload = token_helper.get_token_payload(encoded_jwt)

    assert payload == data
