import flask
import requests

app = flask.Flask(__name__)

@app.route('/')
def index():
    data = {
        'api_key': 'YOUR API KEY',

        # If you want to "bootstrap" the widget with specific parameters for the 
        # user, then you can pass them in here.
        # Optional.
        'destination': {
            'platform': 'github',
            'params': {
                'api_key': 'YOUR_GITHUB_API_KEY'
            }
        }
    }

    # Creates a new migration session
    rc = requests.post(
        'https://widget.hotswap.app/api/sessions',
        json=data
    ).json()

    token = rc['token']

    # Note: You may want to save this session token so that you can 
    #       re-instantiate the widget later when the user returns

    # Pass the session token to the frontend to render the widget
    return flask.render_template('index.html', token=token)

if __name__ == '__main__':
    app.run(debug=True)