def wsgi_app(env, start_response):


  status = '200 OK'
  header = [('Content-Type', 'text/plain')]

  body = []
  for arg in env['QUERY_STRING'].split('&'):
    body += arg + "\n"


  start_response(status, header)
  return body