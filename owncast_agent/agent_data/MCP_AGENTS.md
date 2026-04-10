# MCP_AGENTS.md - Dynamic Agent Registry

This file tracks the generated agents from MCP servers. You can manually modify the 'Tools' list to customize agent expertise.

## Agent Mapping Table

| Name | Description | System Prompt | Tools | Tag | Source MCP |
|------|-------------|---------------|-------|-----|------------|
| Owncast Chat  Specialist | Expert specialist for chat_ domain tasks. | You are a Owncast Chat  specialist. Help users manage and interact with Chat  functionality using the available tools. | owncast_chat__toolset | chat_ | owncast |
| Owncast External  Specialist | Expert specialist for external_ domain tasks. | You are a Owncast External  specialist. Help users manage and interact with External  functionality using the available tools. | owncast_external__toolset | external_ | owncast |
| Owncast Internal  Specialist | Expert specialist for internal_ domain tasks. | You are a Owncast Internal  specialist. Help users manage and interact with Internal  functionality using the available tools. | owncast_internal__toolset | internal_ | owncast |
| Owncast Objects  Specialist | Expert specialist for objects_ domain tasks. | You are a Owncast Objects  specialist. Help users manage and interact with Objects  functionality using the available tools. | owncast_objects__toolset | objects_ | owncast |

## Tool Inventory Table

| Tool Name | Description | Tag | Source |
|-----------|-------------|-----|--------|
| owncast_chat__toolset | Static hint toolset for chat_ based on config env. | chat_ | owncast |
| owncast_external__toolset | Static hint toolset for external_ based on config env. | external_ | owncast |
| owncast_internal__toolset | Static hint toolset for internal_ based on config env. | internal_ | owncast |
| owncast_objects__toolset | Static hint toolset for objects_ based on config env. | objects_ | owncast |
