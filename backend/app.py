from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Une liste en mémoire pour simuler le portfolio
# En pratique, on utiliserait une base de données
portfolio = []

@app.route('/api/coins', methods=['GET'])
def get_coins():
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 50,
            'page': 1,
            'sparkline': False
        }
        response = requests.get(url, params=params)
        
        if response.status_code == 429:
            return jsonify({"error": "Trop de requêtes. Veuillez réessayer plus tard."}), 429
        
        response.raise_for_status()
        coins_data = response.json()
        return jsonify(coins_data)
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête à l'API de CoinGecko: {e}")
        return jsonify({"error": "Impossible de se connecter à l'API de CoinGecko."}), 500

@app.route('/api/coins/<coin_id>/history', methods=['GET'])
def get_coin_history(coin_id):
    try:
        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
        params = {
            'vs_currency': 'usd',
            'days': '7'
        }
        response = requests.get(url, params=params)

        if response.status_code == 429:
            return jsonify({"error": "Trop de requêtes. Veuillez réessayer plus tard."}), 429

        response.raise_for_status()
        history_data = response.json()
        return jsonify(history_data)
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération de l'historique pour {coin_id}: {e}")
        return jsonify({"error": "Impossible de se connecter à l'API de CoinGecko pour l'historique."}), 500

@app.route('/api/portfolio', methods=['GET'])
def get_portfolio():
    return jsonify(portfolio)

@app.route('/api/portfolio', methods=['POST'])
def update_portfolio():
    try:
        data = request.get_json()
        coin_id = data['coin_id']
        if coin_id in portfolio:
            portfolio.remove(coin_id)
        else:
            portfolio.append(coin_id)
        return jsonify({"message": "Portfolio mis à jour", "portfolio": portfolio})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
