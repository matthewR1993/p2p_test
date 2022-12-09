"""added basic tables

Revision ID: ef3f68d8d883
Revises: 
Create Date: 2022-12-09 11:15:21.069809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef3f68d8d883'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('launches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('launch_id', sa.Integer(), nullable=True),
    sa.Column('details', sa.String(), nullable=True),
    sa.Column('is_tentative', sa.Boolean(), nullable=True),
    sa.Column('launch_date_local', sa.DateTime(), nullable=True),
    sa.Column('launch_date_unix', sa.Integer(), nullable=True),
    sa.Column('launch_date_utc', sa.DateTime(), nullable=True),
    sa.Column('launch_success', sa.Boolean(), nullable=True),
    sa.Column('launch_year', sa.Integer(), nullable=True),
    sa.Column('mission_name', sa.String(), nullable=True),
    sa.Column('static_fire_date_unix', sa.Integer(), nullable=True),
    sa.Column('static_fire_date_utc', sa.DateTime(), nullable=True),
    sa.Column('tentative_max_precision', sa.String(), nullable=True),
    sa.Column('upcoming', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('missions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mission_id', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('website', sa.String(), nullable=True),
    sa.Column('wikipedia', sa.String(), nullable=True),
    sa.Column('twitter', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('publications_counter',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('count_launches', sa.Integer(), nullable=True),
    sa.Column('count_missions', sa.Integer(), nullable=True),
    sa.Column('count_rockets', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rockets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rocket_id', sa.String(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('boosters', sa.Integer(), nullable=True),
    sa.Column('company', sa.String(), nullable=True),
    sa.Column('cost_per_launch', sa.Integer(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('first_flight', sa.String(), nullable=True),
    sa.Column('mass_kg', sa.Integer(), nullable=True),
    sa.Column('mass_lb', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('stages', sa.Integer(), nullable=True),
    sa.Column('second_stage_burn_time_sec', sa.Integer(), nullable=True),
    sa.Column('second_stage_engines', sa.Integer(), nullable=True),
    sa.Column('second_stage_fuel_amount_tons', sa.Float(), nullable=True),
    sa.Column('success_rate_pct', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('wikipedia', sa.String(), nullable=True),
    sa.Column('diameter_feet', sa.Float(), nullable=True),
    sa.Column('diameter_meters', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ship_id', sa.String(), nullable=True),
    sa.Column('model', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('abs', sa.Integer(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('attempted_landings', sa.Integer(), nullable=True),
    sa.Column('ship_class', sa.Integer(), nullable=True),
    sa.Column('course_deg', sa.String(), nullable=True),
    sa.Column('home_port', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('imo', sa.Integer(), nullable=True),
    sa.Column('mmsi', sa.Integer(), nullable=True),
    sa.Column('speed_kn', sa.String(), nullable=True),
    sa.Column('position_latitude', sa.String(), nullable=True),
    sa.Column('position_longitude', sa.String(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('weight_kg', sa.Integer(), nullable=True),
    sa.Column('weight_lbs', sa.Integer(), nullable=True),
    sa.Column('year_built', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ships')
    op.drop_table('rockets')
    op.drop_table('publications_counter')
    op.drop_table('missions')
    op.drop_table('launches')
    # ### end Alembic commands ###