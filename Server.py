import os
from flask import Flask, request, jsonify, send_from_directory
from config import ADMIN_PASSWORD, PORT, CHANNEL_ID
from bot import upload_to_telegram

app = Flask(__name__, static_folder=".")

# Mock database for hosted files
hosted_files = []

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/admin')
def admin():
    return send_from_directory('.', 'admin.html')

@app.route('/api/upload', methods=['POST'])
def handle_upload():
    if 'file' not in request.files:
        return jsonify({"success": False, "msg": "No file uploaded"}), 400
        
    file = request.files['file']
    filename = file.filename
    
    # Save temporarily
    path = os.path.join("uploads", filename)
    os.makedirs("uploads", exist_ok=True)
    file.save(path)

    # Upload to Telegram
    try:
        file_id, msg_id = upload_to_telegram(path)
        if os.path.exists(path):
            os.remove(path)

        if file_id:
            # Telegram channel link format
            clean_id = str(CHANNEL_ID).replace("-100", "")
            file_link = f"https://t.me/c/{clean_id}/{msg_id}"
            
            file_data = {
                "name": filename,
                "link": file_link,
                "type": "Python" if filename.endswith('.py') else "General"
            }
            hosted_files.append(file_data)
            return jsonify({"success": True, "link": file_data['link']})
    except Exception as e:
        print(f"Error: {e}")
    
    return jsonify({"success": False, "msg": "Upload failed"}), 500

@app.route('/api/admin/files', methods=['POST'])
def get_admin_files():
    data = request.json
    if data.get("password") == ADMIN_PASSWORD:
        return jsonify({"success": True, "files": hosted_files})
    return jsonify({"success": False, "msg": "Wrong Password"}), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
            "type": "Python" if filename.endswith('.py') else "General"
        }
        hosted_files.append(file_data)
        return jsonify({"success": True, "link": file_data['link']})
    
    return jsonify({"success": False}), 500

@app.route('/api/admin/files', methods=['POST'])
def get_admin_files():
    data = request.json
    if data.get("password") == ADMIN_PASSWORD:
        return jsonify({"success": True, "files": hosted_files})
    return jsonify({"success": False, "msg": "Wrong Password"}), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
  
