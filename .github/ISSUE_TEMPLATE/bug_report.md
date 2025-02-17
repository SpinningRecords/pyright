---
name: Bug report
about: Create a report to help us improve pyright
title: ''
labels: ''
assignees: ''

---

Note: if you are reporting a wrong signature of a function or a class in the standard library, then the typeshed tracker is better suited for this report: https://github.com/python/typeshed/issues.

If you have a question about typing or a behavior that you’re seeing in Pyright (as opposed to a bug report or enhancement request), consider posting to the [Pyright discussion forum](https://github.com/microsoft/pyright/discussions).

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior.

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots or Code**
If possible, provide a minimal, self-contained code sample (surrounded by triple back ticks) to demonstrate the issue. The code should define or imports all referenced symbols.

```python
def foo(self) -> str:
    return 3
```

If your code relies on symbols that are imported from a third-party library, include the associated import statements and specify which versions of those libraries you have installed.

**VS Code extension or command-line**
Are you running pyright as a VS Code extension or a command-line tool? Which version? You can find the version of the VS Code extension by clicking on the Pyright icon in the extensions panel.

**Additional context**
Add any other context about the problem here.
