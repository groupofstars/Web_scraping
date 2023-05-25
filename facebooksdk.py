from elasticsearch import Elasticsearch

es = Elasticsearch()
es.indices.create(index='facebook')

import facebook

graph = facebook.GraphAPI(access_token='your-access-token', version='11.0')

posts = graph.get_object(id='me', fields='posts')['posts']['data']

for post in posts:
  es.index(
    index='facebook',
    doc_type='post',
    body={
      'id': post['id'],
      'message': post.get('message', ''),
      'created_time': post['created_time']
    }
  )
  query = {
    'query': {
        'match': {
        'message': 'keyword'
        }
    }
  }

results = es.search(index='facebook', doc_type='post', body=query)['hits']['hits']

for hit in results:
  print(hit['_source']['message'])