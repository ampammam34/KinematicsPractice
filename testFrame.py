#!/usr/bin/env python
# -*- coding: cp932 -*-

import Tkinter as tk


my_tuple1 = (("8:left arm up       ",-14,130,0),#L1
                    ("9:left arm open    ",0,56,40),#L2
                    ("10:left upper arm   ",0,90,45),#L3
                    ("11:left elbow       ",0,112,0),#L4
                    ("12:left forearm     ",-90,90,0),#L5
                    ("13:left hand length ",-40,28,-6),#L6
                    ("14:left hand side   ",-15,25,5))#L7
my_tuple2 = (("15:right arm up     ",-14,130,130),#R1
                    ("16:right arm open   ",0,56,50),#R2
                    ("17:right upper arm  ",0,90,0),#R3
                    ("18:right elbow      ",0,112,0),#R4
                    ("19:right forearm    ",-90,90,-90),#R5
                    ("13:right hand length ",-40,28,-6),#R6
                    ("14:right hand side   ",-15,25,5))#R7


class TestFrame(tk.Frame):

        def __init__(self,root,number,label,min_,max_,init_):
                tk.Frame.__init__(self,root)
                self.root = root
                                
                row = 0
                column = 0
                self.label = tk.Label(self,text=label)
                self.label.grid(row=row, column=column)
                
                row = 0
                column = 1
                self.slider = tk.Scale(self,orient='h',from_ = min_, to = max_)
                self.slider.set(init_)
                self.slider.grid(row=row, column=column)

                
                row = 0
                column = 2
                self.strvar = tk.StringVar()
                self.strvar.set("0")
                self.entry =tk.Entry(self,textvariable=self.strvar)
                self.entry.grid(row=row,column=column)
                #
                #self.button = tk.Button(root, text = 'Gripper ON', bg = '#250')
                #self.button.grid(column=5,row=13)

        def setvalue(self, value):
                #value = self.slider.get()
                self.strvar.set(value)
                
                #self.strvar.set()
                
        def getvalue(self):
                return self.slider.get()

class ArmLeftFrame(tk.Frame):
        def __init__(self,root, tuple):
                tk.Frame.__init__(self,root)
                self.root = root
                row = 0
                column = 0
                for elem in my_tuple1:
                        title = elem[0]
                        value1 = elem[1]
                        value2 = elem[2]
                        value3 = elem[3]
                        tf = TestFrame(self,0,elem[0],elem[1],elem[2],elem[3])
                                #selfじゃなくてrootにしたら窓全体に追加されるということになる               
                        tf.grid(row=row,column=column)
                        row = row + 1

class ArmRightFrame(tk.Frame):
        def __init__(self,root, tuple):
                tk.Frame.__init__(self,root)
                self.root = root
                row = 0
                column = 0
                for elem in my_tuple2:
                        title = elem[0]
                        value1 = elem[1]
                        value2 = elem[2]
                        value3 = elem[3]
                        tf = TestFrame(self,0,elem[0],elem[1],elem[2],elem[3])
                                #selfじゃなくてrootにしたら窓全体に追加されるということになる               
                        tf.grid(row=row,column=column)
                        row = row + 1

class Coordinate(tk.Frame):
        def __init__(self, root):
                self.entry =tk.Entry(self,textvariable=0)
           


if __name__ == '__main__':
        root = tk.Tk()
        frames1 = []
        frames2 = []
        c0 = tk.Canvas(root, width = 150, height = 30)
        c0.create_text(75, 15, text = '--------LEFT--------', font = ('FixedSys', 14))
        c0.pack()
        armleftFrame1 = ArmLeftFrame(root, my_tuple1)       
        armleftFrame1.pack()
        c0 = tk.Canvas(root, width = 150, height = 30)
        c0.create_text(75, 15, text = '--------RIGHT--------', font = ('FixedSys', 14))
        c0.pack()
        armrightFrame1 = ArmRightFrame(root, my_tuple2)       
        armrightFrame1.pack()
        #coordinate = Coordinate(root)
        #coordinate.pack()



                
        #return root, frames

        root.mainloop()

