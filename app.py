from src.flask_setup import app

if __name__ == '__main__':
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=9661)
    app.run(debug=False, host="0.0.0.0", port=9661)