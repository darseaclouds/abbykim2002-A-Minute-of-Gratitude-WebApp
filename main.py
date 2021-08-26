from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)         # everytime make a change in python server, change in web server (take off when running for real)