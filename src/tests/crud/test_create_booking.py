import logging
import pytest
import allure



from src.constants import api_constants
from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import post_request
from src.helpers.common_verification import *
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Utils

@allure.title("Validate post request")
@allure.description("Validate post request")
# @pytest.mark.positive

class TestPostRequest:
    @allure.title("Validate post positive request")
    @allure.description("Validate post request for booking with positive data")
    # @pytest.mark.positive
    def test_post_positive(self):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("Starting the test case")
        LOGGER.info("Starting the Testcase of TestCreateBooking")
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers= Utils().common_headers_json(),
            payload= payload_create_booking(),
            in_json= False
        )
        LOGGER.info("post request done")
        LOGGER.info("verification started")
        verify_http_status_code(response_data=response, expected_data=200)
        LOGGER.info(response.json())
        LOGGER.info(response.json()['bookingid'])
        verify_json_key_not_none(response.json()['bookingid'])


    @allure.title("Validate post negative request")
    @allure.description("Validate post request for booking with negative data")
    def test_post_negative(self):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("Starting the test case")
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload={},
            in_json=False
        )

        LOGGER.info("status code verification")
        verify_http_status_code(response_data=response, expected_data=500)






# class TestCreateBooking(object):
#
#     @pytest.mark.positive
#     @allure.title("Verify that Create Booking Status and Booking ID shouldn't be null")
#     @allure.description(
#         "Creating a Booking from the payload and verify that booking id should not be null and status code should be 200 for the correct payload")
#     def test_create_booking_positive(self):
#         LOGGER = logging.getLogger(__name__)
#         LOGGER.info("Starting the Testcase of TestCreateBooking")
#         LOGGER.info("POST Req Started.")
#         response = post_request(
#             url=APIConstants().url_create_booking(),
#             auth=None,
#             headers=Utils().common_headers_json(),
#             payload=payload_create_booking(),
#             in_json=False
#         )
#         LOGGER.info("POST Req Done.")
#         LOGGER.info("Now Verify")
#         verify_http_status_code(response_data=response, expected_data=200)
#         LOGGER.info(response.json())
#         LOGGER.info(response.json()["bookingid"])
#         verify_json_key_not_null(response.json()["bookingid"])
#         verify_json_key_gr_zero(response.json()["bookingid"])