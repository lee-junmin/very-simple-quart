from quart import Quart

app = Quart(__name__)

@app.route('/')
async def hello():
    return 'root'

@app.route('/openai_plugin_legal_info')
async def openai():
    return 'openai_plugin_legal_info'

app.run(debug=True, host="0.0.0.0", port=5002)