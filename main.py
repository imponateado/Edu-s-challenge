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

BASE_URL = 'https://pokeapi.co/api/v2/'

@app.route('/pokemon/get', methods=['GET'])
def get_pokemon():
    try:
        name = request.args.get('name')
        if not name:
            return jsonify({ 'erro': 'O parâmetro nam é obrigatório'}), 400
        
        url = f"{BASE_URL}pokemon/{name}"
        data = fetchapidata(url)

        if data is None:
            return jsonify({ 'erro': 'Falha em buscar pokemon'}), 500
        
        filtereddata = {
            key: data.get(key)
            for key in ["height", "weight"]
        }

        return jsonify(filtereddata)
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/berry/get', methods=['GET'])
def get_berry():
    try:
        name = request.args.get('name')
        if not name:
            return jsonify({'erro': 'O parâmetro name não é obrigatório'}), 400
        
        url = f"{BASE_URL}berry/{name}"
        data = fetchapidata(url)
        
        if data is None:
            return jsonify({'erro': 'Erro ao buscar os dados'}), 500
        
        filtereddata = {
            key: data.get(key)
            for key in ["growth_time", "max_harvest", "size", "smoothness", "soil_dryness"]
        }
        return jsonify(filtereddata)
    
    except Exception as e:
        return jsonify({ 'erro': str(e)}), 500

@app.route('/item/get', methods=['GET'])
def get_item():
    try:
        name = request.args.get('name')
        if not name:
            return jsonify({'erro': 'O parâmetro name é obrigatório'})
        
        url = f"{BASE_URL}item/{name}"
        data = fetchapidata(url)

        if data is None:
            return jsonify({'erro': 'Algo deu errado, não foi possível buscar os dados'})
        
        filtereddata = {
            key: data.get(key)
            for key in ["category"]
        }
        return jsonify(filtereddata)
    except Exception as e:
        return jsonify({'erro': str(e)}),500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1235)