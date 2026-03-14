from __future__ import annotations

from pathlib import Path

import duckdb


DEFAULT_DB_PATH = Path("data/output/workspace.duckdb")


def get_connection(db_path: str | Path | None = None) -> duckdb.DuckDBPyConnection:
    """Create a DuckDB connection and load the spatial extension.

    The database is stored under data/output by default so the file stays local
    to the project but out of git.
    """
    target = Path(db_path) if db_path else DEFAULT_DB_PATH
    target.parent.mkdir(parents=True, exist_ok=True)

    con = duckdb.connect(str(target))
    con.execute("INSTALL spatial;")
    con.execute("LOAD spatial;")
    return con
