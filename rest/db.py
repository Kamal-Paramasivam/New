import redis

# This function will return last 100 transactions from DB
def get_transactions():
   r = redis.Redis(host='localhost', port=6379, db=0)
   start = r.dbsize()-100
   end = r.dbsize()
   print("dbsize=%d start=%d" % (r.dbsize(),start))
   print("message%s" % (r.mget(start, end)))
   return r.mget(start, end)



