from src.flask_setup import app

if __name__ == '__main__':
    #app.run(debug=False, host="0.0.0.0", port=9661)
    from waitress import serve
    serve(app, host="172.23.0.23", port=9661)

