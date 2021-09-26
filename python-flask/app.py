import flask
import requests
from requests.sessions import session

app = flask.Flask(__name__)

@app.route('/')
def index():
    params = {'api_key': '{YOUR API KEY}'}
    data = {
        # This can be any identifier: user ID, email address, username, etc.
        # Required.
        'user_id': '{unique user id}',

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
        params=params,
        data=data
    ).json()

    session_id = rc['session_id']

    # Note: You may want to save this session ID so that you can 
    #       re-instantiate the widget later when the user returns

    # Pass the session_id to the frontend to render the widget
    return flask.render_template('index.html', session_id=session_id)

if __name__ == '__main__':
    app.run(debug=True)