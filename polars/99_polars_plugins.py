# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "polars==1.33.1",
# ]
# ///

import marimo

__generated_with = "0.16.0"
app = marimo.App(width="columns")


@app.cell(column=0, hide_code=True)
def _(mo):
    mo.md(r"""## Setup""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Pre-Requirements

    - Rust
    - Cargo
    - Maturin

    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Imports""")
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import polars as pl
    return (pl,)


@app.cell
def _():
    from polars.plugins import register_plugin_function
    return (register_plugin_function,)


@app.cell
def _():
    import tempfile
    return (tempfile,)


@app.cell
def _():
    import pathlib
    return (pathlib,)


@app.cell
def _():
    import subprocess
    return (subprocess,)


@app.cell
def _():
    import shutil
    return (shutil,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Utilities""")
    return


@app.cell
def _(pathlib, tempfile):
    temp_root = pathlib.Path(tempfile.gettempdir())
    return (temp_root,)


@app.cell
def _(mo):
    def code(proj, file: str, content: str):
        if proj is not None:
            dest = proj / file
            dest.parent.mkdir(exist_ok=True, parents=True)
            dest.write_text(content)
        return mo.md(f"`{file}`:\n```{file.rsplit('.', 1)[-1]}\n{content}\n```")
    return (code,)


@app.cell
def _(mo, subprocess):
    def term(workdir, *args):
        mo.stop(workdir is None, "Need a directory before running command")
        result = subprocess.run(args, cwd=workdir, capture_output=True)
        _head = f"`{workdir}$ {' '.join(args)}`:\n"
        _stdout = f"```\n{result.stdout.decode('UTF-8')}\n```\n" if result.stdout else "\n"
        _stderr = f"```\n{result.stderr.decode('UTF-8')}\n```\n" if result.stdout else "\n"
        return mo.md(f"{_head}{_stdout}{_stderr}".strip())
    return (term,)


@app.cell
def _(mo):
    get_project_directory, set_project_directory = mo.state(None)
    return get_project_directory, set_project_directory


@app.cell
def _(mo):
    create_project_button = mo.ui.run_button(label="Create Project")
    return (create_project_button,)


@app.cell
def _(mo):
    compile_project_button = mo.ui.run_button(label="Compile Project")
    return (compile_project_button,)


@app.cell(column=1, hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Rust Project

    Files that are created when you click the `Create Project` button
    """
    )
    return


@app.cell(hide_code=True)
def _(code, get_project_directory):
    cargo_toml = """
    [package]
    name = "expression_lib"
    version = "0.1.0"
    edition = "2021"

    [lib]
    name = "expression_lib"
    crate-type = ["cdylib"]

    [dependencies]
    polars = { version = "*", features=["dtype-struct", "dtype-array"] }
    pyo3 = { version = "*", features = ["extension-module", "abi3-py38"] }
    pyo3-polars = { version = "*", features = ["derive"] }
    serde = { version = "*", features = ["derive"] }
    """
    # NOTE: dtype-struct and dtype-array were added because of https://github.com/pola-rs/polars/issues/24551
    code(get_project_directory(), "Cargo.toml", cargo_toml)
    return


@app.cell(hide_code=True)
def _(code, get_project_directory):
    pyproject_toml = """
    [build-system]
    requires = ["maturin>=1.0,<2.0"]
    build-backend = "maturin"

    [project]
    name = "expression_lib"
    version = "0.0.1"
    requires-python = ">=3.8"
    classifiers = [
      "Programming Language :: Rust",
      "Programming Language :: Python :: Implementation :: CPython",
    ]
    """
    code(get_project_directory(), "pyproject.toml", pyproject_toml)
    return


@app.cell(hide_code=True)
def _(code, get_project_directory):
    src_expressions_rs = """
    use polars::prelude::*;
    use pyo3_polars::derive::polars_expr;
    use std::fmt::Write;

    fn pig_latin_str(value: &str, output: &mut String) {
        if let Some(first_char) = value.chars().next() {
            write!(output, "{}{}ay", &value[1..], first_char).unwrap()
        }
    }

    #[polars_expr(output_type=String)]
    fn pig_latinnify(inputs: &[Series]) -> PolarsResult<Series> {
        let ca = inputs[0].str()?;
        let out: StringChunked = ca.apply_into_string_amortized(pig_latin_str);
        Ok(out.into_series())
    }
    """
    code(get_project_directory(), "src/expressions.rs", src_expressions_rs)
    return


@app.cell(hide_code=True)
def _(code, get_project_directory):
    src_lib_rs = """
    use pyo3_polars::PolarsAllocator;

    mod expressions;

    #[global_allocator]
    static ALLOC: PolarsAllocator = PolarsAllocator::new();
    """
    code(get_project_directory(), "src/lib.rs", src_lib_rs)
    return


@app.cell(column=2, hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Build Extension Dynamic Library

    Copies required files to a temporary folder when you `Create Project`, then builds it once you `Compile Project`
    """
    )
    return


@app.cell(hide_code=True)
def _(compile_project_button, create_project_button, mo):
    mo.hstack([create_project_button, compile_project_button], justify="center")
    return


@app.cell
def _(
    create_project_button,
    get_project_directory,
    mo,
    pathlib,
    set_project_directory,
    shutil,
    temp_root,
    tempfile,
):
    mo.stop(not create_project_button.value, "Press the Create Project button")
    old = get_project_directory()
    if old is not None and old.is_relative_to(temp_root):
        shutil.rmtree(old)
    folder = pathlib.Path(tempfile.mkdtemp())
    set_project_directory(pathlib.Path(folder))
    return


@app.cell
def _(get_project_directory, term):
    term(get_project_directory(), "ls", "-R")
    return


@app.cell
def _(compile_project_button, get_project_directory, mo, term):
    mo.stop(
        not compile_project_button.value,
        "Press the Compile Project button or run `maturin build` yourself in the directory if you'd rather)",
    )

    term(get_project_directory(), "maturin", "build")
    return


@app.cell
def _(get_project_directory, mo):
    ext_directory = get_project_directory() / "target/maturin"
    ext_watcher = mo.watch.directory(ext_directory)
    return (ext_watcher,)


@app.cell(column=3, hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Calling plugin methods from Python

    Register the generated extension and call it
    """
    )
    return


@app.cell
def _(ext_watcher, pl, register_plugin_function):
    def pig_latinnify(expr) -> pl.Expr:
        return register_plugin_function(
            plugin_path=ext_watcher.absolute(),
            args=[expr],
            function_name="pig_latinnify",
            is_elementwise=True,
        )
    return (pig_latinnify,)


@app.cell
def _(pl):
    df = pl.DataFrame({"text": ["Hello World!", "Three Pigs Playing in the mud"]})
    df
    return (df,)


@app.cell
def _(df, pig_latinnify, pl):
    df.with_columns(pig_latinnify(pl.col("text")).alias("pig"))
    return


@app.cell
def _(df, pig_latinnify, pl):
    df.with_columns(pl.col("text").str.split(" ").list.eval(pig_latinnify(pl.element())).list.join(" ").alias("pig"))
    return


if __name__ == "__main__":
    app.run()
