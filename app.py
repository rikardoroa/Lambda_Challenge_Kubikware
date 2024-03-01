import requests
import json
import pandas as pd
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class ParseToJson:

    def __init__(self):

        """
        Initializing attributes

        """

        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        self.body = str
        self.response = str
        self.payload = {}
        self.batches = pd.DataFrame()

    def get_response(self, url: str) -> list:

        """
        Return a list with the body data parsed from the URL

        Args: url(str) refers to the url used to get the request and extract the data

        Returns: list: the body response deserialized to obtain the parsed data

        """

        try:
            self.response = requests.get(url, headers=self.header)
            if self.response.status_code == 404:
                print('can not parse response')
            else:
                body = self.response.content.decode('utf-8')
                self.body = body.split('\n')
                return self.body
        except Exception as e:
            logger.info(f'can not return the body, please review request status code:{e}')

    def parse_data(self) -> pd.DataFrame:

        """
        Convert the parsed body into a pandas dataframe

        Returns: Pandas Dataframe that contains all the information related to the parsed data

        """

        try:
            rows = self.body[1:]
            columns = self.body[0].split('|')
            self.batches = pd.DataFrame()
            for item in rows:
                item_batches = pd.DataFrame(item.split("|")).transpose()
                self.batches = pd.concat([self.batches, item_batches], axis=0)
            self.batches.columns = columns
            self.batches = self.batches.dropna()
            self.batches = self.batches.reset_index(drop=True)
            return self.batches
        except Exception as e:
            logger.info(f'can not return the parse data, please review the process:{e}')

    def convert_data(self) -> dict:

        """
        Filter the STATE and COUNTYNAME values from the dataframe to create a json file with
        that information

        Returns: Json File that contains the STATE as key and COUNTYNAME as values for every STATE in the file

        """

        try:
            df_state_county = self.batches[['STATE', 'COUNTYNAME']]
            keys = [state for state in self.batches.STATE.unique()]
            for state in keys:
                mask = df_state_county[df_state_county.STATE == state]
                json_data = {state: [x for x in mask.COUNTYNAME]}
                self.payload.update(json_data)
            return self.payload
        except Exception as e:
            logger.info(f'can not create the json file, please review the process:{e}')
