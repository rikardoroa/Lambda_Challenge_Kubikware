import json
import pandas as pd
import pytest
from lambda_app.parse_data import ParseToJson
from unittest.mock import patch, Mock, MagicMock


@pytest.fixture()
def event_body():
    # creating an event for test the lambda procedure
    return {"url": "https://www2.census.gov/geo/docs/reference/codes2020/national_county2020.txt"}


@pytest.fixture()
def load_class():
    Parent_class = ParseToJson()
    return Parent_class


@pytest.fixture()
def event_response(event_body, load_class):
    event = event_body
    parse_event = load_class.get_response(event['url'])
    return parse_event


def test_get_response(event_response):
    assert len(event_response) > 0


@pytest.fixture()
def get_parse_data(load_class, event_response):
    body = event_response
    if body:
        batches = load_class.parse_data()
        return batches


def test_parse_data(get_parse_data):
    batches = get_parse_data
    assert batches.shape[0] > 0
    assert batches.notna().any is not False
    assert 'STATE' in batches.columns


def test_convert_data(get_parse_data, load_class):
    batches = get_parse_data
    if batches is not None:
        payload = load_class.convert_data()
        assert len(payload['AL']) > 0
        assert len(payload['VI']) > 0

