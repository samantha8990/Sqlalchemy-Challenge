#Dependencies
import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#Database Setup
engine = create_engine('sqlite:///hawaii.sqlite')
Base = automap_base()
Base.prepare(engine, reflect=True)
measurement = Base.classes.measurement
station = Base.classes.station

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
    prc=session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').order_by(Measurement.date. desc()).all()
    return jsonify(prc)


@app.route("/api/v1.0/stations")
def stations():
    station_list=session.query(Station.station).all()
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    last_year=session.query(Measurement.station, Measurement.date, Measurement.tobs).\
    filter(Measurement.station=='USC00519281').\
    filter(Measurement.date >= '2016-08-23').\
    order_by(Measurement.date).all()
    return jsonify(tobs)

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>") 
def   
    
# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
