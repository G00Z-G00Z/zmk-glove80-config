---
name: skills/read-todoist-improvements
description: Reads the tasks from my todoist instance to get the next features for my keyboard configuration
---

# skills/read-todoist-improvements

Use the todoist mcp. If not available or misconfigured, halt and tell the user that they must configure it correclty.

Then read the following query: `#ZF & /Keyboard Improvements` and get all the tasks including the subtasks.

Then ask the user which of the features he wants to start a sdd.

Then after they select which ones, ask the user if they want 1 sdd or several.

Finally start sdd by asking more details on the task and then proceed with openspec sdd normally

## When to use

When the user asks you to "fetch backlog features", "fetch todoist improvements" or "fetch next improvements list". Anything that implies the "next steps"

## Instructions

1. Check todoist mcp
1. Fetch: `#ZF & /Keyboard Improvements`, all tasks and subtasks
1. Prompt the user to select which features
1. Prompt to decide if combine them into 1 sdd or multiple
1. Ask for more details on the skill
1. Start sdd with open spec as normally
