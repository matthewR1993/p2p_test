from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Launch(Base):
    __tablename__ = "launches"

    id = Column(Integer, primary_key=True)
    launch_id = Column(Integer)
    details = Column(String)
    is_tentative = Column(Boolean)
    launch_date_local = Column(DateTime)
    launch_date_unix = Column(Integer)
    launch_date_utc = Column(DateTime)
    launch_success = Column(Boolean)
    launch_year = Column(Integer)
    mission_name = Column(String)
    static_fire_date_unix = Column(Integer)
    static_fire_date_utc = Column(DateTime)
    tentative_max_precision = Column(String)
    upcoming = Column(Boolean)


class Rocket(Base):
    __tablename__ = "rockets"

    id = Column(Integer, primary_key=True)
    rocket_id = Column(String)
    active = Column(Boolean)
    boosters= Column(Integer)
    company = Column(String)
    cost_per_launch= Column(Integer)
    country = Column(String)
    description = Column(String)
    first_flight = Column(String)
    mass_kg = Column(Integer)
    mass_lb = Column(Integer)
    name = Column(String)
    stages = Column(Integer)
    second_stage_burn_time_sec = Column(Integer)
    second_stage_engines = Column(Integer)
    second_stage_fuel_amount_tons = Column(Float)
    success_rate_pct = Column(Integer)
    type = Column(String)
    wikipedia = Column(String)
    diameter_feet = Column(Float)
    diameter_meters = Column(Float)


class Ship(Base):
    __tablename__ = "ships"

    id = Column(Integer, primary_key=True)
    ship_id = Column(String)
    model = Column(String)
    name = Column(String)
    type = Column(String)
    status = Column(String)
    abs = Column(Integer)
    active = Column(Boolean)
    attempted_landings = Column(Integer)
    ship_class = Column(Integer)
    course_deg = Column(String)
    home_port = Column(String)
    image = Column(String)
    imo = Column(Integer)
    mmsi = Column(Integer)
    speed_kn = Column(String)
    position_latitude = Column(String)
    position_longitude = Column(String)
    url = Column(String)
    weight_kg = Column(Integer)
    weight_lbs = Column(Integer)
    year_built = Column(Integer)


class Mission(Base):
    __tablename__ = "missions"

    id = Column(Integer, primary_key=True)
    mission_id = Column(String)
    name = Column(String)
    website = Column(String)
    wikipedia = Column(String)
    twitter = Column(String)
    description = Column(String)


class PublicationsCounter(Base):
    __tablename__ = "publications_counter"

    id = Column(Integer, primary_key=True, autoincrement=True)
    count_launches = Column(Integer)
    count_missions = Column(Integer)
    count_rockets = Column(Integer)
