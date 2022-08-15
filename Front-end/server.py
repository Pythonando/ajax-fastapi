from urllib import response


def app(amb, start_response):
    arq = open("index.html", "rb")
    data = arq.read()
    status = "200 OK"
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)
    return [data]
    