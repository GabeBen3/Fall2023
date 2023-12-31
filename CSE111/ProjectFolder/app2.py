from flask import Flask, redirect, url_for, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
import json
import sqlite3
from sqlite3 import Error
import glob


#Configure Flask app
app = Flask(__name__)
CORS(app)

#Configure DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite" 

#set db variable as a SQLAlchemy obj tied to flask app "app"
db = SQLAlchemy(app) 

database = r"instance/pokeData.db"

def openConnection(_dbFile):
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    return conn

def closeConnection(_conn, _dbFile):
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)


    # create a database connection


#Default Route "Landing page"
@app.route('/')
def renderIndex():
        #We use the render_template command to render an html page
        return render_template('homePage.html')

@app.route('/viewAllRegions')
def viewAllRegions():
        
        #Perfrom the query based on code from lab 7 
        sql = """SELECT * 
                 FROM region """
        
        #Connect to DB **Necessary before each query 
        conn = openConnection(database)
        cur = conn.cursor()

        #Execute query and save all rows to a variable
        cur.execute(sql)
        _regions = cur.fetchall()

        # print(type(_regions))

        #We can pass the obj lists as arguments to an html page using render_template.
            #We can parse through the list in the html page with Jinja2 
        return render_template('viewAllRegions.html', regions = _regions)

@app.route("/viewIndRegion/<regionName>")
def viewIndRegion(regionName):

    conn = openConnection(database)
    cur = conn.cursor()

    sql = """SELECT * 
                FROM region 
                WHERE r_region_name = ?"""
    
    cur.execute(sql, (regionName, ))
    _regionInfo = cur.fetchall()
    
    trainerQuery = """SELECT t_name 
                        FROM trainers
                        WHERE t_region = ? """
    cur.execute(trainerQuery, (regionName, ))
    _regionTrainers = cur.fetchall()

    print (_regionTrainers)
    
    
    

    return render_template("viewIndRegion.html", regionInfo = _regionInfo, regionTrainers = _regionTrainers)
    
    


@app.route('/viewIndPokemon/<pokemonName>')
def viewIndPokemon(pokemonName):

    #Any query we want to diplay on the page, we fetch it as a list before passing all lists to the html page render

    sql = """SELECT * 
                 FROM pokemon
                  WHERE p_name = ? """
    
    #Second query we will display on viewIndPokemon Page
    evoQuery = """SELECT p2.p_name
                    FROM pokemon p1, pokemon p2 
                        WHERE p1.p_name == ? AND 
                        p1.p_evo_species = p2.p_evo_species
                        ORDER BY p2.p_evolution_stage ASC"""
        
    conn = openConnection(database)
    cur = conn.cursor()

    cur.execute(sql, (pokemonName, ))
    _pokeInfo = cur.fetchall()

    #Need to execute seperate queries separately to obtain different list vars we can pass to the HTML page
    cur.execute(evoQuery, (pokemonName, ))
    _evoGroup = cur.fetchall()
     
     #Pass both vars to html page
    return render_template('viewIndPokemon.html', pokeInfo = _pokeInfo, evoGroup = _evoGroup)

@app.route('/viewAllPokemon')
def viewAllPokemon():

    #Any query we want to diplay on the page, we fetch it as a list before passing all lists to the html page render

    sql = """SELECT * 
                 FROM pokemon"""
    
        
    conn = openConnection(database)
    cur = conn.cursor()

    cur.execute(sql)
    _allPokemon = cur.fetchall()
     
    return render_template('viewAllPokemon.html', allPokemon = _allPokemon)

@app.route('/viewAllTrainers')
def viewAllTrainers():
    sql = """SELECT * 
                 FROM trainers"""
     
    conn = openConnection(database)
    cur = conn.cursor()
    cur.execute(sql)
    _allTrainers = cur.fetchall()
     
    return render_template('viewAllTrainers.html', allTrainers = _allTrainers)

@app.route('/viewIndTrainer/<trainerName>')
def viewIndTrainer(trainerName):
    sql = """ SELECT *
                FROM trainers
                WHERE t_name == ?"""
    
    pokeQuery = """ SELECT DISTINCT t1.tp_pokemon
                    FROM trainer_to_pokemon t1
                    WHERE t1.tp_trainer == ?;"""
     
    conn = openConnection(database)
    cur = conn.cursor()

    cur.execute(sql, (trainerName, ))
    _trainerInfo = cur.fetchall()

    cur.execute(pokeQuery, (trainerName, ))
    _trainerPokemon = cur.fetchall()



    return render_template("viewIndTrainer.html", trainerInfo = _trainerInfo, trainerPokemon = _trainerPokemon)

@app.route('/viewAllAbilities')
def viewAllAbilities():
    sql = """ SELECT * 
                FROM abilities"""
     
    conn = openConnection(database)
    cur = conn.cursor()

    cur.execute(sql)
    _allAbilities = cur.fetchall()
     
    return render_template("viewAllAbilities.html", allAbilities = _allAbilities)

@app.route('/viewIndAbility/<abilityName>')
def viewAllAbility(abilityName):
    sql = """ SELECT * 
                FROM abilities 
                WHERE a_name == ?"""
    
    pokeQuery = """SELECT DISTINCT pa_pokemon
                FROM abilities, pokemon_to_abilities
                WHERE a_name = ? AND 
                        (a_name = pa_ability1 OR 
                            a_name = pa_ability2 OR 
                                a_name = pa_hidden_ability)"""
     
    conn = openConnection(database)
    cur = conn.cursor()

    cur.execute(sql, (abilityName,))
    _allAbilities = cur.fetchall()

    cur.execute(pokeQuery, (abilityName, ))
    _pokemonWithAbility = cur.fetchall()

    print (_pokemonWithAbility)
     
    return render_template("viewIndAbility.html", allAbilities = _allAbilities, pokemonWithAbility = _pokemonWithAbility)

@app.route('/viewEggGroups')
def viewEggGroups():
    sql = """SELECT *
                FROM egg_groups"""

    conn = openConnection(database)
    cur = conn.cursor()

    cur.execute(sql)
    _allEggGroups = cur.fetchall()


    return render_template("viewEggGroups.html", allEggGroups = _allEggGroups) 

@app.route('/viewIndEggGroup/<eggGroup>')
def viewIndEggGroup(eggGroup):
    sql = """SELECT *
                FROM egg_groups
                    WHERE e_egg_group_1 == ? OR 
                            e_egg_group_2 == ? """

    conn = openConnection(database)
    cur = conn.cursor()

    cur.execute(sql, (eggGroup, eggGroup,))
    _pokemonInEggGroup = cur.fetchall()


    return render_template("viewIndEggGroup.html", pokemonInEggGroup = _pokemonInEggGroup, eggGroup = eggGroup) 

@app.route("/test")
def test():
    sql = """SELECT *
                FROM region """

    conn = openConnection(database)
    cur = conn.cursor()

    cur.execute(sql)
    _regionInfo = cur.fetchall()

    return render_template("test.html", regionInfo=json.dumps(_regionInfo))



if __name__ == '__main__':

    app.run()