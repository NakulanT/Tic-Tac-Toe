from flask import Flask, render_template, request
from main import process

processing = process()
app = Flask(__name__)
board = [""] * 9
 
@app.route('/', methods=['GET', 'POST'])
def index():
    restart_clicked = None
    result = None
    play_sound = False
    win_sound = False
    other_sound = False
    restart_sound = False
    global board
    if request.method == 'POST':
        button_clicked = request.form.get('button_clicked')
        restart_clicked = request.form.get('Restart')

        if button_clicked:
            button_clicked = int(button_clicked)
            if board[button_clicked - 1] == "":
                result = processing.pass_input(button_clicked)
                if result:
                    board = result
        elif restart_clicked:
            board = processing.restart()
    
    currentstatus = processing.status()
    if currentstatus == "Ongoing ⚔️":
        play_sound = True
    elif currentstatus == "You Lose 💀":
        win_sound = True
        play_sound = False
    else:
        other_sound = True
        
    if restart_clicked:
        other_sound = False
        play_sound = False
        win_sound = False
        restart_sound = True
            
    return render_template('index.html' , board = board , currentstatus = currentstatus , play_sound = play_sound , other_sound = other_sound , win_sound = win_sound , restart_sound = restart_sound)

if __name__ == '__main__':
    app.run(debug=True)