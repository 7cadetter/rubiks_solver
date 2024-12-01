from flask import Flask, request, jsonify, render_template
from cube import Cube, Face

app = Flask(__name__)

faces = []

panels = ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']
white_face = Face('white', panels)
faces.append(white_face)

panels = ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']
blue_face = Face('blue', panels)
faces.append(blue_face)

panels = ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange']
orange_face = Face('orange', panels)
faces.append(orange_face)

panels = ['red', 'red','red', 'red', 'red', 'red', 'red', 'red', 'red']
red_face = Face('red', panels)
faces.append(red_face)

panels = ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']
green_face = Face('green', panels)
faces.append(green_face)

panels = ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']
yellow_face = Face('yellow', panels)
faces.append(yellow_face)

cube = Cube(faces)

@app.route('/')
def index():
    # Step 1 - White Cross

    return render_template('index.j2', cube=cube)

@app.route('/turn', methods=['POST'])
def turn():
    direction = request.args.get('direction')

    if direction == 'switch':
        cube.switch()
    else:
        cube.turn(direction)

    new_faces = {
        'top': cube.top.panels,
        'front': cube.front.panels,
        'left': cube.left.panels,
        'right': cube.right.panels,
        'bottom': cube.bottom.panels,
        'back': cube.back.panels
    }
    result = {
        "message": "Cube turned successfully",
        "new_faces": new_faces
    }
    return jsonify(result)

@app.route('/set', methods=['POST'])
def set():
    panel = request.args.get('panel')
    colour = request.args.get('colour')
    panel_num = int(panel[-1])
    cube.front.panels[panel_num] = colour

    result = 'Panel set successfully'

    return jsonify(result)

@app.route('/reset', methods=['POST'])
def reset():
    cube.reset()

    new_faces = {
        'top': cube.top.panels,
        'front': cube.front.panels,
        'left': cube.left.panels,
        'right': cube.right.panels,
        'bottom': cube.bottom.panels,
        'back': cube.back.panels
    }
    result = {
        "message": "Cube turned successfully",
        "new_faces": new_faces
    }
    return jsonify(result)
    

if __name__ == '__main__':
    app.run(debug=True)
