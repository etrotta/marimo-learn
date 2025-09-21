# Translation Guidelines

This document outlines the guidelines for translating the course content in this repository.

## Directory Structure

All translations should be placed in the top-level `i18n` directory.

1.  Create a subdirectory for each language using its two-letter [ISO 639-1 code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g., `es` for Spanish, `fr` for French).
2.  Inside the language directory, replicate the directory structure of the original notebooks.

For example, to create a Spanish translation for a Polars notebook:

-   **Original notebook:** `polars/01_why_polars.py`
-   **Spanish translation:** `i18n/es/polars/01_why_polars.py`

## What to Translate

When translating a notebook file (which is a `.py` script for `marimo`), you should only translate the natural language text. This includes:

-   **Markdown Content:** All text inside `mo.md(...)` blocks.
-   **Code Comments:** Any comments in the code (e.g., `# This is a comment`).
-   **User-Facing Strings:** Any string literals that are displayed to the user, such as plot titles, axis labels, or messages in `print()` statements.

## What NOT to Translate

**Do not translate the code itself.** The code must remain identical to the original file to be executable. This includes:

-   Variable names
-   Function names
-   Class names
-   Module names
-   Keywords and operators
-   Arguments to functions (unless they are user-facing strings)

## Exceptions to that rule

If a name or field originated from the language the Notebook is being translated to, or if translating it would make the material significantly easier to grasp for the target audience, it should use the localized language if possible.

## Translating vs Localizing

Avoid literal translations of expressions the target audience may not understand, instead adapt them to deliver the key points in a natural way over preserving the exact choice of words. Take into consideration cultural nuances and social customs.

### Example

**Original:**
```python
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r'''
    ### Counting nulls

    A simple yet convenient aggregation
    '''
    )
    return

@app.cell
def _(df):
    # This cell counts nulls
    df.null_count()
    return
```

**Correct Spanish Translation:**
```python
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r'''
    ### Contando nulos

    Una agregación simple pero conveniente
    '''
    )
    return

@app.cell
def _(df):
    # Esta celda cuenta los nulos
    df.null_count() # The code is not translated
    return
```

By following these guidelines, we can ensure that all translated notebooks are consistent and remain fully functional.
