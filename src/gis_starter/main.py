from __future__ import annotations

from pathlib import Path

from rich.console import Console
from rich.table import Table

from gis_starter.db import get_connection


console = Console()
SQL_DIR = Path("sql")


def run_sample_query() -> list[tuple[str, int]]:
    con = get_connection()
    sql = (SQL_DIR / "sample_query.sql").read_text(encoding="utf-8")
    rows = con.execute(sql).fetchall()
    con.close()
    return rows


def main() -> None:
    rows = run_sample_query()

    table = Table(title="DuckDB Spatial starter check")
    table.add_column("point_wkt")
    table.add_column("sample_value")

    for point_wkt, sample_value in rows:
        table.add_row(point_wkt, str(sample_value))

    console.print(table)
    console.print("\nStarter repo is working.")


if __name__ == "__main__":
    main()
