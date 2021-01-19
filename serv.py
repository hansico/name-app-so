from flask import Flask, request
import json

DB = "./data/names.json"

app = Flask(__name__)

def read_db():
  f = open(DB,'r')
  data = json.loads(f.read())['names']
  f.close()
  return data

def query_from_db(keys=['name','amount'], sort=None, reverse=False):
  data = read_db()
  if sort:
    data.sort(key=lambda x: x[sort], reverse=reverse)
  data = [ [x[k] for k in keys] for x in data ]
  return data

def get_name_count(name):
  data = read_db()
  for entry in data:
    if entry['name'] == name:
      return entry['amount']
  return 0

def count_all_names():
  data = read_db()
  count = 0
  for entry in data:
    count += entry['amount']
  return count

@app.route('/api/names', methods=['GET'])
def names_api():
  # Defaults
  sort, reverse = None, False
  keys = ['name']

  allowed_args = ['sort','reverse','keys']
  allowed_keys = ['amount','name']

  for arg in request.args:
    if arg not in allowed_args:
      return "Unrecognized parameter: "+arg, 200

  if 'keys' in request.args:
    keys = request.args['keys'].split("|")
    for key in keys:
      if key not in allowed_keys:
        return "Unrecognized key: "+request.args[arg], 200

  if 'sort' in request.args:
    if request.args['sort'] not in allowed_keys:
      return "Unrecognized sort: "+request.args[arg], 200
    sort = request.args['sort']
    
    if 'reverse' in request.args:
      if request.args['reverse'] not in ["True","False"] :
        return "Invalid value for reverse: "+request.args['reverse']+". Should be True or False",200
      reverse = request.args['reverse'] == 'True'
    
  data = query_from_db(keys=keys,sort=sort,reverse=reverse)
  data = str(data)

  return data, 200

@app.route('/api/names/count',methods=['GET'])
def count_api():
  if len(request.args) > 1:
    return "Request has too many keywords. Only 'name' is allowed.", 200
  if 'name' not in request.args:
    return "Required keyword missing or invalid: 'name'.", 200

  val = request.args['name']
  if val in ['*','']:
    data = count_all_names()
  else:
    data = get_name_count(val)

  return str(data), 200
  
if __name__ == '__main__':
  app.run()