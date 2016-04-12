from flask import Flask, render_template, json, request, redirect
app = Flask(__name__)
host="localhost"
port="5000"
address="http://{0}:{1}".format(host,port)

users = {"mohamed":"123456","admin":"qwerty"}
emails = ["mohamed@gmail.com","admin@admin.com"]

def serve_forever():
    app.run(host, port)
	
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError("Not running with Werkzeug server")
    func()

@app.route('/shutdown')
def shutdown():
    shutdown_server()

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignIn')
def showSignIn():
    return render_template('signin.html')

@app.route('/watch')
def watch():
    return render_template('video.html')


@app.route('/showHome')
def showHome():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/userHome')
def userHome():
    return render_template('userHome.html')

@app.route('/logout')
def logout():
    return redirect('/')

@app.route('/error')
def error():
    return redirect('error.html')

@app.route('/validateLogin',methods=['POST','GET'])
def validateLogin():
    if request.method == 'POST':
        InputUsername = request.form['InputUsername']
        inputPassword = request.form['inputPassword']
        database = users.get(InputUsername)
        if inputPassword == database :
           return render_template('userHome.html',home = InputUsername)

        else:
           return render_template('wrong.html', error = "Wrong username or password")

@app.route('/signUp',methods=['POST'])
def signUp():
    if request.method == 'POST':
      inputName = request.form['inputName']
      inputEmail = request.form['inputEmail']
      inputPassword = request.form['inputPassword']
    if inputName and inputEmail and inputPassword:
      if inputEmail not in emails:
        if inputName not in users:							
          emails.append(inputEmail)
          users[inputName] = inputPassword
          return render_template('reg.html',error = 'Your Account has been successfully registered')
        else:
           return render_template('error.html',error = 'user already exists in the current database')
      else:
           return render_template('error.html',error = 'user already exists in the current database')
if __name__ == "__main__":
    serve_forever()
