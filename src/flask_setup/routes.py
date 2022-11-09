from src.api.utils import DatabaseHandler
from src.api.request_handler import RequestHandler
from src.flask_setup import app
from flask import request

@app.route("/hitec/app/crawl", methods=['POST'])
def run_crawler():
    if request.method == "POST":
        request_content = request.get_json(force=True)
        app.logger.info(str(request_content))
        
        database_client = DatabaseHandler()
        
        try:
            client = RequestHandler(request_content, database_client, app.logger)
            client.run()
        except KeyError as error:
            app.logger.error(str(error))
            return 'Error'
        
    else:
        app.logger.error('Error: Only Post method implemented')
        
    return 'OK'