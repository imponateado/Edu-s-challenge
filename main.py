from flask import Flask, jsonify, request
import requests

def fetchapidata(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados: {e}")
        return None

app = Flask(__name__)

@app.route('/pokemon/get', methods=['GET'])
def get_pokemon():
    entity = request.args.get('name')
    return fetchapidata(f'https://pokeapi.co/api/v2/pokemon/{entity}')

@app.route('/berry/get', methods=['GET'])
def get_berry():
    entity = request.args.get('name')
    return fetchapidata(f'https://pokeapi.co/api/v2/berry/{entity}')

@app.route('/item/get', methods=['GET'])
def get_item():
    entity = request.args.get('name')
    data = fetchapidata(f'https://pokeapi.co/api/v2/item/{entity}')
    filtereddata = {key: data[key] for key in ["category"]}
    return jsonify(filtereddata)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1235)