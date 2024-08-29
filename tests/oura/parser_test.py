import requests
from ...ouraflask.oura import parser
import pandas as pd

USER_COLLECTION_URL = "https://api.ouraring.com/v2/sandbox/usercollection/"
REQUEST_PARAMS = {"start_date": "2021-11-01", "end_date": "2021-12-01"}
REQUEST_HEADERS = {"Authorization": "Bearer <token>"}


def test_parse_sleep_documents():
    response = requests.request(
        "GET",
        USER_COLLECTION_URL + "daily_sleep",
        headers=REQUEST_HEADERS,
        params=REQUEST_PARAMS,
    )
    sleep_df = parser.parse_sleep_documents(response)
    assert type(sleep_df) is pd.DataFrame
    raise AssertionError
