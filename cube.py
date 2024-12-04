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
            self.turn('forward')
            self.turn('right')
            self.turn('backward')
        elif direction == 'counter':
            self.turn('forward')
            self.turn('left')
            self.turn('backward')

        for face in self.faces:
            face.set_lines()

    def twist (self, side, direction='normal'):
        if side == 'face':
            if direction == 'normal':
                self.front.rotate()
                self.shift_lines(self.top.b_line, self.right.l_line, self.bottom.u_line, self.left.r_line)
                self.top.b_line.reverse()
                self.bottom.u_line.reverse()
            elif direction == 'r':
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
            elif direction == 'r':
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
            elif direction == 'r':
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
            elif direction == 'r':
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
            elif direction == 'r':
                self.bottom.rotate('anti')
                self.shift_lines(self.front.b_line, self.left.b_line, self.back.b_line, self.right.b_line)
            self.front.panels[5], self.front.panels[6], self.front.panels[7] = self.front.b_line
            self.left.panels[5], self.left.panels[6], self.left.panels[7] = self.left.b_line
            self.back.panels[5], self.back.panels[6], self.back.panels[7] = self.back.b_line
            self.right.panels[5], self.right.panels[6], self.right.panels[7] = self.right.b_line
        
        for face in self.faces:
            face.set_lines()

    def shift_lines(self, line1, line2, line3, line4):
        temp = line1[:]
        line1[:] = line4
        line4[:] = line3
        line3[:] = line2
        line2[:] = temp

    def switch(self):
        self.turn('left')
        self.turn('left')

    def reset(self):
        self.bottom.panels = ['white' for _ in self.bottom.panels]
        self.front.panels = ['blue' for _ in self.front.panels]
        self.left.panels = ['orange' for _ in self.left.panels]
        self.right.panels = ['red' for _ in self.right.panels]
        self.top.panels = ['yellow' for _ in self.top.panels]
        self.back.panels = ['green' for _ in self.back.panels]

        for face in self.faces:
            face.set_lines()

    def white_cross(self):
        if self.front.colour == 'white':
            self.turn('backward')
        elif self.bottom.colour == 'white':
            self.turn('counter')
            self.turn('counter')
        elif self.right.colour == 'white':
            self.turn('counter')
        elif self.left.colour == 'white':
            self.turn('clockwise')
        elif self.back.colour == 'white':
            self.turn('forward')

        while self.top.panels[1] != 'white' or self.top.panels[3] != 'white' or self.top.panels[4] != 'white' \
        or self.top.panels[6] != 'white':
            while self.front.panels[1] == 'white' or self.front.panels[3] == 'white' or \
            self.front.panels[4] == 'white' or self.front.panels[6] == 'white' or self.bottom.panels[1] == 'white':
                if self.front.panels[3] == 'white':
                    print('White in panel 6')
                    while self.top.panels[3] == 'white':
                        print('Twisting top r')
                        self.twist('top', 'r')
                    print('Twisting left r')
                    self.twist('left', 'r')
                if self.front.panels[4] == 'white':
                    print('White in panel 4')
                    while self.top.panels[4] == 'white':
                        print('Twisting top r')
                        self.twist('top', 'r')
                    print('Twisting right')
                    self.twist('right')
                if self.front.panels[1] == 'white':
                    print('White in panel 2')
                    while self.top.panels[6] == 'white':
                        print('Twisting top r')
                        self.twist('top', 'r')
                    print('Twisting face')
                    self.twist('face')
                    while self.top.panels[4] == 'white':
                        print('Twisting top r')
                        self.twist('top', 'r')
                    print('Twisting right')
                    self.twist('right')
                if self.front.panels[6] == 'white':
                    print('White in panel 8')
                    while self.top.panels[6] == 'white':
                        print('Twisting top r')
                        self.twist('top', 'r')
                    print('Twisting face r')
                    self.twist('face', 'r')
                    while self.top.panels[4] == 'white':
                        print('Twisting top r')
                        self.twist('top', 'r')
                    print('Twisting right')
                    self.twist('right')
                if self.bottom.panels[1] == 'white':
                    print('White on centre bottom')
                    while self.top.panels[6] == 'white':
                        print('Twisting top r')
                        self.twist('top', 'r')
                    print('Twisting face twice')
                    self.twist('face')
                    self.twist('face')

            print('Turning left\n')
            self.turn('left')

            


class Face(object):
    def __init__(self, colour, panels):
        self.colour = colour
        self.panels = panels
        self.set_lines()

    def __str__(self):
        return (f'{self.panels[0][:1]}  {self.panels[1][:1]}  {self.panels[2][:1]}\n'
                f'{self.panels[3][:1]}  {self.panels[8][:1]}  {self.panels[4][:1]}\n'
                f'{self.panels[5][:1]}  {self.panels[6][:1]}  {self.panels[7][:1]}\n\n')

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

        if direction == 'clock':
            self.u_line, self.r_line, self.b_line, self.l_line = (
                self.l_line, self.u_line, self.r_line, self.b_line
                )
        elif direction == 'anti':
            self.u_line, self.l_line, self.b_line, self.r_line = (
                self.r_line, self.u_line, self.l_line, self.b_line
            )

    def flip(self):
            self.rotate()
            self.rotate()

    def set_lines(self):
        self.l_line = [self.panels[0], self.panels[3], self.panels[5]]
        self.r_line = [self.panels[2], self.panels[4], self.panels[7]]
        self.u_line = [self.panels[0], self.panels[1], self.panels[2]]
        self.b_line = [self.panels[5], self.panels[6], self.panels[7]]

def solve(cube):
    # Step 1 - White Cross
    if cube.top.panels[1] != 'white' or cube.top.panels[3] != 'white' or cube.top.panels[4] != 'white' \
    or cube.top.panels[6] != 'white':
        cube.white_cross()

    # Step 2 - Colour Blocks (URURUFUF)

    # Step 3 - Yellow Cross (FRURUF)

    # Step 4 - Switch Block Tops (RURURUURU)

    # Step 5 - Switch Top Corners (URULURUL)

    # Step 6 - Finish (Down Left Up Right)




