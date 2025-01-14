import allure
import pytest
import logging
from src.conftest import *
from src.helpers.payload_manager import *
from src.helpers.common_verification import *
from src.helpers.api_request_wrapper import *
from src.constants import api_constants

class TestE2E:
    @pytest.mark.envtoenv
    @allure.title("Validate Update > Delete > verify booking get deleted")
    @allure.description("validate end to end work flow for update > delete and verify it's got deleted")
    # booking= get_booking_id()
    # token =generate_token()
    def test_update_booking_with_id_token(self, create_token, get_booking_id):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("staring update request")
        booking = get_booking_id
        token = create_token
        urls= APIConstants().url_patch_put_delete(booking_id=booking)
        print(urls)

        response = put_requests(
            url=APIConstants().url_patch_put_delete(booking_id=booking),
            auth=None,
            headers=Utils().common_header_put_delete_patch_cookie(token=token),
            payload=payload_update_booking(),
            in_json=False
        )
        verify_http_status_code(response_data=response,expected_data=200)
        verify_response_key(response.json()["firstname"], "Rajesh")
        verify_response_key(response.json()["lastname"], "Brown")
        print(response.json())


    @allure.title("Delete booking id")
    @allure.description("Delete booking id and verify records")
    def test_delete_booking_id(self, create_token, get_booking_id):
        booking = get_booking_id
        token = create_token
        response = delete_requests(
            url=APIConstants().url_patch_put_delete(booking_id=booking),
            auth=None,
            headers=Utils().common_header_put_delete_patch_cookie(token=token),
            in_json=False
        )

        verify_http_status_code(response_data=response,expected_data=201)
        print(response.text)


    @allure.title("verify deleted booking id")
    @allure.description("check deleted booking id by using get request")
    def test_get_booking_id(self, get_booking_id):
        booking = get_booking_id
        response = get_request(
            url=APIConstants().url_patch_put_delete(booking_id=booking),
            auth=None
        )
        print(response.text)






