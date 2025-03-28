from flask import Flask, Response
from Score import ScoreManager
import threading


class ScoreServer:
    def __init__(self):
        self.app = Flask(__name__)

        @self.app.route('/score', methods=['GET'])
        def score_server():
            """The /score endpoint serves the score as an HTML response."""
            try:
                score = int(ScoreManager().read_score().strip())
                if score < 0:
                    raise ValueError(f"ERROR ({score}): Score is negative!")
            except ValueError as e:
                print(e)
                html_response = f"""
                <html>
                   <head>
                      <title>Scores Game</title>
                   </head>
                   <body>
                      <h1><div id="score" style="color:red">{e}</div></h1>
                   </body>
                </html>"""
            else:
                html_response = f"""
                <html>
                   <head>
                      <title>Scores Game</title>
                   </head>
                   <body>
                      <h1>The score is <div id="score">{score}</div></h1>
                   </body>
                </html>"""

            return Response(html_response, mimetype='text/html')

        # Start the Flask server in a new thread
        self.thread = threading.Thread(target=self.run)
        self.thread.start()


    def run(self):
        self.app.run(host="0.0.0.0", port=5000, debug=False)  # host=0.0.0.0 means every one can run it

    def stop(self):
        print("Shutting down the score server...")
        self.thread.join()  # CHECK WHY THE SERVER DOES NOT STOP!!!
        exit(0)


if __name__ == '__main__':
    score_server = ScoreServer()  # Create a ScoreServer instance

    print("Score server is running in the background...")

    # Keep the main program alive
    try:
        while True:
            pass
    except KeyboardInterrupt:
        score_server.stop()