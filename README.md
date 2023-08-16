# dagster-starter

## 1. Getting started

### 1.a. Local development

```
git clone <this repo>
cd <this repo>
cp .env.example .env
pipenv shell
pipenv install
cd dagster_starter
pip install -e ".[dev]"
dagster dev
```

### 1.b. First time?

```
dagster project scaffold --name <my_new_project>
pip install -e ".[dev]"
dagster dev
```

### 1.c. Tests

```
pytest -s dagster_starter_tests
```

## Theory

1. There are two components of Dagster - UI and daemon (to run the schedules)
2. Software-defined asets (SDA) are assets that represent data in your graph (e.g., notebooks, tables, models)

## References

1. https://www.youtube.com/watch?v=ZmUjf3gL1VU&t=1s
2. https://github.com/petehunt/dagster-github-stars-example/tree/master
