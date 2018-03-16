import redis
import xxhash
conn = redis.Redis('localhost')


def hashIt(url):
    return xxhash.xxh32(url).hexdigest()


def setUrl(longUrl):
    conn.hsetnx(hashIt(longUrl), "url", longUrl)

def flush():
    conn.flushall()


def getLongUrl(shortUrl):

    conn.hincrby(shortUrl, "count", 1)
    return conn.hget(shortUrl , "url")


def getCount(shortUrl):
    return  conn.hget(shortUrl, "count")


def getShortUrl(longUrl):
    return  hashIt(longUrl)

