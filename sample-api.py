from flask import Flask, json, request

api = Flask(__name__)

@api.route('/companies', methods=['GET'])
def get_companies():
  companies = []
  nitems = request.args.get('nitems',type=int)
  print(nitems)

  for x in range(nitems):
    companies.append({"id": x+1, "name": "Company " + str(x+1)})
  
  return json.dumps(companies, indent=4)

if __name__ == '__main__':
    api.run()