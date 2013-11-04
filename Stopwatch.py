# template for "Stopwatch: The Game"
import simplegui
# define global variables
time = '0:00.0'
t = 0
A = 0
B = 0
C = 0
D = 0
success = 0
num_stop = 0
interval = 100

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global A, B, C, D, time
    A = (t / 600)
    B = (t - A * 600) / 100
    C = (t - A * 600 - B * 100) / 10
    D = t % 10
    time = str(A) + ":" + str(B) + str(C) + "." + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    timer.start()
    
def Stop():
    timer.stop()
    global success, num_stop
    if t != 0:
        num_stop += 1
        if t % 50 == 0:
            success += 1
    
    
def Reset():
    timer.stop()
    global t, time, success, num_stop
    t = 0
    time = "0:00.0"
    success = 0
    num_stop = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t += 1
    format(t)

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(time, (80, 120), 60, 'White')
    canvas.draw_text(str(success) + '/' + str(num_stop), (260, 30), 25, 'Green')
    
# create frame
frame = simplegui.create_frame('Stopwatch', 300, 200)
button1 = frame.add_button('Start', Start, 100)
button2 = frame.add_button('Stop', Stop, 100)
button3 = frame.add_button('Reset', Reset, 100)

# register event handlers
timer = simplegui.create_timer(interval, timer_handler)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()

# Please remember to review the grading rubric
