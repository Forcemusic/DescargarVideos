from flask import Flask,render_template,request,jsonify

import descargar_Videos as py

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/api/data', methods = ['POST'])

def received_data():
    link = request.get_json();
    link_url = link['name'];
    py.download_video(link_url);
    return jsonify({'received_data':'Descarga de Video Completa'});

if(__name__=='__main__'):
    app.run(debug=True); 