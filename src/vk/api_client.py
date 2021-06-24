import json
import requests


class VKApiClient:
    '''
        Класс для работы с vk api.
        Базовый запрос:
            https://api.vk.com/method/METHOD?PARAMS&access_token=TOKEN&v=V
        Документация vk api:
            https://vk.com/dev/manuals
    '''

    __BASE_QUERY = \
        'https://api.vk.com/{method}/{submethod}?{params}&access_token={token}&v={version}'
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
        if response.status != 200:
            pass
            # exception_msg =    
        data = response.json()


if __name__ == '__main__':
    cfg_path = 'config.json'
    with open(cfg_path, 'r') as cfg_file:
        cfg = json.load(cfg_file)
    
    print(cfg)
        