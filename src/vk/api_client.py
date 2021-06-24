import json
import requests
from pprint import pprint


class VKApiClient:
    '''
        Класс для работы с vk api.
        Базовый запрос:
            https://api.vk.com/method/METHOD?PARAMS&access_token=TOKEN&v=V
        Документация vk api:
            https://vk.com/dev/manuals
    '''

    __BASE_QUERY = \
        'https://api.vk.com/method/{method}.{submethod}?{params}&access_token={token}&v={version}'
    __API_VERSION = '5.131'

    def __init__(self, vk_token, logger):
        self.__vk_token = vk_token
        self.__logger = logger
    
    def get_group_posts(self):
        pass
    
    def get_group_name(self):
        pass
    
    def create_query(self, method, submethod, params):
        query = self.__BASE_QUERY.format(
            method=method,
            submethod=submethod,
            params=params,
            token=self.__vk_token,
            version=self.__API_VERSION
        )
        return query
    
    def get(self, query):
        resposne = requests.get(query)
        status = response.status_code
        if status != 200:
            # TODO: add logging
            exp_msg = 'Bad response status!'
            status_msg = f'status: {status}'
            query_msg = f'query: {query}'
            msg = '\n'.join([exp_msg, status_msg, query_msg])
            raise Exception(msg)
        else:
            pass
        data = response.json()


if __name__ == '__main__':
    cfg_path = 'config.json'
    with open(cfg_path, 'r') as cfg_file:
        cfg = json.load(cfg_file)
    
    logger = None
    vk_token = cfg['vk_token']

    vk_api_client = VKApiClient(vk_token, logger)   
    
    method = 'wall'
    submethod = 'get'
    params = 'owner_id=-86529522'
    query = vk_api_client.create_query(method, submethod, params)
    response = requests.get(query)
    print(response.status_code)
    # print(list(response.json().keys()))
    pprint(list(response.json()['response'].keys()))
    # pprint(response.json())
