import json
from parse_data import ParseToJson
import logging
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """
    Return a payload witch contains the STATE as key and COUNTYNAME

    Args: event(dict) refers the URL as lambda event

    Returns: Dict: the payload response from convert_data object

    """

    start_time = time.time()
    json_data = ParseToJson()
    json_data.get_response(event['url'])
    json_data.parse_data()
    json_payload = json_data.convert_data()
    end_time = time.time() - start_time
    logger.info(f'the total time of execution was:{end_time}')

    if json_payload:
        logger.info('data successfully parsed')

        return {
            'statusCode': 200,
            'body': json_payload
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('data was not parsed')
        }
