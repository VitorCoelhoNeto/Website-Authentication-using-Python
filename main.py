from website import create_app

app = create_app()

if __name__ == '__main__':
    """
    Main function used to run the server.
    """
    app.run(debug = True)