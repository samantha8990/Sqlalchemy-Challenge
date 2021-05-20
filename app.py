#Dependencies
import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd
import numpy as np

from flask import Flask, jsonify


#Database Setup
engine = create_engine('sqlite:///hawaii.sqlite')
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

session=Session(engine)

#Flask Setup
app = Flask(__name__)

#Flask Routes
@app.route("/")
def home():
    return (
        f"Welcome!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date/end_date<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    results=session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').order_by(Measurement.date. desc()).all()
    prec=list(np.ravel(results))
    return jsonify(prec)


@app.route("/api/v1.0/stations")
def stations():
    results=session.query(Station.station).all()
    stations=list(np.ravel(results))
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    results=session.query(Measurement.station, Measurement.date, Measurement.tobs).\
    filter(Measurement.station=='USC00519281').\
    filter(Measurement.date >= '2016-08-23').\
    order_by(Measurement.date).all()
    tobs=list(np.ravel(results))
    return jsonify(tobs)

@app.route("/api/v1.0/temp/<start>")
def start():
    results=session.query(func.min(Measurement.tobs).\
    func.avg(Measurement.tobs).\
    func.max(Measurement.tobs).\
    filter(Measurement.date >=start). first()
    stats=list(np.ravel(results))
return jsonify(stats)


@app.route("/api/v1.0/temp/<start>/<end>") 
def range():
    results=session.query(func.min(Measurement.tobs).\
    func.avg(Measurement.tobs).\
    func.max(Measurement.tobs).\
    filter(Measurement.date >=start).\
    filter(Measurement.date <= end).first()
    range_stats=list(np.ravel(results))
return jsonify(range_stats)

    
# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
