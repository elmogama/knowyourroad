from flask import Flask, render_template, abort, request, Response
import gmaps
import flask
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host = "localhost",
    user = "makeuc",
    password = "makeuc",
    database = "testdb",
    auth_plugin='mysql_native_password',
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE IF NOT EXISTS testdb")

my_cursor.execute('''CREATE TABLE IF NOT EXISTS map (latitude VARCHAR(20),
                                        longitude VARCHAR(20),
                                        category VARCHAR(255),
                                        sev VARCHAR(2),
                                        dummy VARCHAR(255))''')

sqlInsert = "INSERT INTO map (latitude, longitude, category, sev, dummy) VALUES (%s, %s, %s, %s, %s)"

gmaps.configure(api_key='AIzaSyC9bILq0BA8VHrKytVrRUK7Rx8849IgaEQ')

marker_locations = [
    [-32.23333, -64.433327]
]

fig = gmaps.figure()
markers = gmaps.marker_layer(marker_locations)
fig.add_layer(markers)

@app.route('/')
def entry_point():
  if fig:
      return render_template('index.html', fig = fig)
  else:
      abort(404)

@app.route('/map')
def map():
   return render_template('index.html')

@app.route('/get-map', methods=['POST'])
def get_map():
   my_cursor.execute("SELECT * FROM map")
   myresult = my_cursor.fetchall()
   print(myresult)
   map_data = []
   for i in myresult:
       map_data.append(list(i))
   return flask.jsonify({'map':map_data})

   #return flask.jsonify({'map':[ ["name1",40.166672, 44.133331] , ["name2", 33.3, 44.4], ["name3", 35.3, 58.4] ]})

@app.route('/receivedata',methods=['POST'])
def insert_data():
   input_data = request.args.get('loc_data')
   list_data = input_data.split(',')
   recordX = (list_data[0][1:], list_data[1], list_data[2], list_data[3], list_data[4])
   my_cursor.execute(sqlInsert,recordX)
   mydb.commit()
   return Response(status=200)

if __name__ == '__main__':
  app.run()
