# Backend Python com Flask
# Instale: pip install flask flask-cors

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__, static_folder='.')
CORS(app)

# Arquivo para armazenar os cadastros (substitua por banco de dados em produção)
DATABASE_FILE = 'subscribers.json'

def load_subscribers():
    """Carrega a lista de inscritos do arquivo JSON"""
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_subscribers(subscribers):
    """Salva a lista de inscritos no arquivo JSON"""
    with open(DATABASE_FILE, 'w', encoding='utf-8') as f:
        json.dump(subscribers, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    """Serve o arquivo HTML principal"""
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    """Serve arquivos estáticos (CSS, JS)"""
    return send_from_directory('.', filename)

@app.route('/api/newsletter', methods=['POST'])
def subscribe():
    """Endpoint para cadastrar novo inscrito na newsletter"""
    try:
        data = request.get_json()
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        
        # Validação
        if not name or not email:
            return jsonify({'error': 'Nome e email são obrigatórios'}), 400
        
        if '@' not in email:
            return jsonify({'error': 'Email inválido'}), 400
        
        # Carregar inscritos existentes
        subscribers = load_subscribers()
        
        # Verificar se email já existe
        if any(sub['email'].lower() == email.lower() for sub in subscribers):
            return jsonify({'error': 'Este email já está cadastrado'}), 409
        
        # Adicionar novo inscrito
        new_subscriber = {
            'name': name,
            'email': email,
            'subscribed_at': datetime.now().isoformat()
        }
        subscribers.append(new_subscriber)
        
        # Salvar
        save_subscribers(subscribers)
        
        print(f"[OK] Novo inscrito: {name} ({email})")
        
        return jsonify({
            'success': True,
            'message': 'Cadastro realizado com sucesso!'
        }), 201
        
    except Exception as e:
        print(f"[ERRO] {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@app.route('/api/subscribers', methods=['GET'])
def list_subscribers():
    """Lista todos os inscritos (para administração)"""
    subscribers = load_subscribers()
    return jsonify({
        'total': len(subscribers),
        'subscribers': subscribers
    })

if __name__ == '__main__':
    print("Servidor rodando em http://localhost:5000")
    print("Arquivos servidos da pasta atual")
    app.run(debug=True, port=5000)
