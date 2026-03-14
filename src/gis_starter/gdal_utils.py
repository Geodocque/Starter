from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


class GDALError(RuntimeError):
    """Raised when a GDAL CLI command fails or GDAL is unavailable."""


def _require_command(command_name: str) -> None:
    if shutil.which(command_name) is None:
        raise GDALError(
            f"'{command_name}' is not available on PATH. Install GDAL CLI first, "
            "for example with: brew install gdal"
        )


def run_command(args: list[str]) -> subprocess.CompletedProcess[str]:
    _require_command(args[0])
    return subprocess.run(args, check=True, text=True, capture_output=True)


def vector_info(input_file: str | Path) -> str:
    """Return ogrinfo output for a vector dataset."""
    result = run_command(["ogrinfo", str(input_file)])
    return result.stdout


def reproject_vector(
    input_file: str | Path,
    output_file: str | Path,
    target_epsg: str,
) -> None:
    """Reproject a vector dataset with ogr2ogr.

    Example target_epsg values: 'EPSG:3857', 'EPSG:4326'.
    """
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    run_command(
        [
            "ogr2ogr",
            "-t_srs",
            target_epsg,
            str(output_path),
            str(input_file),
        ]
    )
