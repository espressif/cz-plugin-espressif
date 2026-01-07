
---

Commit message schema:

    <type>(<scope>): <subject>
        <... empty line ...>
    <body>
        <... empty line ...>
    (BREAKING CHANGE: <breaking changes>)*
    (<footers>)*

---

Commit types in this project:

  feat: A new feature
  fix: A bug fix
  perf: A code change that improves performance
  docs: Documentation only change
  refactor: A changeset neither fixing a bug nor adding a feature
  remove: Removing code or files
  change: A change made to the codebase.
  ci: Changes to CI configuration files and scripts
  test: Adding missing or correcting existing tests
  revert: Revert one or more commits


---

Short commit messages (one line):

    fix: fix something (present or imperative, no period)
    fix(package): fix something
    feat(name): add a new feature
    refactor(package)!: this refactoring breaks the thing

---

Full commit messages with body and footer:

    feat(something): add something new (present/imperative, no period)

    Here optionally comes the details - this is commit message body.
    It can be multiline, hyphens, asterisks, are okay.

    BREAKING CHANGE: It breaks something!
    Closes https://github.com/espressif/<project>/issues/<issue_number>

---

More info:

- https://www.conventionalcommits.org/en/v1.0.0/#specification
- https://github.com/espressif/conventional-precommit-linter
- https://github.com/espressif/standards
    