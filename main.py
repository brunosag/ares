from website import create_app

app = create_app()


@app.template_filter("is_integer")
def is_integer(a):
    return a.is_integer()


# When file is ran, run web server
if __name__ == '__main__':
    app.run(debug=True)