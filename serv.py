from flask import Flask
import json

DB = "./data/names.json"

app = Flask(__name__)

def accessDB(DB):
  f = open(DB,'r')
  data = f.read()
  f.close()
  return json.loads(data)

@app.route('/api/names', methods=['GET'])
def names_api():
  data = accessDB(DB)
  return data, 200

if __name__ == '__main__':
  app.run()