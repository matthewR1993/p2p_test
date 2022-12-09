#!/bin/bash
alembic upgrade head && python3 load_data.py
