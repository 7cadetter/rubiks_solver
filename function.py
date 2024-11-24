import copy

class Cube(object):
    def __init__(self, faces):
        self.faces = faces
        self.bottom = faces[0]
        self.front = faces[1]
        self.left = faces[2]
        self.right = faces[3]
        self.back = faces[4]
        self.top = faces[5]

    def __str__(self):
        return (str(self.bottom) + str(self.front) + str(self.left) + str(self.right)
                + str(self.back) + str(self.top))

    def turn(self, direction):
        orient_corn = [0, 2, 7, 5]
        orient_edge = [1, 4, 6, 3]

        left_copy = copy.deepcopy(self.left.panels)
        right_copy = copy.deepcopy(self.right.panels)
        top_copy = copy.deepcopy(self.top.panels)
        bottom_copy = copy.deepcopy(self.bottom.panels)
        front_copy = copy.deepcopy(self.front.panels)
        back_copy = copy.deepcopy(self.back.panels)

        if direction == 'forward':
            self.front, self.top, self.back, self.bottom = (
                self.top, self.back, self.bottom, self.front
            )
            self.top.flip()
            self.back.flip()
            self.left.rotate()
            self.right.rotate('anti')
        elif direction == 'backward':
            self.front, self.top, self.back, self.bottom = (
                self.bottom, self.front, self.top, self.back
            )
            self.back.flip()
            self.bottom.flip()
            self.right.rotate()
            self.left.rotate('anti')
        elif direction == 'left':
            self.front, self.left, self.back, self.right = (
                self.right, self.front, self.left, self.back
            )
            self.top.rotate()
            self.bottom.rotate('anti')
        elif direction == 'right':
            self.front, self.left, self.back, self.right = (
                self.left, self.back, self.right, self.front
            )
            self.bottom.rotate()
            self.top.rotate('anti')
        elif direction == 'clockwise':
            self.top, self.right, self.bottom, self.left = (
                self.left, self.top, self.right, self.bottom
            )
            self.top.rotate()
            self.bottom.rotate()
            self.left.rotate()
            self.right.rotate()
            self.front.rotate()
            self.back.rotate('anti')
        elif direction == 'counter':
            self.top, self.right, self.bottom, self.left = (
                self.right, self.bottom, self.left, self.top
            )
            self.top.rotate('anti')
            self.bottom.rotate('anti')
            self.left.rotate('anti')
            self.right.rotate('anti')
            self.back.rotate()
            self.front.rotate('anti')

    def twist (self, side, direction='normal'):
        if direction == 'normal':
            if side == 'face':
                self.front.rotate()
                temp = self.top.panels[5], self.top.panels[6], self.top.panels[7]
                self.top.panels[5], self.top.panels[6], self.top.panels[7] = (
                    self.left.panels[7], self.left.panels[4], self.left.panels[2])
                self.left.panels[7], self.left.panels[4], self.left.panels[2] = (
                    self.bottom.panels[2], self.bottom.panels[1], self.bottom.panels[0]
                )
                self.bottom.panels[2], self.bottom.panels[1], self.bottom.panels[0] = (
                    self.right.panels[0], self.right.panels[3], self.right.panels[5]
                )
                self.right.panels[0], self.right.panels[3], self.right.panels[5] = temp


        # elif direction == 'reverse':





class Face(object):
    def __init__(self, colour, panels):
        self.colour = colour
        self.panels = panels

        self.neighbours = {
            'top': None,
            'bottom': None,
            'left': None,
            'right': None,
            'opp': None
        }

    def __str__(self):
        return (f'{self.panels[0]}  {self.panels[1]}  {self.panels[2]}\n'
                f'{self.panels[3]}  {self.colour[0]}  {self.panels[4]}\n'
                f'{self.panels[5]}  {self.panels[6]}  {self.panels[7]}\n\n')

    def set_neighbours(self, top, bottom, left, right, opp):
        self.neighbours['top'] = top
        self.neighbours['bottom'] = bottom
        self.neighbours['left'] = left
        self.neighbours['right'] = right
        self.neighbours['opp'] = opp

    def rotate(self, direction='clock'):
        orient_corn = [0, 2, 7, 5]
        orient_edge = [1, 4, 6, 3]

        panel_copy = copy.deepcopy(self.panels)

        for i in range(0, 8):
            is_corner = i in orient_corn
            group = orient_corn if is_corner else orient_edge
            group_index = group.index(i)

            if direction == 'clock':
                index = (group_index - 1) % 4
            elif direction == 'anti':
                index = (group_index + 1) % 4

            print(f'{panel_copy[group[index]]} into panel {i}, replaces {self.panels[i]}')
            self.panels[i] = panel_copy[group[index]]
        print('\n')

    def flip(self):
        self.rotate('clockwise')
        self.rotate('clockwise')


colours = ['white', 'blue', 'orange', 'red', 'green', 'yellow']
valid_inputs = ['w', 'b', 'r', 'o', 'g', 'y']
faces = []

panels = ['w1', 'w2', 'w3', 'w4', 'w6', 'w7', 'w8', 'w9']
white_face = Face('white', panels)
faces.append(white_face)
panels = ['b1', 'b2', 'b3', 'b4', 'b6', 'b7', 'b8', 'b9']
blue_face = Face('blue', panels)
faces.append(blue_face)
panels = ['o1', 'o2', 'o3', 'o4', 'o6', 'o7', 'o8', 'o9']
orange_face = Face('orange', panels)
faces.append(orange_face)
panels = ['r1', 'r2','r3', 'r4', 'r6', 'r7', 'r8', 'r9']
red_face = Face('red', panels)
faces.append(red_face)
panels = ['g1', 'g2', 'g3', 'g4', 'g6', 'g7', 'g8', 'g9']
green_face = Face('green', panels)
faces.append(green_face)
panels = ['y1', 'y2', 'y3', 'y4', 'y6', 'y7', 'y8', 'y9']
yellow_face = Face('yellow', panels)
faces.append(yellow_face)

cube = Cube(faces)

white_face.set_neighbours(blue_face, green_face, orange_face, red_face, yellow_face)
blue_face.set_neighbours(yellow_face, white_face, orange_face, red_face, green_face)
orange_face.set_neighbours(yellow_face, white_face, green_face, blue_face, red_face)
red_face.set_neighbours(yellow_face, white_face, blue_face, green_face, orange_face)
green_face.set_neighbours(yellow_face, white_face, red_face, orange_face, blue_face)
white_face.set_neighbours(blue_face, green_face, orange_face, red_face, yellow_face)

cube.twist('face')
print(cube)



# Step 1 - White Cross
# while faces[0].tm != 'w' and faces[0].ml != 'w' and faces[0].mr != 'r' and faces[0].bm != 'r':


    # for colour in colours:
    #     print(f'Pattern on {colour} face? Enter first letter of colour (white = w, etc.')
    #     tl = input('Top left: ')
    #     while tl not in valid_inputs:
    #         tl = input('Invalid input. Top left: ')
    #     tm = input('Top middle: ')
    #     while tm not in valid_inputs:
    #         tm = input('Invalid input. Top middle: ')
    #     tr = input('Top right: ')
    #     while tr not in valid_inputs:
    #         tr = input('Invalid input. Top right: ')
    #     ml = input('Middle left: ')
    #     while ml not in valid_inputs:
    #         ml = input('Invalid input. Middle left: ')
    #     mr = input('Middle right: ')
    #     while mr not in valid_inputs:
    #         mr = input('Invalid input. Middle right: ')
    #     bl = input('Bottom left: ')
    #     while bl not in valid_inputs:
    #         bl = input('Invalid input. Bottom left: ')
    #     bm = input('Bottom middle: ')
    #     while bm not in valid_inputs:
    #         bm = input('Invalid input. Bottom middle: ')
    #     br = input('Bottom right: ')
    #     while br not in valid_inputs:
    #         br = input('Invalid input. Bottom right: ')
    #     print('\n\n')
    #     face = Face(colour, tl, tm, tr, ml, mr, bl, bm, br)
    #     faces.append(face)




