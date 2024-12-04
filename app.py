from flask import Flask, request, jsonify, render_template
from cube import Cube, Face

app = Flask(__name__)

faces = []

panels = ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']
bottom_face = Face('white', panels)
faces.append(bottom_face)

panels = ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']
front_face = Face('blue', panels)
faces.append(front_face)

panels = ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange']
left_face = Face('orange', panels)
faces.append(left_face)

panels = ['red', 'red','red', 'red', 'red', 'red', 'red', 'red', 'red']
right_face = Face('red', panels)
faces.append(right_face)

panels = ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']
back_face = Face('green', panels)
faces.append(back_face)

panels = ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']
top_face = Face('yellow', panels)
faces.append(top_face)

cube = Cube(faces)

@app.route('/')
def index():
    cube.reset()
    cube.twist('left')
    cube.twist('face')
    cube.twist('top')
    cube.twist('top')
    cube.twist('bottom')
    cube.twist('right')
    cube.twist('face')
    cube.twist('left')
    cube.twist('bottom')
    cube.twist('right')

    cube.white_cross()

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
