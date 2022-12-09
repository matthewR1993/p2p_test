import requests
from flatten_json import flatten
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import numpy as np

from data_models import Ship, Rocket, Mission, Launch


url = 'https://api.spacex.land/graphql/'


query_launches = """
query Launches {
  launches {
    details
    id
    is_tentative
    launch_date_local
    launch_date_unix
    launch_date_utc
    launch_success
    launch_year
    mission_name
    static_fire_date_unix
    static_fire_date_utc
    tentative_max_precision
    upcoming
  }
}
"""

query_rockets = """
query Rockets {
  rockets {
    active
    boosters
    company
    cost_per_launch
    country
    description
    first_flight
    id
    mass {
      kg
      lb
    }
    name
    stages
    second_stage {
      burn_time_sec
      engines
      fuel_amount_tons
    }
    success_rate_pct
    type
    wikipedia
    diameter {
      feet
      meters
    }
  }
}
"""

query_missions = """
query Missions {
  missions {
    name
    website
    wikipedia
    twitter
    id
    description
  }
}"""

query_ships = """
query Ships {
  ships {
    model
    name
    type
    status
    abs
    active
    attempted_landings
    class
    course_deg
    home_port
    id
    image
    imo
    mmsi
    speed_kn
    position {
      latitude
      longitude
    }
    url
    weight_kg
    weight_lbs
    year_built
  }
}"""

counter_query = """
INSERT INTO publications_counter SELECT 0 as id, (
        SELECT COUNT(*)
        FROM   launches
        ) AS count_launches,
        (
        SELECT COUNT(*)
        FROM   missions
        ) AS count_missions,
        (
        SELECT COUNT(*)
        FROM   rockets
        ) AS count_rockets
"""


def load_from_api(query, entity_name):
    request = requests.post(url, json={'query': query, 'variables': {'limit': 1000}})
    res = request.json()
    return [flatten(x) for x in res['data'][entity_name]]


def populate_tables():
    res_rockets = load_from_api(query_rockets, 'rockets')
    res_missions = load_from_api(query_missions, 'missions')
    res_ships = load_from_api(query_ships, 'ships')
    res_launches = load_from_api(query_launches, 'launches')

    # cleaning
    df_rockets = pd.DataFrame(res_rockets)
    df_rockets = df_rockets.rename(columns={"id": "rocket_id"})
    df_rockets = df_rockets.replace(np.nan, None)
    df_rockets = df_rockets.fillna(np.nan).replace([np.nan], [None])

    df_missions = pd.DataFrame(res_missions)
    df_missions = df_missions.rename(columns={"id": "missions_id"})
    df_missions = df_missions.replace(np.nan, None)
    df_missions = df_missions.fillna(np.nan).replace([np.nan], [None])

    df_ships = pd.DataFrame(res_ships)
    df_ships = df_ships.rename(columns={"id": "ship_id", "class": "ship_class"})
    df_ships = df_ships.astype({'abs': 'Int64', 'attempted_landings': 'Int64',
                                'ship_class': 'Int64', 'imo': 'Int64', 'mmsi': 'Int64'})
    df_ships = df_ships.replace(np.nan, None)
    df_ships = df_ships.fillna(np.nan).replace([np.nan], [None])

    df_launches = pd.DataFrame(res_launches)
    df_launches['id'] = df_launches['id'].astype('Int64')
    df_launches = df_launches.rename(columns={"id": "launch_id"})
    df_launches['launch_year'] = df_launches['launch_year'].astype('Int64')
    df_launches['launch_date_local'] = pd.to_datetime(df_launches['launch_date_local'], utc=True)
    df_launches['launch_date_utc'] = pd.to_datetime(df_launches['launch_date_utc'], utc=True)
    df_launches['static_fire_date_utc'] = pd.to_datetime(df_launches['static_fire_date_utc'], utc=True)
    df_launches = df_launches.replace(np.nan, None)
    df_launches = df_launches.fillna(np.nan).replace([np.nan], [None])

    # engine = create_engine("sqlite:///sqlite.db")
    engine = create_engine("postgresql+psycopg2://postgres:postgres@postgres:5432/postgres")

    with Session(engine) as session:
        session.execute("""
        truncate table publications_counter;
        truncate table launches;
        truncate table missions;
        truncate table rockets;
        truncate table ships;
        """)
        session.commit()

    for table, model in [(df_ships, Ship), (df_rockets, Rocket),
                         (df_missions, Mission), (df_launches, Launch)]:
        with Session(engine) as session:
            session.bulk_insert_mappings(model, table.to_dict(orient="records"))
            session.commit()

    with Session(engine) as session:
        session.execute(counter_query)
        session.commit()

    print('ETL completed')


if __name__ == '__main__':
    populate_tables()

