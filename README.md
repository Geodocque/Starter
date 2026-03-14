# GIS Starter Repo

A small starter repo for local geospatial development on macOS with:

- Python
- GeoPandas / Shapely / Rasterio
- DuckDB + Spatial extension
- GDAL CLI helpers
- pytest
- VS Code settings

## Project structure

```text
.
├── data/
│   ├── raw/
│   ├── processed/
│   └── output/
├── sql/
│   └── sample_query.sql
├── src/
│   └── gis_starter/
│       ├── __init__.py
│       ├── db.py
│       ├── gdal_utils.py
│       └── main.py
├── tests/
│   └── test_db.py
├── .gitignore
├── .python-version
├── pyproject.toml
├── requirements.txt
└── README.md
```

## 1. Create or activate your environment

If you already use `pyenv` and `pyenv-virtualenv`:

```bash
pyenv activate myproject-env
```

Or create a dedicated env for this repo:

```bash
pyenv virtualenv 3.12.8 gis-starter-env
cd gis_starter_repo
pyenv local gis-starter-env
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 2. Run the sample script

```bash
python -m gis_starter.main
```

This will:

- open a DuckDB connection
- load the `spatial` extension
- create a sample point
- print a tiny result table

## 3. Run tests

```bash
pytest
```

## 4. Optional: install GDAL CLI on macOS

```bash
brew install gdal
```

Then you can use commands like:

```bash
gdalinfo your_raster.tif
ogr2ogr -f GPKG output.gpkg input.shp
```

## 5. Typical workflow

1. Put input data in `data/raw/`
2. Use `gdal_utils.py` helpers or GDAL CLI to normalize/reproject
3. Use `db.py` for DuckDB spatial SQL
4. Write outputs to `data/processed/` or `data/output/`

## 6. Notes

- `data/processed/` and `data/output/` are gitignored.
- `data/raw/` is also gitignored by default because GIS files can be large. Remove that rule if you want to version small sample datasets.
- DuckDB installs the spatial extension on first use if needed.
