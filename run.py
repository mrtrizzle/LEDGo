from flask import jsonify, render_template, request, Flask
from Matrix import Matrix

app = Flask(__name__)
#app.config.from_object(__name__)
#app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

# CONFIG
MAT_SIZE = 8


@app.route('/', defaults={'site': 'draw'})
@app.route('/<any(animations, draw, gradient, text):site>')
def index(site):
    return render_template('{0}.html'.format(site), site=site)


@app.route('/setPixel', methods=['POST'])
def setPixel():
	x = request.form.get('x', 0, type=int)
	y = request.form.get('y', 0, type=int)
	color = request.form.get('color', 'rgb(0,0,0)', type=str)
	
	print("Setting Pixel[{}, {}] to {}".format(x,y,color))
	mat.convertJSPixel(x,y,color)

	return jsonify(message="Set Pixel[{}, {}] to {}".format(x,y,color))

@app.route('/clearMatrix')
def clearMatrix():
	mat.clearMatrix()
	return jsonify(message="Matrix cleared.")

@app.route('/fillWithColor', methods=['POST'])
def fillWithColor():
	print("Filling with color")
	color = request.form.get('color', 'rgb(0,0,0)', type=str)
	mat.fillWithColor(color)
	return jsonify(message="Matrix filled with "+color+".")

if __name__=='__main__':
	mat = Matrix(MAT_SIZE,MAT_SIZE)
	print("created matrix")

	app.run('0.0.0.0', debug=True)