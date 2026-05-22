#!/usr/bin/env python3
"""Build processed CSV tables for the MEPV-KPI research package."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
AGG = ROOT / "data" / "aggregated"

PROCESSED.mkdir(parents=True, exist_ok=True)
AGG.mkdir(parents=True, exist_ok=True)

selection = json.loads((RAW / "selection_process.json").read_text(encoding="utf-8"))
episodes = json.loads((RAW / "episodes_analysis.json").read_text(encoding="utf-8"))

with (PROCESSED / "selection_process.csv").open("w", newline="", encoding="utf-8") as f:
    fieldnames = ["stage", "name", "description", "input_records", "output_records", "excluded", "exclusion_reason", "exclusion_count"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for stage in selection["stages"]:
        for reason, count in stage["exclusion_reasons"].items():
            writer.writerow({
                "stage": stage["stage"],
                "name": stage["name"],
                "description": stage["description"],
                "input_records": stage["input_records"],
                "output_records": stage["output_records"],
                "excluded": stage["excluded"],
                "exclusion_reason": reason,
                "exclusion_count": count,
            })

conflicts = episodes["conflicts"]
with (PROCESSED / "episodes_matrix.csv").open("w", newline="", encoding="utf-8") as f:
    fieldnames = ["episode_type", "kpi", *conflicts, "total"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for episode_type, values in episodes["matrix"].items():
        row = {"episode_type": episode_type, "kpi": values.get("KPI"), "total": values.get("Итого")}
        for conflict in conflicts:
            row[conflict] = values.get(conflict, 0)
        writer.writerow(row)

for filename, source, columns in [
    ("mepv_by_conflict.csv", selection["MEPV_by_conflict"], ["conflict", "mepv_count"]),
    ("mepv_by_kpi.csv", selection["MEPV_by_KPI"], ["kpi", "mepv_count"]),
    ("episodes_by_conflict.csv", selection["episodes_by_conflict"], ["conflict", "episode_count"]),
]:
    with (AGG / filename).open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        for key, value in source.items():
            writer.writerow([key, value])

print("Built MEPV-KPI tables successfully.")
