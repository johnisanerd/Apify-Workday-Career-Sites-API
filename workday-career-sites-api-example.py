"""
Workday Career Sites API: A Quick Start Example
See more at: https://apify.com/johnvc/workday-career-sites-api?fpr=9n7kx3
Input schema: https://apify.com/johnvc/workday-career-sites-api/input-schema?fpr=9n7kx3

This script shows how to call the Workday Career Sites API on Apify from Python
and read its structured JSON output. Give it a company name and it returns every
Workday career site that company runs: the tenant, datacenter, careers URL, the
direct jobs API URL, and a live open-role count. Turn on discovery mode to build
a list of companies using Workday in bulk.

The default run stays cheap on purpose. The optional --example recipes mirror
published Store tasks (see the README Recipes section).

Get your free Apify API key at: https://apify.com?fpr=9n7kx3

Examples:
  uv run python workday-career-sites-api-example.py
  uv run python workday-career-sites-api-example.py --example companies_list
  uv run python workday-career-sites-api-example.py --example every_site
  uv run python workday-career-sites-api-example.py --example jobs_api_url
"""

from __future__ import annotations

import argparse
import os
from typing import Any

from apify_client import ApifyClient
from dotenv import load_dotenv

load_dotenv()

ACTOR_ID = "johnvc/workday-career-sites-api"


def _print_sites(items: list[dict[str, Any]]) -> None:
    """Print a short summary of each career site returned.

    Args:
        items: Rows returned from the Actor's default dataset, one per site.
    """
    print(f"Returned {len(items)} career site(s).\n")
    for site in items:
        tenant = site.get("tenant", "")
        slug = site.get("siteSlug", "")
        jobs = site.get("totalJobs")
        jobs_text = f"{jobs} open roles" if jobs is not None else "not verified"
        print(f"- {tenant} / {slug} ({jobs_text})")
        print(f"    careers: {site.get('careersUrl', '')}")
        print(f"    jobs API: {site.get('apiUrl', '')}")


def run_default(client: ApifyClient) -> None:
    """Cheap general quick-start: resolve two companies to their career sites.

    Named lookups are inexpensive, so this default keeps costs low while still
    showing the full output shape, including a multi-site company (KLA).
    """
    run_input: dict[str, Any] = {
        "companies": ["nvidia", "kla"],
        "verifyLive": True,
    }
    run = client.actor(ACTOR_ID).call(run_input=run_input)
    if run is None:
        raise SystemExit("The Actor run did not return a result.")
    items = list(client.dataset(run.default_dataset_id).iterate_items())
    _print_sites(items)


def run_companies_list(client: ApifyClient) -> None:
    """Build a list of companies using Workday in bulk.

    Mirrors the published task "Build a List of Companies Using Workday":
    https://apify.com/johnvc/workday-career-sites-api/examples/build-a-list-of-companies-using-workday?fpr=9n7kx3

    maxResults is clamped small here to keep the first run inexpensive. Raise it
    once you know your budget.
    """
    run_input: dict[str, Any] = {
        "discoverAll": True,
        "maxResults": 25,
        "verifyLive": True,
    }
    run = client.actor(ACTOR_ID).call(run_input=run_input)
    if run is None:
        raise SystemExit("The Actor run did not return a result.")
    items = list(client.dataset(run.default_dataset_id).iterate_items())
    _print_sites(items)


def run_every_site(client: ApifyClient) -> None:
    """Return every career site a company runs, not just the main one.

    Mirrors the published task "Find Every Workday Career Site a Company Runs":
    https://apify.com/johnvc/workday-career-sites-api/examples/find-every-workday-career-site-a-company-runs?fpr=9n7kx3

    KLA and Cadence each run several boards for regions and university hiring.
    """
    run_input: dict[str, Any] = {
        "companies": ["kla", "cadence"],
        "verifyLive": True,
    }
    run = client.actor(ACTOR_ID).call(run_input=run_input)
    if run is None:
        raise SystemExit("The Actor run did not return a result.")
    items = list(client.dataset(run.default_dataset_id).iterate_items())
    _print_sites(items)


def run_jobs_api_url(client: ApifyClient) -> None:
    """Get the direct jobs API URL for a company's Workday career sites.

    Mirrors the published task "Get the Workday Jobs API URL for a Company":
    https://apify.com/johnvc/workday-career-sites-api/examples/get-workday-jobs-api-url-for-a-company?fpr=9n7kx3

    Each returned apiUrl is a ready-to-POST endpoint you can page through to pull
    the actual postings.
    """
    run_input: dict[str, Any] = {
        "companies": ["adobe"],
        "verifyLive": True,
    }
    run = client.actor(ACTOR_ID).call(run_input=run_input)
    if run is None:
        raise SystemExit("The Actor run did not return a result.")
    items = list(client.dataset(run.default_dataset_id).iterate_items())
    for site in items:
        print(site.get("apiUrl", ""))


def main() -> None:
    """Dispatch a quick-start or a task-aligned recipe."""
    parser = argparse.ArgumentParser(description="Workday Career Sites API examples")
    parser.add_argument(
        "--example",
        default="default",
        choices=["default", "companies_list", "every_site", "jobs_api_url"],
        help="Which recipe to run (see the README Recipes section).",
    )
    args = parser.parse_args()

    token = os.getenv("APIFY_API_TOKEN")
    if not token:
        raise SystemExit("Set APIFY_API_TOKEN in .env or the environment.")

    client = ApifyClient(token)
    dispatch = {
        "default": run_default,
        "companies_list": run_companies_list,
        "every_site": run_every_site,
        "jobs_api_url": run_jobs_api_url,
    }
    dispatch[args.example](client)


if __name__ == "__main__":
    main()
