#https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, jsonify
from werkzeug.exceptions import abort
import json
import sqlite3

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ilionx'



def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_slide(slideNumber):
    # print (slideNumber)
    sql = f"""
            SELECT * 
            FROM slides s, sections ss
            WHERE TRUE
            AND s.sectionId = ss.id
            AND s.include = 1
            AND slideNumber = {slideNumber}
            """
    conn = get_db_connection()
    slide = conn.execute(sql).fetchone()
    conn.close()
    print (slide)
    if slide is None:
        abort(404)
    return slide

def get_slide_blocks(slideNumber):
                                  
    sql = f""" 
            SELECT * 
            FROM   slides s, slide_blocks sb,  sections ss, persona p, block_type bt
            WHERE TRUE
            AND   s.id  = sb.slideId
            AND   ss.id = s.sectionId
            AND   sb.personaId = p.id
            AND   sb.blockTypeId = bt.id
            AND   s.slideNumber = {slideNumber}

                   """

    conn = get_db_connection()
    slide_blocks = conn.execute(sql).fetchall()
    conn.close()
    if slide_blocks is None:
        abort(404)
    return slide_blocks 


def get_slide_sections():
                                  
    sql = f""" 
            SELECT name
            FROM   sections
            WHERE include = 1
            ORDER BY sectionSort 
        """

    conn = get_db_connection()
    slide_sections = conn.execute(sql).fetchall()
    conn.close()
    if slide_sections is None:
        abort(404)
    return slide_sections


def get_personaList():
    sql = f"""
            SELECT  * 
            FROM    persona 
            WHERE   TRUE
            AND     include = 1
            """
    conn = get_db_connection()
    personaList = conn.execute(sql).fetchall()
    conn.close()
    if personaList is None:
        abort(404)
    return personaList


@app.route('/')
def index():
    slide = get_slide(1)
    slide_blocks = get_slide_blocks(1)

    return render_template('slide.html', slide=slide, slide_blocks=slide_blocks)


@app.route('/<int:slideNumber>')
def slide(slideNumber):
    slide = get_slide(slideNumber)
    # x = get_b(slideNumber)
    slide_blocks = get_slide_blocks(slideNumber)

    return render_template('slide.html', slide=slide, slide_blocks=slide_blocks, slide_sections=slide_sections)

@app.route('/assignPersonas', methods=('GET', 'POST'))
def assignPersonas():
    slide = {"id": 1,
    "slideNumber" : 0,
    "created" : '2025-06-01 00:00:00',
    "title" : 'Assign Personas',
    "content" : '',
    "include" : 1,
    "skippable" : 0, 
    "section" : 1
    }
    personaList = get_personaList()
    if request.method == 'POST':

        personaId     = request.form['personaId']
        personaName     = request.form['personaName']
        personaGender = request.form['personaGender']
        
        if not personaId:
            flash('Persona is required!')
        else:
            conn = get_db_connection()
            sql = f"""UPDATE persona set personaGender = '{personaGender}', personaName = '{personaName}' WHERE id = {personaId}"""
            conn.execute(sql)
            conn.commit()
            
            
            writePersonasToJson()
            
            
            conn.close()
            
            return redirect(url_for('assignPersonas'))

    return render_template('assignPersonas.html',
                            slide=slide,
                            selectListPersona=personaList,
                            selectListPersonaGender=[
                                            {'gender': '--Select'}, 
                                            {'gender': 'Man'}, 
                                            {'gender': 'Woman'}, 

                                            ],                            
)


def writePersonasToJson():
    rows = get_personaList()
   
    list = [dict(row) for row in rows]
    print('list:',list)
    with open('static/iframes/process/personas.json', 'w') as f:
        f.write(json.dumps(list))
    return

def get_useCaseList():
    sql = f"""
            SELECT  * 
            FROM    use_case 
            WHERE   TRUE
            ORDER BY created DESC
            """
    conn = get_db_connection()
    useCaseList = conn.execute(sql).fetchall()
    conn.close()
    if useCaseList is None:
        abort(404)
    return useCaseList


@app.route('/createUseCase', methods=('GET', 'POST'))
def createUseCase():
    slide = {"id": 1,
    "slideNumber" : 0,
    "created" : '2025-06-01 00:00:00',
    "title" : 'Create Use Case',
    "content" : '',
    "include" : 1,
    "skippable" : 0, 
    "section" : 1
    }
    useCaseList = get_useCaseList()

    if request.method == 'POST':
        
        personaName         = request.form['personaName']
        gender              = request.form['personaGender']
        useCaseDescription  = request.form['useCaseDescription']
        
        if not useCaseDescription:
            flash('Use Case description is required!')
        elif not personaName:
            flash('Persona Name is required!') 
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO use_case (personaGender, personaName, description) VALUES (?, ?, ?)',
                         ( gender, personaName, useCaseDescription ))
            conn.commit()
            conn.close()
            return redirect(url_for('createUseCase'))

    return render_template('createUseCase.html',
                            slide=slide,
                            useCaseList=useCaseList,
                            selectListPersonaGender=[
                                            {'gender': 'Man'}, 
                                            {'gender': 'Woman'}, 

                                            ],                            
)
    

# Only need to get the slide sections once    
slide_sections=get_slide_sections()    