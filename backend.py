from flask import Flask, jsonify
import psutil
import os

app = Flask(__name__)

@app.route('/healthz', methods=['GET'])
def healthz():
    cpu_usage = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')

    response = {
        'cpu_usage': cpu_usage,
        'memory': {
            'total': memory_info.total,
            'used': memory_info.used,
            'free': memory_info.free,
            'percent': memory_info.percent
        },
        'disk_space': {
            'total': disk_info.total,
            'used': disk_info.used,
            'free': disk_info.free,
            'percent': disk_info.percent
        }
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')