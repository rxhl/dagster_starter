# dagster_starter

![Architecture](/assets/arch.png)

Read the full article [here](https://rxhl.notion.site/Decoding-the-EL-in-ELT-f3f56ed7e2d947c0b1618b5bee293256).

## Getting started

Make sure you have a GitHub token (fine-grained) with the permission to create gists. See [here](https://github.blog/2022-10-18-introducing-fine-grained-personal-access-tokens-for-github/) for more details on creating one.

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
