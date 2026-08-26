# 🏢 Workday Career Sites API: Find the Companies Using Workday

> Find the companies using Workday and every career site each one runs, as clean structured JSON: tenant, datacenter, careers URL, direct jobs API URL, and a live open-role count.

**Actor page:** [apify.com/johnvc/workday-career-sites-api](https://apify.com/johnvc/workday-career-sites-api?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/workday-career-sites-api/input-schema](https://apify.com/johnvc/workday-career-sites-api/input-schema?fpr=9n7kx3)

Give this API a company name and it returns every Workday career site that company runs, each with the tenant, datacenter, public careers URL, the direct jobs API URL, and how many roles are open right now. Turn on discovery mode and it enumerates companies using Workday in bulk, so you can build a Workday customer list for sales or research. It returns every board a company runs, not just the main one: large employers keep separate sites for regions, subsidiaries, and university hiring.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

### Text walkthrough

The primary use case is finding the **companies using Workday** and resolving each to its career sites. You give the API a list of company names or domains (the `companies` input), or you switch on `discoverAll` to enumerate in bulk. For each career site it returns `tenant`, `datacenter`, `siteSlug`, `careersUrl`, `apiUrl`, and `totalJobs`. The `apiUrl` field is the piece most people are after: a direct, ready-to-POST jobs endpoint you can page through to pull the actual postings. A concrete example from the published tasks: run it on `kla` and you get all seven of KLA's Workday boards, including its regional sites, each with a live open-role count. That is the difference from a single-company scraper, which stops at the first board. Sales and market-research teams use the bulk mode to turn Workday adoption into a lead list; data teams use the named mode to resolve a company to its Workday tenant and jobs API URL.

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Workday-Career-Sites-API.git
   cd Apify-Workday-Career-Sites-API
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python workday-career-sites-api-example.py
   # Optional recipes:
   # uv run python workday-career-sites-api-example.py --example companies_list
   # uv run python workday-career-sites-api-example.py --example every_site
   # uv run python workday-career-sites-api-example.py --example jobs_api_url
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python workday-career-sites-api-example.py
```

## Why Use This Workday Career Sites API?

Every other Workday tool needs you to already know the company's Workday URL, which means knowing the tenant, the datacenter, and the site slug. This API produces those, so it sits upstream of the job scrapers and feeds them.

The datacenter is the hard part. Every Workday career site lives in a specific datacenter (`wd1`, `wd5`, `wd108`, and so on) that is part of the URL and cannot be derived from the company name. This API resolves it for you, then hands back a working careers URL and a direct jobs API URL.

Discovery mode turns Workday adoption into a dataset. Enumerate companies using Workday in bulk, each with its careers URL and live open-role count, and you have a Workday customer list you can filter for sales, market research, or CRM enrichment.

It returns every board, not just one. A single company can run many career sites for regions, subsidiaries, and university hiring; this API returns all of them so nothing is missed.

## Features

### Core Capabilities
- Resolve a company name or domain to its Workday tenant, datacenter, and career sites
- Enumerate companies using Workday in bulk with `discoverAll`
- Return the direct jobs API URL for each site, ready to POST
- Report a live open-role count per site
- Return every career site a company runs, not just the main board

### Data Quality
- Clean structured JSON, one row per career site
- Only verified live sites are returned by default
- No API key needed for the underlying data, no login, no proxies

## Recipes

### Build a List of Companies Using Workday

[Run this on Apify](https://apify.com/johnvc/workday-career-sites-api/examples/build-a-list-of-companies-using-workday?fpr=9n7kx3): turn on discovery mode and get each company's tenant, careers URL, jobs API URL, and open-role count.

Local: `uv run python workday-career-sites-api-example.py --example companies_list`

### Build a Workday Customer List for Sales

[Run this on Apify](https://apify.com/johnvc/workday-career-sites-api/examples/build-a-workday-customer-list?fpr=9n7kx3): a sales-ready list of every company on Workday with its careers URL, tenant, and open-role count.

Local: `uv run python workday-career-sites-api-example.py --example companies_list`

### Find Every Workday Career Site a Company Runs

[Run this on Apify](https://apify.com/johnvc/workday-career-sites-api/examples/find-every-workday-career-site-a-company-runs?fpr=9n7kx3): all of a company's boards, each with careers URL, jobs API URL, and open roles.

Local: `uv run python workday-career-sites-api-example.py --example every_site`

### Get the Workday Jobs API URL for a Company

[Run this on Apify](https://apify.com/johnvc/workday-career-sites-api/examples/get-workday-jobs-api-url-for-a-company?fpr=9n7kx3): the direct jobs endpoint for a company's career sites, ready to POST.

Local: `uv run python workday-career-sites-api-example.py --example jobs_api_url`

### Find a Company's Workday Careers URL

[Run this on Apify](https://apify.com/johnvc/workday-career-sites-api/examples/find-a-company-workday-careers-url?fpr=9n7kx3): resolve a single company name to its Workday careers URL and jobs API URL.

**Schedule tip:** Save any of these inputs as an Apify Task and [schedule it](https://apify.com/johnvc/workday-career-sites-api?fpr=9n7kx3) to run daily or weekly so your dataset stays fresh without manual runs.

## Usage Examples

### Basic Example
```json
{
  "companies": ["nvidia", "kla"],
  "verifyLive": true
}
```

### Advanced Example
```json
{
  "discoverAll": true,
  "maxResults": 100,
  "crawlDepth": 2,
  "verifyLive": true
}
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `companies` | `array` | no | `["nvidia", "kla"]` | Company names or domains to resolve. Each returns every career site it runs. |
| `discoverAll` | `bool` | no | `false` | Enumerate companies using Workday in bulk instead of a named list. |
| `maxResults` | `int` | no | `100` | Cap on companies processed in discovery mode. One company can yield several rows. |
| `verifyLive` | `bool` | no | `true` | Check each site and record its live open-role count. |
| `includeInactive` | `bool` | no | `false` | Also return sites that failed verification. |
| `crawlDepth` | `int` | no | `2` | How many index snapshots to combine in discovery mode. |

## Output Format

```json
{
  "resultType": "career_site",
  "tenant": "kla",
  "companyName": "kla",
  "datacenter": "wd1",
  "hostKind": "myworkdayjobs",
  "siteSlug": "Penang_Semicon",
  "careersUrl": "https://kla.wd1.myworkdayjobs.com/en-US/Penang_Semicon",
  "apiUrl": "https://kla.wd1.myworkdayjobs.com/wday/cxs/kla/Penang_Semicon/jobs",
  "totalJobs": 37,
  "status": "live",
  "slugSource": "robots",
  "discoveredAt": "2026-07-31T18:54:41+00:00"
}
```

## People also search for

### Is this a Workday scraper or an API?

This repo teaches the **Workday Career Sites API** on Apify. People often search for a "workday scraper" or "workday jobs scraper"; this Actor covers the discovery side of that need and returns structured JSON you can call from Python or MCP. It finds the career sites and the jobs API URL; you feed that URL to a job scraper to pull the postings.

### How do I get a list of companies using Workday?

Clone this repo, set `APIFY_API_TOKEN`, and run `uv run python workday-career-sites-api-example.py --example companies_list`. That runs discovery mode and returns one row per career site with the company tenant and open-role count. See Quick Start and Recipes above.

### What is a Workday tenant, and how do I find it?

The tenant is the company's own label inside Workday, the first part of its career-site hostname (for `nvidia.wd5.myworkdayjobs.com`, the tenant is `nvidia`). Pass a company name to this API and it returns the tenant and datacenter for you.

### Can I use this with MCP or Claude?

Yes. Use the install sections below to add the Actor as an MCP tool in [Claude Code](https://claude.ai/referral/uIlpa7nPLg) (free trial), [Claude Cowork](https://claude.ai/referral/uIlpa7nPLg) (free trial), Claude.ai, Cursor, or ChatGPT.

## Related Tools

Chain this discovery API with the [Workday Careers API](https://apify.com/johnvc/workday-careers-api?fpr=9n7kx3): this repo finds the career sites and the `apiUrl`; that Actor extracts every job posting from a site's URL. Discovery here, extraction there.

## n8n integration

Available as an n8n community node, **[n8n-nodes-workday-career-sites-api](https://www.npmjs.com/package/n8n-nodes-workday-career-sites-api)**. In n8n: Settings, Community Nodes, install `n8n-nodes-workday-career-sites-api`, then use it in any workflow (it also works as an AI Agent tool).

---

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the Workday Career Sites API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/workday-career-sites-api"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the Workday Career Sites API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

---

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/workday-career-sites-api"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/workday-career-sites-api" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the Workday Career Sites API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

---

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/workday-career-sites-api`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/workday-career-sites-api`, using OAuth when prompted.
5. Ask Claude to run the Workday Career Sites API.

Open Claude on the web: https://claude.ai

---

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/workday-career-sites-api"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/workday-career-sites-api",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the Workday Career Sites API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

---

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/workday-career-sites-api`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the Workday Career Sites API to find the companies using Workday and power your data workflows with reliable, structured results.*

Last Updated: 2026.08.26
