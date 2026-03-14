from gis_starter.db import get_connection


def test_spatial_extension_loads() -> None:
    con = get_connection(":memory:")
    result = con.execute("SELECT ST_AsText(ST_Point(1, 2))").fetchone()
    assert result == ("POINT (1 2)",)
    con.close()
