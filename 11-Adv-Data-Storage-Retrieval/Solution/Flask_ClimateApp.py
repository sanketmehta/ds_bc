import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

#################################################
# Application Setup
#################################################

#################################################
# Calculate Start and End date for past 1 year
#################################################

end_dt = datetime.today().strftime('%Y-%m-%d')
start_dt = (datetime.today() - relativedelta(years=1)).strftime('%Y-%m-%d')

#################################################
# Database Setup
#################################################
connection_str = 'sqlite:///hawaii.sqlite'
engine = create_engine(connection_str)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

#Default Route#
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"<pre>Available Routes:</pre>"
        f"<pre>/api/v1.0/precipitation</pre>"
        f"<pre>/api/v1.0/stations</pre>"
        f"<pre>/api/v1.0/tobs</pre>"
        f"<pre>/api/v1.0/start_date            e.g. /api/v1.0/2017-01-01</pre>"
        f"<pre>/api/v1.0/start_date/end_date   e.g. /api/v1.0/2017-01-01/2017-01-15</pre><br/>"
    )

#Route for precipitation data during past year#
@app.route("/api/v1.0/precipitation")
def Precipitation():
    dict_1 = {}
    results = session.query(Measurement.date.label('date'), Measurement.prcp.label('prcp')).filter(Measurement.date.between(start_dt, end_dt))

    for result in results:
        dict_1[result.date.strftime('%Y-%m-%d')] = float(result.prcp)

    return jsonify(dict_1)

#Route for stations list#
@app.route("/api/v1.0/stations")
def Stations():
    stations = []
    results = session.query(Station.name).all()

    for result in results:
        stations.append(result)

    return jsonify(stations)

#Route for temperature observations data#
@app.route("/api/v1.0/tobs")
def TempObservations():
    temObs = []
    results = session.query(Measurement.tobs).all()

    for result in results:
        temObs.append(float(result.tobs))

    return jsonify(temObs)

#Route for temperature observations since a start date#
@app.route("/api/v1.0/<start>")
def TempStats(start):
    dict_2 = {}
    results = session.query(func.max(Measurement.tobs).label('max_temp'), func.min(Measurement.tobs).label('min_temp'), func.avg(Measurement.tobs).label('avg_temp')).filter(Measurement.date >= start).all()

    for result in results:
        dict_2['max_temp'] = float(result.max_temp)
        dict_2['min_temp'] = float(result.min_temp)
        dict_2['avg_temp'] = float(result.avg_temp)

    return jsonify(dict_2)

#Route for temperature observations between a start and end date#
@app.route("/api/v1.0/<start>/<end>")
def TempStats1(start, end):
    dict_3 = {}
    results = session.query(func.max(Measurement.tobs).label('max_temp'), func.min(Measurement.tobs).label('min_temp'), func.avg(Measurement.tobs).label('avg_temp')).filter(Measurement.date.between(start, end)).all()

    for result in results:
        dict_3['max_temp'] = float(result.max_temp)
        dict_3['min_temp'] = float(result.min_temp)
        dict_3['avg_temp'] = float(result.avg_temp)

    return jsonify(dict_3)


if __name__ == '__main__':
    app.run(debug=True)
