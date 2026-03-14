# GIS Python Starter

A lightweight starter repository for **modern GIS development with
Python**.

This project template provides a clean environment for building
geospatial workflows using:

-   Python
-   DuckDB Spatial
-   GeoPandas
-   GDAL
-   SQL-based spatial analysis

It is designed for **local spatial analytics, ETL pipelines, and
automation scripts**.

------------------------------------------------------------------------

## Features

-   Python package structure (`src/` layout)
-   DuckDB + Spatial extension ready
-   GeoPandas / Rasterio / Fiona stack
-   SQL-based spatial queries
-   pytest testing setup
-   Makefile automation
-   VS Code configuration
-   pyenv-compatible environment

------------------------------------------------------------------------

## Requirements

Recommended environment:

-   Python 3.12+
-   pyenv
-   Homebrew
-   GDAL CLI tools

Example setup:

    brew install gdal

------------------------------------------------------------------------

## Project Setup

Clone the repository:

    git clone <repo-url>
    cd <repo-name>

Install the environment:

    make setup

This will:

-   upgrade pip
-   install the package in editable mode
-   install dependencies

------------------------------------------------------------------------

## Run the Starter Script

    make run

Expected output:

    DuckDB Spatial starter check
    POINT (5.1214 52.0907)

------------------------------------------------------------------------

## Run Tests

    make test

------------------------------------------------------------------------

## Code Quality

Format code:

    make format

Lint code:

    make lint

------------------------------------------------------------------------

## Project Structure

    project/
    │
    ├── data/
    │   ├── raw/
    │   ├── processed/
    │   └── output/
    │
    ├── sql/
    │   └── spatial_queries.sql
    │
    ├── src/
    │   └── gis_starter/
    │       ├── db.py
    │       ├── gdal_utils.py
    │       └── main.py
    │
    ├── tests/
    │
    ├── Makefile
    ├── pyproject.toml
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## GIS Stack

This project uses a modern geospatial Python stack:

  Package          Purpose
  ---------------- -------------------------
  GeoPandas        Vector spatial analysis
  Shapely          Geometry operations
  Rasterio         Raster processing
  Fiona            Vector file IO
  PyProj           Coordinate systems
  DuckDB Spatial   Fast spatial SQL

------------------------------------------------------------------------

## Example Workflow

Typical GIS pipeline using this repo:

    Raw GIS files
    ↓
    GDAL conversion / reprojection
    ↓
    DuckDB spatial SQL analysis
    ↓
    Python automation
    ↓
    Export results

------------------------------------------------------------------------

## Creating New Projects

This repository is designed to be used as a **GitHub template**.

Create a new project by clicking:

    Use this template

Then:

    git clone new-project
    cd new-project
    make setup

Start building your spatial analysis pipeline.

------------------------------------------------------------------------

## Development Badges

You can optionally add badges at the top of this README in GitHub:

    ![Python](https://img.shields.io/badge/python-3.12-blue)
    ![Tests](https://img.shields.io/badge/tests-pytest-green)
    ![License](https://img.shields.io/badge/license-MIT-lightgrey)

These give your repo a more professional look.

------------------------------------------------------------------------

## License

MIT
