# Воспроизводимость

## 1. Цель

Этот файл описывает, как воспроизвести основные таблицы и агрегированные результаты МЭПВ-KPI слоя исследования.

## 2. Минимальные требования

- Python 3.10+
- стандартная библиотека Python

Внешние зависимости не требуются.

## 3. Быстрый запуск

Из корня репозитория:

```bash
python scripts/build_tables.py
```

Скрипт читает:

- `data/raw/selection_process.json`
- `data/raw/episodes_analysis.json`

и создаёт/обновляет:

- `data/processed/selection_process.csv`
- `data/processed/episodes_matrix.csv`
- `data/aggregated/mepv_by_conflict.csv`
- `data/aggregated/mepv_by_kpi.csv`
- `data/aggregated/episodes_by_conflict.csv`

## 4. Что воспроизводится

Скрипты воспроизводят только описательную статистику и таблицы распределений. Они не выполняют содержательную интерпретацию эпизодов и не заменяют исследовательскую кодировку.

## 5. Версия данных

Для воспроизведения результатов статьи используется релиз `v1.0.0-submission-package`.
