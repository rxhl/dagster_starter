# dagster_starter

## Getting started

### Local development

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

### Starting from scratch?

```
dagster project scaffold --name <my_new_project>
pip install -e ".[dev]"
dagster dev
```

### Tests

```
pytest -s dagster_starter_tests
```

## References

1. https://www.youtube.com/watch?v=ZmUjf3gL1VU&t=1s
2. https://github.com/petehunt/dagster-github-stars-example/tree/master
