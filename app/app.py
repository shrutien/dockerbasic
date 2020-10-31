from flask import Flask, request, render_template

app = Flask(__name__, template_folder='template')
default_key = 1
cache = {default_key: 'one'}

@app.route('/', methods=['GET', 'POST'])
def mainPage():
	print('request.form-----',request.form)
	key = default_key

	if 'key' in request.form:
		key = request.form.get('key')

	if request.method == 'POST' and request.form['submit'] == 'save':
		cache[key] = request.form['cache_value']

	cache_value = None
	if key in cache:
		cache_value = cache[key]


	return 'Hello Test'

	

if __name__ == '__main__':
    app.run(host='0.0.0.0')
