from basic import create_app

app=create_app()
app.path('/','NNN')
app.run(5000)
