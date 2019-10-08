import redis
import json
#from rejson import Client, Path

def save_transaction(message):
  r = redis.Redis(host='localhost', port=6379, db=0)
  #r = redis.StrictRedis(host='localhost', port=6379, db=0)
  #r = Client.Client(host='localhost', port=6379, decode_responses=True)
  id = r.dbsize()
  id = id + 1
  #r.rpush(id,message)
  #while(r.llen(r)!=0):
   # print(r.rpop(r))
  r.set(id,message)
  #r.jsonset(id,message)
  print(r.expire(id,10800))
  print(r.get(id))
  print("Transactions stored, It will be deleted after 3 hrs !!")


