# Owncast Agent - A2A | AG-UI | MCP

![PyPI - Version](https://img.shields.io/pypi/v/owncast-agent)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')
![PyPI - Downloads](https://img.shields.io/pypi/dd/owncast-agent)
![GitHub Repo stars](https://img.shields.io/github/stars/Knuckles-Team/owncast-agent)
![GitHub forks](https://img.shields.io/github/forks/Knuckles-Team/owncast-agent)
![GitHub contributors](https://img.shields.io/github/contributors/Knuckles-Team/owncast-agent)
![PyPI - License](https://img.shields.io/pypi/l/owncast-agent)
![GitHub](https://img.shields.io/github/license/Knuckles-Team/owncast-agent)

![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/Knuckles-Team/owncast-agent)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Knuckles-Team/owncast-agent)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/Knuckles-Team/owncast-agent)
![GitHub issues](https://img.shields.io/github/issues/Knuckles-Team/owncast-agent)

![GitHub top language](https://img.shields.io/github/languages/top/Knuckles-Team/owncast-agent)
![GitHub language count](https://img.shields.io/github/languages/count/Knuckles-Team/owncast-agent)
![GitHub repo size](https://img.shields.io/github/repo-size/Knuckles-Team/owncast-agent)
![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/Knuckles-Team/owncast-agent)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/owncast-agent)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/owncast-agent)

*Version: 0.1.4*

## Overview

**Owncast Agent MCP Server + A2A Agent**

Agent for interacting with Owncast API

This repository is actively maintained - Contributions are welcome!

## MCP

### Using as an MCP Server

The MCP Server can be run in two modes: `stdio` (for local testing) or `http` (for networked access).

#### Environment Variables

*   `OWNCAST_URL`: The URL of the target service.
*   `OWNCAST_TOKEN`: The API token or access token.

#### Run in stdio mode (default):
```bash
export OWNCAST_URL="http://localhost:8080"
export OWNCAST_TOKEN="your_token"
owncast-mcp --transport "stdio"
```

#### Run in HTTP mode:
```bash
export OWNCAST_URL="http://localhost:8080"
export OWNCAST_TOKEN="your_token"
owncast-mcp --transport "http" --host "0.0.0.0" --port "8000"
```

## A2A Agent

### Run A2A Server
```bash
export OWNCAST_URL="http://localhost:8080"
export OWNCAST_TOKEN="your_token"
owncast-agent --provider openai --model-id gpt-4o --api-key sk-...
```

## Docker

### Build

```bash
docker build -t owncast-agent .
```

### Run MCP Server

```bash
docker run -d \
  --name owncast-agent \
  -p 8000:8000 \
  -e TRANSPORT=http \
  -e OWNCAST_URL="http://your-service:8080" \
  -e OWNCAST_TOKEN="your_token" \
  knucklessg1/owncast-agent:latest
```

### Deploy with Docker Compose

```yaml
services:
  owncast-agent:
    image: knucklessg1/owncast-agent:latest
    environment:
      - HOST=0.0.0.0
      - PORT=8000
      - TRANSPORT=http
      - OWNCAST_URL=http://your-service:8080
      - OWNCAST_TOKEN=your_token
    ports:
      - 8000:8000
```

#### Configure `mcp.json` for AI Integration (e.g. Claude Desktop)

```json
{
  "mcpServers": {
    "owncast": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "owncast-agent",
        "owncast-mcp"
      ],
      "env": {
        "OWNCAST_URL": "http://your-service:8080",
        "OWNCAST_TOKEN": "your_token"
      }
    }
  }
}
```

## Install Python Package

```bash
python -m pip install owncast-agent
```
```bash
uv pip install owncast-agent
```

## Repository Owners

<img width="100%" height="180em" src="https://github-readme-stats.vercel.app/api?username=Knucklessg1&show_icons=true&hide_border=true&&count_private=true&include_all_commits=true" />

![GitHub followers](https://img.shields.io/github/followers/Knucklessg1)
![GitHub User's stars](https://img.shields.io/github/stars/Knucklessg1)
