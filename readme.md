# Zed Test Runner

Run tests with shortcuts in Zed editor.

## Features

- Run tests from an entire jest file
- Run test case based on cursor position

# Setup

1. Clone this repository.
2. Create an alias to run main.py and add it to your `.zshrc` or `.bashrc` file.

```
alias zed-test-runner="python3 /Users/danny/personal/zed-test-runner/main.py"
```

3. Add the tasks definitions to your `task.json` file

```
[
  {
    "label": "run jest file",
    "command": "node 'node_modules/.bin/jest' $ZED_FILE",
    "use_new_terminal": false
  },
  {
    "label": "run cursor jest test",
    "command": "zed-test-runner $ZED_WORKTREE_ROOT $ZED_FILE $ZED_ROW",
    "use_new_terminal": false
  }
]
```

4. Create the Zod Keymaps

```
[
  {
    "context": "Workspace",
    "bindings": {
      "cmd-alt-l": ["task::Spawn", { "task_name": "run jest file" }],
      "cmd-alt-k": ["task::Spawn", { "task_name": "run cursor jest test" }]
    }
  }
]
```
