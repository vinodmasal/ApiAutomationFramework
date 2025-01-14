from src.constants.api_constants import *
from src.helpers.api_request_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import *
import pytest

@pytest.fixture(scope="session")
def create_token():
    response = post_request(
        url= APIConstants().url_create_token(),
        auth=None,
        payload= payload_create_token(),
        headers= Utils().common_headers_json(),
        in_json= False
    )
    verify_http_status_code(response_data=response,expected_data=200)
    token= response.json()["token"]
    return token

@pytest.fixture(scope="session")
def get_booking_id():
    response = post_request(
        url= APIConstants().url_create_booking(),
        auth= None,
        headers=Utils().common_headers_json(),
        payload=payload_create_booking(),
        in_json=False
    )
    verify_http_status_code(response_data=response,expected_data=200)
    print(response.json())
    return response.json()['bookingid']
