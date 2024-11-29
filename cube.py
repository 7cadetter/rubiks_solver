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
        print(f"Turning {direction}")

    def twist (self, side, direction='normal'):
        if side == 'face':
            if direction == 'normal':
                self.front.rotate()
                self.shift_lines(self.top.b_line, self.right.l_line, self.bottom.u_line, self.left.r_line)
                self.top.b_line.reverse()
                self.bottom.u_line.reverse()
            elif direction == 'reverse':
                self.front.rotate('anti')
                self.shift_lines(self.top.b_line, self.left.r_line, self.bottom.u_line, self.right.l_line)
                self.right.l_line.reverse()
                self.left.r_line.reverse()
            self.top.panels[5], self.top.panels[6], self.top.panels[7] = self.top.b_line
            self.right.panels[0], self.right.panels[3], self.right.panels[5] = self.right.l_line
            self.bottom.panels[0], self.bottom.panels[1], self.bottom.panels[2] = self.bottom.u_line
            self.left.panels[2], self.left.panels[4], self.left.panels[7] = self.left.r_line
        elif side == 'left':
            if direction == 'normal':
                self.left.rotate()
                self.shift_lines(self.front.l_line, self.bottom.l_line, self.back.r_line, self.top.l_line)
                self.top.l_line.reverse()
            elif direction == 'reverse':
                self.left.rotate('anti')
                self.shift_lines(self.front.l_line, self.top.l_line, self.back.r_line, self.bottom.l_line)
                self.bottom.l_line.reverse()
            self.back.r_line.reverse()
            self.front.panels[0], self.front.panels[3], self.front.panels[5] = self.front.l_line
            self.top.panels[0], self.top.panels[3], self.top.panels[5] = self.top.l_line
            self.back.panels[2], self.back.panels[4], self.back.panels[7] = self.back.r_line
            self.bottom.panels[0], self.bottom.panels[3], self.bottom.panels[5] = self.bottom.l_line
        elif side == 'right':
            if direction == 'normal':
                self.right.rotate()
                self.shift_lines(self.front.r_line, self.top.r_line, self.back.l_line, self.bottom.r_line)
                self.bottom.r_line.reverse()
            elif direction == 'reverse':
                self.right.rotate('anti')
                self.shift_lines(self.front.r_line, self.bottom.r_line, self.back.l_line, self.top.r_line)
                self.top.r_line.reverse()
            self.back.l_line.reverse()
            self.front.panels[2], self.front.panels[4], self.front.panels[7] = self.front.r_line
            self.top.panels[2], self.top.panels[4], self.top.panels[7] = self.top.r_line
            self.back.panels[0], self.back.panels[3], self.back.panels[5] = self.back.l_line
            self.bottom.panels[2], self.bottom.panels[4], self.bottom.panels[7] = self.bottom.r_line
        elif side == 'top':
            if direction == 'normal':
                self.top.rotate()
                self.shift_lines(self.front.u_line, self.left.u_line, self.back.u_line, self.right.u_line)
            elif direction == 'reverse':
                self.top.rotate('anti')
                self.shift_lines(self.front.u_line, self.right.u_line, self.back.u_line, self.left.u_line)
            self.front.panels[0], self.front.panels[1], self.front.panels[2] = self.front.u_line
            self.left.panels[0], self.left.panels[1], self.left.panels[2] = self.left.u_line
            self.back.panels[0], self.back.panels[1], self.back.panels[2] = self.back.u_line
            self.right.panels[0], self.right.panels[1], self.right.panels[2] = self.right.u_line
        elif side == 'bottom':
            if direction == 'normal':
                self.bottom.rotate()
                self.shift_lines(self.front.b_line, self.right.b_line, self.back.b_line, self.left.b_line)
            elif direction == 'reverse':
                self.bottom.rotate('anti')
                self.shift_lines(self.front.b_line, self.left.b_line, self.back.b_line, self.right.b_line)
            self.front.panels[5], self.front.panels[6], self.front.panels[7] = self.front.b_line
            self.left.panels[5], self.left.panels[6], self.left.panels[7] = self.left.b_line
            self.back.panels[5], self.back.panels[6], self.back.panels[7] = self.back.b_line
            self.right.panels[5], self.right.panels[6], self.right.panels[7] = self.right.b_line

    def shift_lines(self, line1, line2, line3, line4):
        temp = line1[:]
        line1[:] = line4
        line4[:] = line3
        line3[:] = line2
        line2[:] = temp

class Face(object):
    def __init__(self, colour, panels):
        self.colour = colour
        self.panels = panels
        self.l_line = [panels[0], panels[3], panels[5]]
        self.r_line = [panels[2], panels[4], panels[7]]
        self.u_line = [panels[0], panels[1], panels[2]]
        self.b_line = [panels[5], panels[6], panels[7]]

        self.neighbours = {
            'top': None,
            'bottom': None,
            'left': None,
            'right': None,
            'opp': None
        }

    def __str__(self):
        return (f'{self.panels[0][:1]}  {self.panels[1][:1]}  {self.panels[2][:1]}\n'
                f'{self.panels[3][:1]}  {self.colour[0][:1]}  {self.panels[4][:1]}\n'
                f'{self.panels[5][:1]}  {self.panels[6][:1]}  {self.panels[7][:1]}\n\n')

    # def set_neighbours(self, top, bottom, left, right, opp):
    #     self.neighbours['top'] = top
    #     self.neighbours['bottom'] = bottom
    #     self.neighbours['left'] = left
    #     self.neighbours['right'] = right
    #     self.neighbours['opp'] = opp

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
            else:
                exit()

            self.panels[i] = panel_copy[group[index]]

    def flip(self):
        self.rotate()
        self.rotate()




colours = ['white', 'blue', 'orange', 'red', 'green', 'yellow']
valid_inputs = ['w', 'b', 'r', 'o', 'g', 'y']
# faces = []

# panels = ['w1', 'w2', 'w3', 'w4', 'w6', 'w7', 'w8', 'w9']
# white_face = Face('white', panels)
# faces.append(white_face)
# panels = ['b1', 'b2', 'b3', 'b4', 'b6', 'b7', 'b8', 'b9']
# blue_face = Face('blue', panels)
# faces.append(blue_face)
# panels = ['o1', 'o2', 'o3', 'o4', 'o6', 'o7', 'o8', 'o9']
# orange_face = Face('orange', panels)
# faces.append(orange_face)
# panels = ['r1', 'r2','r3', 'r4', 'r6', 'r7', 'r8', 'r9']
# red_face = Face('red', panels)
# faces.append(red_face)
# panels = ['g1', 'g2', 'g3', 'g4', 'g6', 'g7', 'g8', 'g9']
# green_face = Face('green', panels)
# faces.append(green_face)
# panels = ['y1', 'y2', 'y3', 'y4', 'y6', 'y7', 'y8', 'y9']
# yellow_face = Face('yellow', panels)
# faces.append(yellow_face)

# cube = Cube(faces)

# white_face.set_neighbours(blue_face, green_face, orange_face, red_face, yellow_face)
# blue_face.set_neighbours(yellow_face, white_face, orange_face, red_face, green_face)
# orange_face.set_neighbours(yellow_face, white_face, green_face, blue_face, red_face)
# red_face.set_neighbours(yellow_face, white_face, blue_face, green_face, orange_face)
# green_face.set_neighbours(yellow_face, white_face, red_face, orange_face, blue_face)
# white_face.set_neighbours(blue_face, green_face, orange_face, red_face, yellow_face)

# print(cube)

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




