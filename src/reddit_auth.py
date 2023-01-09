import praw
import random
import webbrowser
import socket


def receive_connection():
    """
    Wait for and then return a connected socket.
    Opens a TCP connection on port 8080, and waits for a single client.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('localhost', 8080))
    server.listen(1)
    client = server.accept()[0]
    server.close()
    return client


def send_message(client, message):
    """
    Send message to client and close the connection.
    """
    client.send('HTTP/1.1 200 OK\r\n\r\n{}'.format(message).encode('utf-8'))
    client.close()


def reddit_login(client_id, client_secret):  # client_credentials = [client_id,client_secret]
    reddit = praw.Reddit(
        client_id=client_id,  # read the client_id
        client_secret=client_secret,  # read the client_secret
        user_agent='lets download some wallpapers',
        redirect_uri='http://localhost:8080',
    )

    state = str(random.randint(0, 65000))
    scopes = ['identity', 'history']
    url = reddit.auth.url(scopes=scopes, state=state, duration='permanent')
    print('We will now open a window in your browser to complete the login process to reddit.')
    webbrowser.open(url)

    client = receive_connection()
    data = client.recv(1024).decode('utf-8')
    param_tokens = data.split(' ', 2)[1].split('?', 1)[1].split('&')
    params = {key: value for (key, value) in [token.split('=')
                                              for token in param_tokens]}

    if state != params['state']:
        send_message(client, 'State mismatch. Expected: {} Received: {}'
                     .format(state, params['state']))
        return 1
    elif 'error' in params:
        send_message(client, params['error'])
        return 1

    refresh_token = reddit.auth.authorize(params["code"])
    send_message(client, "Feel free to close this window")
    return refresh_token
