# Python 2 to 3 compatibility
from __future__ import print_function

from flask import Flask, render_template, request, jsonify, json, flash
from flask_mail import Mail, Message
from forms import ContactForm

# Add path to current directory
import os
cd = os.getcwd()

import sys
sys.path.append(cd)

# Sudoku imports
from python.sudoku import get_boxes
from python.sudoku import solve_values
from python.sudoku import eliminate_one
import time


app = Flask(__name__)
app.secret_key = 'weidmanssecret'

# add mail server config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'seth@sethweidman.com'
app.config['MAIL_PASSWORD'] = '**PASSWORD**'

mail = Mail(app)

@app.route('/contact', methods=('GET', 'POST'))
def contact():
    # form = ContactForm(data=request.form)
    # dir()
    form = ContactForm(obj=dict(request.form));
    # form.populate_obj(request.form)

    if request.method == 'POST':
        if form.validate() == False:

            return render_template('form.html', form=form)
        else:
            msg = Message("Message from your visitor " + form.name.data,
                          sender=form.email.data,
                          recipients=['seth@sethweidman.com'])
            msg.body = """
            From: %s <%s>,
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return "Successfully sent message!"
    elif request.method == 'GET':
        return render_template('form.html', form=form)

###
# Sudoku stuff #
###

ROWS = 'ABCDEFGHI'
COLS = '123456789'
boxes = get_boxes(ROWS, COLS)

def try_read_int(cell, default_value='123456789'):
    '''
    This function is applied to every cell, from A1 through I9.
    It takes in a cell and tries to return a string representing the value of
    that cell. Otherwise I return a default value.
    '''
    acceptable_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    try:
        value = int(request.form[cell])
        return str(value)
    except:
        return default_value


@app.route('/sudoku/', methods=['GET', 'POST'])
def hello_world():
    '''Sets up the Sudoku with an easy-to-solve puzzle.
    Uses Javascript to render it.'''
    easy_dict = {"A1": 7, "A5": 9,
                 "B2": 6, "B3": 8, "B8": 3, "B9": 1,
                 "C1": 5, "C3": 1, "C4": 3, "C7": 4, "C8": 2, "C9": 7,
                 "D1": 8, "D2": 1, "D5": 5,
                 "E3": 7, "E4": 9, "E5": 1, "E6": 6, "E7": 8,
                 "F5": 7, "F8": 1, "F9": 3,
                 "G1": 4, "G2": 3, "G3": 5, "G6": 7, "G7": 1, "G9": 2,
                 "H1": 9, "H2": 7, "H7": 6, "H8": 4,
                 "I5": 2, "I9": 5}
    return render_template('index.html', input_sudoku=easy_dict)


@app.route('/sudoku/sudoku_action/', methods=['GET', 'POST'])
def sudoku_action():
    '''
    This function:
    -Loops through the boxes and uses "try_read_int" to fill them with values.
    -If we have requested to "solve the whole puzzle", then solve the whole puzzle.
    -Otherwise, simply return the template with the same values.
    '''
    cell_data = {}
    for box in boxes:
        cell_data[box] = ''
        cell_data[box] = try_read_int(box)
    if request.form['type'] == 'solve_all':
        final_values = solve_values(cell_data)
        return render_template("solved_sudoku.html", sudoku=final_values)
    else:
        return render_template('sudoku_action.html', input_sudoku=cell_data)


@app.route('/sudoku/eliminate_one/', methods=['GET', 'POST'])
def update_one():
    '''
    Update just one value in the cell.
    '''
    cell_data = {}
    for box in boxes:
        cell_data[box] = ''
        cell_data[box] = try_read_int(box)
    new_values, message, peer = eliminate_one(cell_data)
    time.sleep(3)
    return jsonify(values=new_values, message=message, peer=peer)


if __name__ == '__main__':
    app.run()
