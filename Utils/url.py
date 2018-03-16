import validators
from Utils import cache

def validateUrl(url):
    if not validators.url(url):
        return False
    else:
        return True

def transformSuccessResponse(url):

    return  {
        "payload": url,
        "status": "OK",
        "status_codes": []
    }

def transformErrorResponse():

    return  {
        "status": "FAILED",
        "status_codes": ["INVALID_URLS"]
    }


def getShortUrl(url):
    if not validateUrl(url):
        return None
    # Get Short Url
    shortUrl =   cache.getShortUrl( url )
    cache.setUrl(url)
    return shortUrl


def getLongUrl(url):
    # Get Short Url

    return url
