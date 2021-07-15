#! /usr/bin/python3
from tkinter import *
from tkinter import ttk as ttk
from PIL import Image, ImageTk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.ticker import MaxNLocator
import threading
import time
import serial
import xlsxwriter



style.use("fivethirtyeight")


#variables
counter = 0
table = {}
xmax = 50
xs = []
ys = []

FILEIMAGE = 'dummy.png'





#ser = serial.Serial(port="/dev/ttyS0", baudrate=115200, bytesize=serial.EIGHTBITS)
#   open serial, set the refresh time to update comm
ser = serial.Serial("/dev/ttyS0", 115200)
txt_name = "SerialTxt.txt"
serial_refresh_time_ms = 500

#buttons_sensors = ['Sensor 1','Sensor 2','Sensor 3','Sensor 4','Sensor 5','Sensor 6']
buttons_sensors = {'Sensor 1' : 0,
                   'Sensor 2' : 1,
                   'Sensor 3' : 2,
                   'Sensor 4' : 3,
                   'Sensor 5' : 4,
                   'Sensor 6' : 5}

class Sensor:
    # create the sensor default object
    def __init__(self):
        self.sensor_descriptor = "CS"
        self.sensorId = 'EXPVAL_0'
        self.ys = []
        self.bg_color = 'gray'
# set the changeble colours thar represents the intensity measured
    def set_color(self):

        if self.ys[-1] < 20000:
            self.bg_color = "red"
        elif 20000 < self.ys[-1] < 25000:
            self.bg_color = "orange"
        elif 25000 < self.ys[-1] < 30000:
            self.bg_color = "yellow"
        elif 30000 < self.ys[-1] < 35000:
            self.bg_color = "green"
        elif 35000 < self.ys[-1] < 40000:
            self.bg_color = "blue"
        elif 40000 < self.ys[-1] < 45000:
            self.bg_color = "indigo"
        else:
            self.bg_color = "violet"
#flags used throughout the program
class Flags:
    def __init__(self):
        self.initial_flag = 1
        self.filled_table = 0
        self.sensor_ativo = Sensor()
        self.sensores = []
        self.first_line = []
        self.buttons = ['raised'] * len(buttons_sensors)
    def set_initial_flag(self):
        self.initial_flag = 1
    def reset_initial_flag(self):
        self.initial_flag = 0
    def set_filled_table(self):
        self.filled_table = 1
    def reset_filled_table(self):
        self.filled_table = 0
    def set_sensor_ativo(self, sensor):
        program_control.sensor_ativo = sensor
    def release_all_buttons(self):
        for bt in range(len(buttons_sensors)):
            self.buttons[bt] = 'raised'
    def button_pressed(self, bt):
        self.release_all_buttons()
        self.buttons[bt] = 'solid'

         
program_control = Flags()


f = Figure(figsize=(9, 7), dpi=70)
a = f.add_subplot(111)

#function resposible for the real-time behavior of graphs
def animate(i):
    global iter
    if i == 0:
        iter = 0
    if program_control.filled_table:
        if id(table[program_control.sensor_ativo.sensorId][iter]) != id(table[program_control.sensor_ativo.sensorId][-1]):
            xs.append(table['TIME'][iter])
            for sensor in program_control.sensores:
                sensor.ys.append(table[sensor.sensorId][iter])
                sensor.set_color()
            iter = iter+1
            # sets a movable window of showing data 
            if iter >= xmax:
                xs.pop(0)
                for sensor in program_control.sensores:
                    sensor.ys.pop(0)
    a.clear()      
    a.plot(xs, program_control.sensor_ativo.ys)
    a.set_xlabel('Seconds')
    #set the yY-values on the graph to show for extense instead of scientific notation as default
    a.get_yaxis().get_major_formatter().set_useOffset(False)
    #set the y-values to be integers, instead of the default
    a.get_yaxis().set_major_locator(MaxNLocator(integer=True))

class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        container = Frame(self)
        container.pack(side="top",fill="both",expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, GraphPage):
            self.frame = F(container, self)
            self.frames[F] = self.frame
            self.frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(GraphPage)
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
    #serial routine is called through the GUI update
    def handle_serial(self,func):
        self.func = func
        self.func()
        self.frame.grid_things()
    def spreadsheet(self,func):
        self.func = func
        self.func()
        self.finish()
    #function need to close serial comm
    def finish(self):
        ser.close()
        self.destroy()
        


class StartPage(Frame):
    def __init__(self, parent,controller):
        Frame.__init__(self, parent)
        self.name = "StartPage"
        label = Label(self, text="Start Page")
        self.button1 = ttk.Button(self, text = 'Page 1', command = lambda: controller.show_frame(PageOne))
        self.button_sensor1 = ttk.Button(self, text='Sensor1', 
                             command=lambda: [controller.show_frame(GraphPage),
                                              program_control.set_sensor_ativo(program_control.sensores[0])])
        self.button_sensor2 = ttk.Button(self, text='Sensor2',
                             command=lambda: [controller.show_frame(GraphPage),
                                              program_control.set_sensor_ativo(program_control.sensores[1])])
        self.button_sensor3 = ttk.Button(self, text='Sensor3',
                             command=lambda: [controller.show_frame(GraphPage),
                                              program_control.set_sensor_ativo(program_control.sensores[2])])

        self.button3 = ttk.Button(self, text='Graph',
                             command=lambda: controller.show_frame(GraphPage))
        self.button_finish = ttk.Button(self, text = "Close", command = controller.finish)
        self.button_spreadsheet = ttk.Button(self, text = "Create Spreadsheet", command=lambda: controller.spreadsheet(createSpreadsheet))
        self.grid_things()

    def grid_things(self):
        self.button_sensor1.grid(column=0, row=1,   pady = 10, sticky = "ew")
        self.button_sensor2.grid(column=1, row=1,  pady = 10, sticky = "ew")
        self.button_sensor3.grid(column=2, row=1,  pady = 10, sticky = "ew")
        self.button_finish.grid(column=1, row=3, sticky='nsew')
        self.button_spreadsheet.grid(column=1, row=4, sticky='nsew')

class GraphPage(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.name = 'GraphPage'
        label = Label(self, text="Graph page")
        self.button1 = ttk.Button(self, text='Return',
                             command=lambda: controller.show_frame(StartPage))
        self.button2 = ttk.Button(self, text='Home',
                             command=lambda: controller.show_frame(StartPage)) 
        self.button_sensor1 = Button(self, text= 'Sensor 1', borderwidth = 4,
                             command=lambda: [controller.show_frame(GraphPage),
                                              program_control.button_pressed(buttons_sensors['Sensor 1']), 
                                              program_control.set_sensor_ativo(program_control.sensores[1])])
        self.button_sensor2 = Button(self, text='Sensor 2', borderwidth = 4,
                             command=lambda: [controller.show_frame(GraphPage),
                                              program_control.button_pressed(buttons_sensors['Sensor 2']), 
                                              program_control.set_sensor_ativo(program_control.sensores[4])])
#         sensor on P1.0 is not conected on the current sensor array
#        self.button_sensor3 = Button(self, text='Sensor3',
#                             command=lambda: [controller.show_frame(GraphPage),
#                                              program_control.set_sensor_ativo(program_control.sensores[2])])
        self.button_sensor3 = Button(self, text='Sensor 3', borderwidth = 4,
                             command=lambda: [controller.show_frame(GraphPage),
                                              program_control.button_pressed(buttons_sensors['Sensor 3']), 
                                              program_control.set_sensor_ativo(program_control.sensores[0])])
        self.button_sensor4 = Button(self, text='Sensor 4', borderwidth = 4,
                             command=lambda: [controller.show_frame(GraphPage),
                                              program_control.button_pressed(buttons_sensors['Sensor 4']), 
                                           program_control.set_sensor_ativo(program_control.sensores[5])])
        self.button_sensor5 = Button(self, text='Sensor 5', borderwidth = 4,
                             command=lambda: [controller.show_frame(GraphPage),
                                              program_control.button_pressed(buttons_sensors['Sensor 5']), 
                                              program_control.set_sensor_ativo(program_control.sensores[3])])
        self.button_sensor6 = Button(self, text='Sensor 6', borderwidth = 4,
                             command=lambda: [controller.show_frame(GraphPage),
                                              program_control.button_pressed(buttons_sensors['Sensor 6']), 
                                              program_control.set_sensor_ativo(program_control.sensores[6])])   
    
        self.button_spreadsheet = ttk.Button(self, text = "Create Spreadsheet", command=lambda: controller.spreadsheet(createSpreadsheet))
        self.button_finish = ttk.Button(self, text = "Close", command = controller.finish)
        self.label_sensor = Label(self, text = program_control.sensor_ativo.sensorId)
        self.render = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/CapSense/legenda_software.png"))
        self.legends = Label(self,image = self.render)
        self.canvas = FigureCanvasTkAgg(f, self)
        #self.canvas.set_xlabel('Seconds')
        self.canvas.draw()
        self.grid_things()
        
    def grid_things(self):

        self.label_sensor = Label(self, text= 'id MCU ' + program_control.sensor_ativo.sensorId)
        if program_control.filled_table:
            self.button_sensor1['bg'] = program_control.sensores[1].bg_color
            self.button_sensor1['relief'] = program_control.buttons[buttons_sensors['Sensor 1']]
            self.button_sensor2['bg'] = program_control.sensores[4].bg_color
            self.button_sensor2['relief'] = program_control.buttons[buttons_sensors['Sensor 2']]
        #         sensor on P1.0 is not conected on the current sensor array            
        #    self.button_sensor3['bg'] = program_control.sensores[2].bg_color
            self.button_sensor3['bg'] = program_control.sensores[0].bg_color
            self.button_sensor3['relief'] = program_control.buttons[buttons_sensors['Sensor 3']]
            self.button_sensor4['bg'] = program_control.sensores[5].bg_color
            self.button_sensor4['relief'] = program_control.buttons[buttons_sensors['Sensor 4']]
            self.button_sensor5['bg'] = program_control.sensores[3].bg_color
            self.button_sensor5['relief'] = program_control.buttons[buttons_sensors['Sensor 5']]
            self.button_sensor6['bg'] = program_control.sensores[6].bg_color
            self.button_sensor6['relief'] = program_control.buttons[buttons_sensors['Sensor 6']]
        self.button_sensor1.grid(column=0, row=1,   pady = 10, sticky = "ew")
        self.button_sensor2.grid(column=1, row=1,  pady = 10, sticky = "ew")
        #         sensor on P1.0 is not conected on the current sensor array
        #self.button_sensor3.grid(column=2, row=1,  pady = 10, sticky = "ew")
        self.button_sensor3.grid(column=2, row=1,   pady = 10, sticky = "ew")
        self.button_sensor4.grid(column=3, row=1,  pady = 10, sticky = "ew")
        self.button_sensor5.grid(column=4, row=1,  pady = 10, sticky = "ew")
        self.button_sensor6.grid(column=5, row=1,  pady = 10, sticky = "ew")
        self.button_finish.grid(column=1, row=3)
        self.button_spreadsheet.grid(column=2, row=3)
        self.label_sensor.grid(row = 5, sticky = "ew")
        self.canvas.get_tk_widget().grid(column=0, columnspan=7, padx=100, pady=10)
        self.legends.grid(column=7, row = 6, padx=10, sticky = "ew")


def receiveDataFromSerial():

    global table
    global initialTime_ms
    if program_control.initial_flag:
        #the first byte stablish the communication with the MCU should be "a" defined on the firmware
        ser.write(b"a")
        program_control.reset_initial_flag()
        initialTime_ms = time.time_ns()//1000000
    else:
        #send a byte to ask for a new line
        ser.write(b"/n")
    timeNow_ms = time.time_ns()//1000000
    time_ms = timeNow_ms - initialTime_ms
    line = ser.readline().decode('ascii')# covert a byte array into a string
    line = line.replace('|', '').split()#convert a string into a list of strings

    if "*SENSOR_DESCRIPTORS" in line:
        line.remove("*SENSOR_DESCRIPTORS")
        create_sensors(line.copy())
    if "*HEADER" in line:
        line.remove("*HEADER")
        program_control.first_line = line.copy()
        #create a dictionary with the index items from the serial
        for dic_item in line:
            table[dic_item] = []
        table['TIME'] = []
    # just fill the table with is a numeric line from the serial
    if (line != []) and (line[0].isdigit()):
        #print(line)
        for index_list, item in enumerate(program_control.first_line):
            table[item].append(int(line[index_list]))
        #appending time in seconds
        table['TIME'].append(round((time_ms/1000),1))
        program_control.set_filled_table()
    app.after(serial_refresh_time_ms,app.handle_serial,receiveDataFromSerial)

#create sensor object
def create_sensors(list_sensors):

    for index_sensor, _sensor in enumerate(list_sensors):
        sensor = Sensor()
        sensor.sensor_descriptor = _sensor
        #EXP VALue is the measure averaged by the MCU hardware function
        sensor.sensorId = "EXPVAL_"+str(index_sensor)
        #sensor.sensorId = "RAW_" + str(index_sensor)
        program_control.sensores.append(sensor)
    if program_control.sensores[0] is not None:
      program_control.set_sensor_ativo(program_control.sensores[0])

#create spreadsheet to store the data      
def createSpreadsheet():
    workbook = xlsxwriter.Workbook('sensors_data.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0
    for keys in table:
        if any(s in keys for s in ('EXP','BASE','TIME')):
            worksheet.write(row,col,keys)
            for values in table[keys]:
                row +=1
                worksheet.write(row, col, values)
            col += 1
            row = 0
    workbook.close()
# GUI routines
app = Application()
app.handle_serial(receiveDataFromSerial)
ani = animation.FuncAnimation(f, animate, interval=10)
app.mainloop()