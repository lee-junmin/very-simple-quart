from quart import Quart

app = Quart(__name__)

@app.route('/')
async def hello():
    return 'root'

@app.route('/openai_plugin_legal_info')
async def openai():
    return 'openai_plugin_legal_info'

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
