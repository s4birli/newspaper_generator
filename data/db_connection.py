from pymongo import MongoClient
from configparser import ConfigParser


class Connection:
    def __init__(self):
        config = ConfigParser()
        config.read('config.ini')
        self.conn = str(config['DEFAULT']['connection_string'])
        self.client = MongoClient(self.conn)
        self.db = self.client.ContentorDb

    def get_active_urls(self):
        return self.db.Urls.find({'isActive': True})
    
    def get_active_requests(self, url_id):
        return self.db.Requests.find({'urlId': url_id, 'isActive': True})



def db():
    return Connection()


def get_active_urls_test():
    conn = Connection()
    return conn.db.Urls.find({'isActive': True})
