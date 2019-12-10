from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    str = "<h1>About me</h1> Hello, my name is Kseniia Klimenko.<br>I'm studying 3rd year Computer Science in TU Dublin.<br>"
	return str
	
@app.route("/contact-me")
def contact():
	return 'Contact me <a href="mailto:d17123220@example.com">by email</a>'
	

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
