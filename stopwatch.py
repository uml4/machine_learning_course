import simplegui

# Global variables
current_time = 0
is_running = False
successful_stops = 0
total_stops = 0

# Event handler for timer
def tick():
    global current_time
    current_time += 1

# Helper function to format time
def format(t):
    mins = t // 600
    secs = (t // 10) % 60
    tenths = t % 10
    return f"{mins}:{secs // 10}{secs % 10}.{tenths}"

# Draw handler
def draw(canvas):
    formatted_time = format(current_time)
    canvas.draw_text(formatted_time, [50, 110], 36, "White")
    score_text = f"{successful_stops}/{total_stops}"
    canvas.draw_text(score_text, [150, 30], 24, "Green")

# Start button handler
def start():
    global is_running
    timer.start()
    is_running = True

# Stop button handler
def stop():
    global is_running, successful_stops, total_stops
    if is_running:
        total_stops += 1
        if current_time % 10 == 0:
            successful_stops += 1
        is_running = False
    timer.stop()

# Reset button handler
def reset():
    global current_time, is_running, successful_stops, total_stops
    timer.stop()
    current_time = 0
    successful_stops = 0
    total_stops = 0
    is_running = False

# Create frame and timer
frame = simplegui.create_frame("Stopwatch", 300, 200)
timer = simplegui.create_timer(100, tick)

# Add buttons and canvas
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# Start frame
frame.start()
