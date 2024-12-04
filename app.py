from flask import Flask, request, jsonify, render_template
from cube import Cube, Face
import random

app = Flask(__name__)

faces = []

panels = ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']
bottom_face = Face(panels)
faces.append(bottom_face)

panels = ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']
front_face = Face(panels)
faces.append(front_face)

panels = ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange']
left_face = Face(panels)
faces.append(left_face)

panels = ['red', 'red','red', 'red', 'red', 'red', 'red', 'red', 'red']
right_face = Face(panels)
faces.append(right_face)

panels = ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']
back_face = Face(panels)
faces.append(back_face)

panels = ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']
top_face = Face(panels)
faces.append(top_face)

cube = Cube(faces)

@app.route('/')
def index():
    cube.reset()
    
    cube.twist('right')
    cube.turn('clockwise')
    cube.twist('top')
    cube.twist('bottom', 'r')
    cube.twist('face')
    cube.turn('forward')
    cube.turn('left')
    cube.twist('right')
    cube.turn('forward')
    cube.twist('top', 'r')
    cube.twist('face', 'r')
    cube.turn('backward')
    cube.turn('counter')
    cube.twist('bottom')



    cube.solve()
    print(cube)

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
