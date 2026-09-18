# Contributing to Document Intelligence CLI

Thank you for your interest in contributing to Document Intelligence CLI.

The goal of this project is to remain small, readable, testable, and easy to understand.

Contributions should preserve those qualities.

## Getting Started

### 1. Fork the Repository

Create a fork of the repository on GitHub.

### 2. Clone the Repository

```bash
git clone https://github.com/michaelbag8/document-intelligence-cli.git
cd document-intelligence-cli
```

### 3. Create a Virtual Environment

```bash
python3 -m venv .venv
```

### 4. Activate the Virtual Environment

Linux, macOS, and WSL:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install the Project

```bash
python -m pip install -e .
```

### 6. Install Development Dependencies

The project currently uses `pytest` for testing.

```bash
python -m pip install pytest
```

## Project Structure

```text
src/docintel/
├── cli.py
├── extractors.py
├── __main__.py
├── processor.py
├── reader.py
├── report.py
└── validators.py

tests/
├── test_cli.py
├── test_extractors.py
├── test_processor.py
├── test_report.py
└── test_validators.py
```

## Module Responsibilities

Keep responsibilities separated between modules.

### `reader.py`

Responsible for reading documents.

### `extractors.py`

Responsible for finding candidate values in document text.

### `validators.py`

Responsible for validating extracted candidates.

### `processor.py`

Responsible for coordinating extraction and validation.

### `report.py`

Responsible for formatting processed results.

### `cli.py`

Responsible for command-line interaction and user-facing behavior.

### `__main__.py`

Provides module-based execution through:

```bash
python -m docintel
```

Avoid moving responsibilities between modules unless there is a clear architectural reason.

## Development Workflow

Before making a change:

1. Understand the existing behavior.
2. Identify which module owns the responsibility.
3. Review the relevant tests.
4. Decide what behavior should change.
5. Make the smallest reasonable change.
6. Add or update tests.
7. Run the complete test suite.
8. Review the final changes.

The general workflow is:

```text
Understand
    ↓
Plan
    ↓
Implement
    ↓
Test
    ↓
Review
```

## Adding a New Extraction Type

A new extraction type should be considered as a complete pipeline feature.

```text
Document
   ↓
Extractor
   ↓
Candidate values
   ↓
Validator
   ↓
Processor
   ↓
Report
```

When adding a new extraction type:

1. Add the extractor to `extractors.py`.
2. Add validation logic to `validators.py` when validation is required.
3. Connect the extractor and validator in `processor.py`.
4. Add extractor tests.
5. Add validator tests.
6. Add processor tests.
7. Update the README.
8. Run the complete test suite.

Do not describe an extraction type as a supported CLI feature until it is connected to the processing pipeline and appears in the final result.

## Writing Tests

Every new feature or behavior change should have appropriate tests.

Tests should cover both normal and edge-case behavior.

For a validator, consider testing:

* Valid input
* Invalid input
* Empty input
* Boundary values
* Unexpected characters
* Malformed input

For an extractor, consider testing:

* One valid candidate
* Multiple candidates
* No candidates
* Candidates surrounded by other text
* Invalid or malformed candidates
* Boundary cases

### Test Naming

Test names should clearly describe the behavior being tested.

Prefer:

```python
def test_invalid_email_without_domain():
    ...
```

over:

```python
def test_email():
    ...
```

A developer should be able to understand what a test verifies from its name.

## Running Tests

Run the complete test suite:

```bash
python -m pytest
```

Run a specific test file:

```bash
python -m pytest tests/test_extractors.py
```

Run a specific test:

```bash
python -m pytest tests/test_validators.py::test_valid_email
```

All tests should pass before submitting a pull request.

## Code Style

Keep code:

* Readable
* Simple
* Explicit
* Consistent
* Properly structured
* Focused on a single responsibility

Use type hints where appropriate.

Avoid unnecessary abstractions.

For example, do not introduce a class when a simple function is sufficient.

Do not introduce a dependency when the Python standard library can reasonably solve the problem.

## Error Handling

Expected user errors should be handled deliberately.

Examples include:

* Missing files
* Empty documents
* Invalid input
* Permission errors

Avoid unnecessarily broad exception handling such as:

```python
try:
    ...
except Exception:
    ...
```

Unexpected programming errors should generally remain visible during development rather than being silently hidden.

## Documentation

Update documentation when a change affects user-visible behavior.

Documentation may need to include changes to:

* `README.md`
* Supported extraction types
* CLI commands
* Command-line options
* Example input/output
* Limitations
* Installation instructions

Documentation must describe functionality that actually exists.

For example, having an `extract_urls()` function in `extractors.py` does not by itself mean that URL extraction is a supported CLI feature.

The feature should be connected to the processing pipeline before being documented as an end-to-end capability.

## Commit Messages

Use clear commit messages that describe the change.

Good examples:

```text
Add date extraction tests
```

```text
Improve phone number validation
```

```text
Handle missing files in CLI
```

```text
Add JSON report output
```

Avoid vague messages such as:

```text
fix stuff
```

or:

```text
changes
```

A commit should communicate what changed.

## Pull Requests

Before opening a pull request, run:

```bash
python -m pytest
```

Make sure that:

* Existing tests pass.
* New functionality has appropriate tests.
* Existing functionality has not been unintentionally changed.
* Documentation has been updated when necessary.
* The change has a clear purpose.
* No unnecessary dependencies have been introduced.

### Pull Request Description

Explain:

1. What changed?
2. Why was it changed?
3. What tests were added or updated?
4. How was the change verified?

For example:

```text
## What changed?

Added validation for calendar dates.

## Why?

The date extractor can identify values such as 2024-02-30,
but the value is not a valid calendar date.

## Tests

Added tests for:

- Valid leap-year dates
- Invalid February dates
- Invalid month values

## Verification

python -m pytest
```

## Reporting Bugs

When reporting a bug, include:

* What you expected to happen
* What actually happened
* The command or input that produced the problem
* Relevant error output
* Python version
* Operating system

A small reproducible example is especially helpful.

## Suggesting Features

Feature suggestions are welcome.

When proposing a feature, explain:

* What problem it solves
* Expected behavior
* Example input
* Expected output
* Whether it changes existing CLI behavior

For extraction-related features, also describe:

* Values that should be accepted
* Values that should be rejected
* How the values should appear in the final report

## Dependencies

Keep dependencies to a minimum.

Before adding a new dependency, consider whether the Python standard library can reasonably provide the required functionality.

If a dependency is necessary, explain:

* Why it is needed
* What problem it solves
* Why the standard library is insufficient

Update the appropriate project configuration when adding dependencies.

## Architecture Guidelines

The project uses separation of responsibilities.

The normal flow is:

```text
CLI
 ↓
Reader
 ↓
Processor
 ├── Extractors
 └── Validators
 ↓
Report
```

Changes should preserve this separation where practical.

For example:

* `reader.py` should not generate reports.
* `extractors.py` should not print CLI messages.
* `validators.py` should not handle command-line arguments.
* `report.py` should not read files.
* `cli.py` should coordinate the application rather than contain extraction logic.

## Keeping the Project Focused

Document Intelligence CLI is intentionally a focused project.

The objective is not to make the codebase as large as possible.

The objective is to build a clear, reliable, maintainable command-line application.

Before introducing a major abstraction, dependency, command, or architectural change, consider whether the existing design can solve the problem more simply.

## License

This project is licensed under the MIT License.

By contributing to this project, you agree that your contributions will be licensed under the same license.