import pytest
import allure
import logging

from src.constants import api_constants
from src.constants.api_constants import APIConstants
from src.helpers import api_request_wrapper
from src.helpers import common_verification
from src.helpers import payload_manager


@allure.title("verify get request")
@allure.description("validating get request for booking")
@pytest.mark.positive

# @logging.
def test_get_request():
    responce = api_request_wrapper.get_request(
        url=APIConstants().url_get_booking()

    )
    common_verification.verify_http_status_code(response_data=responce, expected_data= 200)