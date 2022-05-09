from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    path = self.path
    url_components = parse.urlsplit(path)
    query_string_list = parse.parse_qsl(url_components)
    country = countries(query_string_list)

    if "capital" in country:
      url = "https://restcountries.com/v3.1/capital/"
      response = requests.get(url + country["capital"])
      data = response.json()
      capitals = []
      for country_capital in data:
        info = country_capital["capital"][0]
        capitals.append(info)
      message = str(capitals)

    else:
        message = "Give me a valid country please"


    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    self.wfile.write(message.encode())
    return

    