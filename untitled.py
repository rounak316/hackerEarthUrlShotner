from flask import Flask, jsonify, request, redirect
from Utils import url, cache

app = Flask(__name__)


@app.route('/fetch/short-url/', methods=['POST'])
def fetchShortUrl():
    request_json = request.get_json()
    longUrl = request_json.get('long_url')

    try:
        shortUrl = url.getShortUrl(longUrl)
        if not shortUrl:
            raise Exception()
        else:
            return jsonify({
                "short_url": shortUrl
            })
    except:
        return jsonify({
            "status": "FAILED",
            "status_codes": ["INVALID_URLS"]
        })


# DONE
@app.route('/fetch/long-url/', methods=['POST'])
def fetchLongUrl():
    request_json = request.get_json()
    shortUrl = request_json.get('short_url')
    try:
        longUrl = cache.getLongUrl(shortUrl)
        if not longUrl:
            raise Exception()
        return jsonify({

            "long_url": longUrl.decode("utf-8")
        })

    except:
        return jsonify({
            "status": "FAILED",
            "status_codes": ["INVALID_URLS"]
        })


# DONE


@app.route('/fetch/short-urls/', methods=['POST'])
def fetchShortUrls():
    request_json = request.get_json()
    longUrls = request_json.get('long_urls')
    short_urls = {}
    invalid_urls = []

    for longUrl in longUrls:
        shortUrl = url.getLongUrl(longUrl)
        if shortUrl:
            short_urls[longUrl] = shortUrl
        else:
            invalid_urls.append(longUrl)

    if len(invalid_urls) > 0:

        return jsonify({
            "invalid_urls": invalid_urls,
            "status": "FAILED",
            "status_codes": ["SHORT_URLS_NOT_FOUND"]
        })
    else:
        return jsonify({
            "short_urls": short_urls,
            "invalid_urls": [],
            "status": "OK",
            "status_codes": []
        })



@app.route('/fetch/long-urls/', methods=['POST'])
def fetchLongUrls():
    request_json = request.get_json()
    longUrls = request_json.get('short_urls')
    short_urls = {}
    invalid_urls = []

    for longUrl in longUrls:
        shortUrl = url.getShortUrl(longUrl)
        if shortUrl:
            short_urls[longUrl] = shortUrl
        else:
            invalid_urls.append(longUrl)

    if len(invalid_urls) > 0:

        return jsonify({
            "invalid_urls": invalid_urls,
            "status": "FAILED",
            "status_codes": ["SHORT_URLS_NOT_FOUND"]
        })
    else:
        return jsonify({
            "long_urls": short_urls,
            "invalid_urls": [],
            "status": "OK",
            "status_codes": []
        })
#DONE

@app.route('/fetch/count/', methods=['POST'])
def fetchCount():
    request_json = request.get_json()
    shortUrl = request_json.get('short_url')

    try:
        if not shortUrl:
            raise Exception("Something went wront")

        count = cache.getCount(shortUrl)

        return jsonify({
            "count": count.decode("utf-8"),
            "status": "OK",
            "status_codes": "[]"
        })

    except:
        return jsonify({
            "status": "FAILED",
            "status_codes": "[]"
        })


# DONE


@app.route('/<shorturl>/', methods=['GET'])
def redirectReq(shorturl):
    try:
        longUrl = cache.getLongUrl(shorturl)
        if not longUrl:
            raise Exception()
        return redirect(longUrl)
    except:
        return jsonify({})


# DONE

@app.route('/clean-urls/', methods=['POST'])
def cleanUrl():
    cache.flush()
    return jsonify({})


# DONE

if __name__ == '__main__':
    app.run()
