from redis import Redis
from elasticsearch import Elasticsearch

rd = Redis(host='127.0.0.1', db=2)

es = Elasticsearch([{
    'host': '127.0.0.1',
    'port': 9200
}])

