from cgi import parse_qs


def wsgi_app(env, start_response):


  status = '200 OK'
  header = [('Content-Type', 'text/plain')]

  body = []
  str = parse_qs(env['QUERY_STRING', keep_blank_values=True])
  for key in str:
    for val in key:
      body.append(key, '=', val)


  start_response(status, header)
  return body