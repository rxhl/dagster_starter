from dagster import (
    load_assets_from_package_module,
    Definitions,
    define_asset_job,
    ScheduleDefinition,
)
from . import assets
import os
from dotenv import load_dotenv
from github import Github

load_dotenv()

defs = Definitions(
    assets=load_assets_from_package_module(assets),
    schedules=[
        ScheduleDefinition(
            job=define_asset_job(name="every_minute", selection="*"),
            cron_schedule="* * * * *",
        )
    ],
    resources={"github_api": Github(os.environ.get("GITHUB_ACCESS_TOKEN"))},
)
