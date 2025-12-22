# /// script
# requires-python = "==3.13"
# dependencies = [
#     "adbc-driver-sqlite==1.7.0",
#     "duckdb==1.4.0",
#     "lxml==6.0.2",
#     "marimo",
#     "pandas==2.3.2",
#     "polars==1.32.3",
#     "pyarrow==21.0.0",
#     "sqlalchemy==2.0.43",
# ]
# ///

import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Carregando Dados

    _Por [etrotta](https://github.com/etrotta)._

    Este tutorial aborda como carregar dados de vários formatos e de diferentes fontes usando [polars](https://docs.pola.rs/).

    Ele inclui exemplos de como carregar e gravar em uma variedade de formatos, mostra como converter dados de outras bibliotecas para suportar formatos não diretamente suportados por polars, inclui links relevantes para usuários que precisam se conectar a fontes externas e explica como lidar com formatos personalizados via plugins.
    """)
    return


@app.cell(hide_code=True)
def _(mo, pl):
    df = pl.DataFrame(
        [
            {"format": "Parquet", "lazy": True, "notes": None},
            {"format": "CSV", "lazy": True, "notes": None},
            {
                "format": "Databases",
                "lazy": False,
                "notes": "Requires another library as an Engine",
            },
            {
                "format": "Excel",
                "lazy": False,
                "notes": "Requires another library as an Engine",
            },
            {
                "format": "Newline-delimited JSON",
                "lazy": True,
                "notes": None,
            },
            {
                "format": "Traditional JSON",
                "lazy": False,
                "notes": None,
            },
            {"format": "Arrow", "lazy": False, "notes": "You can load XML and HTML files via pandas"},
            {"format": "Plugins", "lazy": True, "notes": "The most flexible, but takes some effort to implement"},
            {"format": "Feather / IPC", "lazy": True, "notes": None},
            {"format": "Avro", "lazy": False, "notes": None},
            {"format": "Delta", "lazy": True, "notes": "No Lazy writing"},
            {"format": "Iceberg", "lazy": True, "notes": "No Lazy writing"},
        ],
        orient="rows",
    )
    mo.vstack(
        [
            mo.ui.table(df, label="Quick Reference", pagination=False),
            "Também usaremos esta tabela para demonstrar a escrita e leitura para cada formato",
        ]
    )
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Parquet
    Parquet é um formato popular para armazenar dados tabulares baseado na especificação de memória Arrow, é um ótimo padrão e você encontrará muitos conjuntos de dados já o utilizando em sites como HuggingFace
    """)
    return


@app.cell
def _(df, folder, pl):
    df.write_parquet(folder / "data.parquet")  # Eager API - Writing to a file
    _ = pl.read_parquet(folder / "data.parquet")  # Eager API - Reading from a file
    lz = pl.scan_parquet(folder / "data.parquet")  # Lazy API - Reading from a file
    lz.sink_parquet(folder / "data_copy.parquet")  # Lazy API - Writing to a file
    return (lz,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## CSV
    Um formato clássico e comum que tem sido amplamente utilizado por décadas.

    A API é quase idêntica à do Parquet - você pode simplesmente substituir `parquet` por `csv` e funcionará com as configurações padrão, mas o Polars também permite personalizar algumas configurações, como o delimitador e as regras de citação.
    """)
    return


@app.cell
def _(df, folder, lz, pl):
    lz.sink_csv(folder / "data.csv")  # Lazy API - Writing to a file
    df.write_csv(folder / "data_no_head.csv", include_header=False, separator=";")  # Eager API - Writing to a file

    _ = pl.scan_csv(folder / "data.csv")  # Lazy API - Reading from a file
    _ = pl.read_csv(folder / "data_no_head.csv", has_header=False, separator=";")  # Eager API - Reading from a file
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## JSON

    JavaScript Object Notation é um formato de dados comumente usado para armazenar dados não estruturados, e extremamente comum para respostas de API.

    Para grandes conjuntos de dados, você frequentemente verá uma variação em que cada linha no arquivo define um objeto separado, chamado "JSON delimitado por nova linha" (`ndjson`) ou "Linhas JSON" (`jsonl`)

    /// Nota

        É muito mais comum encontrar dados aninhados em JSON do que em outros formatos, mas outros formatos como Parquet também suportam tipos de dados aninhados.

        Polars suporta Listas com comprimento variável, Arrays com comprimento fixo e Structs com campos bem definidos, mas não mapeamentos com chaves arbitrárias.

        Você pode querer transformar os dados desaninhando structs e explodindo listas após carregar de arquivos JSON complexos.
    """)
    return


@app.cell
def _(df, folder, lz, pl):
    # Newline Delimited JSON
    lz.sink_ndjson(folder / "data.ndjson")  # Lazy API - Writing to a file
    df.write_ndjson(folder / "data.ndjson")  # Eager API - Writing to a file

    _ = pl.scan_ndjson(folder / "data.ndjson")  # Lazy API - Reading from a file
    _ = pl.read_ndjson(folder / "data.ndjson")  # Eager API - Reading from a file

    # Normal JSON
    df.write_json(folder / "data.json")  # Eager API - Writing to a file
    _ = pl.read_json(folder / "data.json")  # Eager API - Reading from a file

    # Note that there are no Lazy methods for normal JSON files,
    # either use NDJSON instead or use `lz.collect().write_json()` to collect into memory before writing, and `pl.read_json().lazy()` to read into memory before operating in lazy mode
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Bancos de Dados

    O Polars não suporta nenhum banco de dados _diretamente_, mas utiliza outras bibliotecas como "Engines". A leitura e escrita em bancos de dados usando métodos do Polars não suporta execução "Lazy", mas você pode passar uma consulta SQL para o banco de dados pré-filtrar os dados antes que eles cheguem ao Polars. Consulte o [Guia do Usuário](https://docs.pola.rs/user-guide/io/database) para mais detalhes.

    Você também pode usar outras bibliotecas com [suporte Arrow](#arrow-support) ou [plugins do Polars](#plugin-support) para ler de bancos de dados antes de carregar no Polars, alguns dos quais suportam leitura "Lazy".

    Usando o suporte SQLite de Conectividade de Banco de Dados Arrow como exemplo:
    """)
    return


@app.cell
def _(df, folder, pl):
    URI = "sqlite:///" + f"/{folder.resolve()}/db.sqlite"
    df.write_database(table_name="quick_reference", connection=URI, engine="adbc", if_table_exists="replace")

    query = """SELECT * FROM quick_reference WHERE format LIKE '%Database%'"""

    pl.read_database_uri(query=query, uri=URI, engine="adbc")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Excel

    Do ponto de vista de desempenho, recomendamos usar outros formatos, se possível, como arquivos Parquet ou CSV.

    Similarmente aos bancos de dados, o Polars não o suporta nativamente, mas utiliza outras bibliotecas como "Engines". Consulte o [Guia do Usuário](https://docs.pola.rs/user-guide/io/excel) se precisar usá-lo.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Outros formatos suportados nativamente

    Se você entendeu os exemplos acima, então todos os outros formatos devem parecer familiares - a API é similar para todos os formatos, `read` e `write` para a API Eager ou `scan` e `sink` para a API Lazy.

    Consulte https://docs.pola.rs/api/python/stable/reference/io.html para a lista completa de formatos suportados nativamente pelo Polars
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Suporte Arrow

    Você pode converter dados compatíveis com Arrow de outras bibliotecas, como `pandas`, `duckdb` ou `pyarrow`, para DataFrames do Polars e vice-versa, muitas vezes sem precisar copiar os dados.

    Isso permite que você use outras bibliotecas para carregar dados em formatos não suportados pelo Polars e, em seguida, converta o DataFrame em memória para o Polars.
    """)
    return


@app.cell
def _(df, folder, pd, pl):
    # XML Example using `pandas` read_xml() and to_xml() methods
    df.to_pandas().to_xml(folder / "data.xml")
    pandas_df = pd.read_xml(folder / "data.xml")
    _ = pl.from_pandas(pandas_df)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Suporte a Plugins

    Você também pode escrever [Plugins de I/O](https://docs.pola.rs/user-guide/plugins/io_plugins/) para o Polars a fim de suportar qualquer formato que você precise, ou usar outras bibliotecas que suportam o Polars através de seus próprios plugins, como o DuckDB.
    """)
    return


@app.cell
def _(duckdb, folder):
    # Requires duckdb >= 1.4.0
    conn = duckdb.connect(folder / "db.sqlite")
    conn.sql("SELECT * FROM quick_reference").pl(lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Criando seu próprio Plugin

    A forma mais simples de plugins são essencialmente geradores que produzem DataFrames.

    Sem analisar os filtros, você perderá melhorias de desempenho, mas mesmo assim isso pode ajudar a melhorar seu desempenho em muitos casos, pois permite que o Polars otimize a consulta e solicite dados em lotes, em vez de sempre carregar tudo na memória.

    Abaixo está um exemplo de plugin que apenas pega o produto entre múltiplos iteráveis, alguns destaques são:

    - Você deve usar `register_io_source` para o Polars criar o LazyFrame que consumirá o Gerador
    - Espera-se que você forneça um Schema antes do Gerador iniciar
    - - Para muitos casos de uso, o Plugin pode inferir o Schema, mas você também pode passá-lo explicitamente para a função do plugin
    - Idealmente, você deve analisar alguns dos filtros e seletores de coluna para evitar trabalho desnecessário, mas é possível delegar isso ao Polars após carregar os dados para mantê-lo mais simples (ao custo de eficiência)

    A análise eficiente das expressões de filtro está fora do escopo deste notebook.
    """)
    return


@app.cell
def _(my_custom_input_plugin):
    my_custom_input_plugin(int, range(3), range(5))
    return


@app.cell
def _(my_custom_input_plugin, pl):
    my_custom_input_plugin(bool, [True, False], [True, False]).with_columns(
        (pl.col("A") & pl.col("B")).alias("AND"),
        (pl.col("A") & pl.col("B")).not_().alias("NAND"),
        (pl.col("A") | pl.col("B")).alias("OR"),
        (pl.col("A") ^ pl.col("B")).alias("XOR"),
    ).collect()
    return


@app.cell
def _(Iterator, get_positional_names, itertools, pl, register_io_source):
    def my_custom_input_plugin(dtype, *iterables) -> pl.LazyFrame:
        schema = pl.Schema({key: dtype for key in get_positional_names(len(iterables))})

        def source_generator(
            with_columns: list[str] | None,
            predicate: pl.Expr | None,
            n_rows: int | None,
            batch_size: int | None,
        ) -> Iterator[pl.DataFrame]:
            """
            Generator function that creates the source.
            This function will be registered as IO source.
            """
            if batch_size is None:
                batch_size = 100
            if n_rows is not None:
                batch_size = min(batch_size, n_rows)

            generator = itertools.product(*iterables)
            while n_rows is None or n_rows > 0:
                rows = []
                try:
                    while len(rows) < batch_size:
                        rows.append(next(generator))
                except StopIteration:
                    n_rows = -1

                df = pl.from_records(rows, schema=schema, orient="row")
                if n_rows is not None:
                    n_rows -= df.height
                    batch_size = min(batch_size, n_rows)

                # If we would make a performant reader, we would not read these
                # columns at all.
                if with_columns is not None:
                    df = df.select(with_columns)

                # If the source supports predicate pushdown, the expression can be parsed
                # to skip rows/groups.
                if predicate is not None:
                    df = df.filter(predicate)

                yield df

        return register_io_source(io_source=source_generator, schema=schema)
    return (my_custom_input_plugin,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### DuckDB

    Como demonstrado acima, além do suporte de interoperabilidade Arrow, o [DuckDB](https://duckdb.org/) também adicionou suporte para carregar resultados de consulta em um DataFrame ou LazyFrame do Polars via um plugin do Polars.

    Você pode ler mais sobre as integrações entre Polars e DuckDB em

    - https://docs.pola.rs/user-guide/ecosystem/#duckdb
    - https://duckdb.org/docs/stable/guides/python/polars.html

    Você pode aprender mais sobre o DuckDB no curso marimo sobre ele, incluindo recursos relacionados a SQL do Marimo
    """)
    return


@app.cell
def _():
    # Amazing if you need of features not yet supported by Polars such as geospatial data
    duckdb_query = """
        SELECT 
            id,
            name,
            ST_X(geometry) as longitude,
            ST_Y(geometry) as latitude
        FROM locations
    """
    return (duckdb_query,)


@app.cell
def _(duckdb_conn, duckdb_query):
    # Eager (default):
    duckdb_conn.sql(duckdb_query).pl()
    return


@app.cell
def _(duckdb_conn, duckdb_query):
    # Lazy (requires >= 1.4.0):
    duckdb_conn.sql(duckdb_query).pl(lazy=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Partições Hive

    Também há suporte para dados particionados [Hive](https://docs.pola.rs/user-guide/io/hive/), mas partes da API ainda são instáveis (podem mudar em futuras versões do Polars).

    Mesmo sem usar partições, muitos métodos também suportam padrões glob para ler vários arquivos na mesma pasta, como `scan_csv(folder / "*.csv")`
    """)
    return


@app.cell
def _(df, folder, pl):
    df.write_parquet(str((folder / "hive").resolve()) + "/", partition_by=["lazy"])
    _ = pl.scan_parquet(str((folder / "hive").resolve()) + "/").filter(pl.col("lazy").eq(True)).collect()

    print(*(folder / "hive").rglob("*.parquet"), sep="\n")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Lendo da Nuvem

    O Polars também suporta a leitura de conjuntos de dados públicos e privados de vários sites e soluções de armazenamento em nuvem.

    Se você precisar (re)utilizar o mesmo arquivo muitas vezes na mesma máquina, pode ser interessante fazer o download manual e carregar do seu sistema de arquivos local para evitar o download repetido, ou baixar e gravar em disco apenas se o arquivo não existir.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Sites arbitrários

    Você pode carregar arquivos de quase qualquer site usando apenas uma URL HTTPS, desde que não esteja bloqueado por autorização.
    """)
    return


@app.cell(disabled=True)
def _():
    # df = pl.read_csv('https://example.com/file.csv')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conjuntos de Dados Hugging Face e Kaggle

    Procure por "polars" dentro de menus suspensos como "Use this dataset" no Hugging Face ou "Code" no Kaggle, e muitas vezes você obterá um trecho para carregar os dados diretamente em um dataframe que você pode usar.

    Leia mais: [Hugging Face](https://docs.pola.rs/user-guide/io/hugging-face/), [Kaggle](https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpolars)
    """)
    return


@app.cell(disabled=True)
def _():
    # df = pl.read_parquet('hf://datasets/username/dataset/*.parquet')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Armazenamento em Nuvem - AWS S3, Azure Blob Storage, Google Cloud Storage

    A API é a mesma para todos os três provedores de armazenamento; consulte o [Guia do Usuário](https://docs.pola.rs/user-guide/io/cloud-storage/) se precisar de algum deles.

    Exemplos executáveis não estão incluídos neste Notebook, pois exigiriam a configuração de autenticação, mas a célula desabilitada abaixo mostra um exemplo usando o Azure.
    """)
    return


@app.cell(disabled=True)
def _(adlfs, df, os, pl):
    fs = adlfs.AzureBlobFileSystem(connection_string=os.environ["AZURE_STORAGE_CONNECTION_STRING"])
    destination = f"abfs://{os.environ['AZURE_CONTAINER_NAME']}/file.parquet"

    # Writing
    with fs.open(destination, mode="wb") as f:
        df.write_parquet(f)

    # Reading
    pl.read_parquet(
        destination, storage_options={"account_name": os.environ["AZURE_STORAGE_ACCOUNT"], "use_azure_cli": "True"}
    )

    # Deleting
    fs.delete(destination)

    # If you get an error saying that the account does not exists, double check you logged in the correct account and subscription via `az login`
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Multiplexação

    Você também pode dividir uma consulta em vários "sinks" via [multiplexação](https://docs.pola.rs/user-guide/lazy/multiplexing/), para evitar ler várias vezes, repetir as mesmas operações para cada "sink" ou coletar resultados intermediários na memória.
    """)
    return


@app.cell
def _(folder, lz, pl):
    lz2 = lz.with_columns(pl.col(pl.String).str.to_uppercase())
    lz3 = lz.with_columns(pl.col(pl.String).str.to_lowercase())

    # Collecting multiple LazyFrames into memory
    _df, _df2, _df3 = pl.collect_all([lz, lz2, lz3])

    # Sinking multiple LazyFrames into different destinations
    sinks = [
        lz.sink_csv(folder / "data_1.csv", lazy=True),
        lz2.sink_csv(folder / "data_2.csv", lazy=True),
        lz3.sink_csv(folder / "data_3.csv", lazy=True),
    ]
    _ = pl.collect_all(sinks)
    return (sinks,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Execução Assíncrona

    O Polars também possui suporte experimental para executar consultas "lazy" em modo `async`, permitindo que você `await` operações dentro de funções assíncronas.
    """)
    return


@app.cell
async def _(lz):
    await lz.collect_async()
    return


@app.cell
async def _(folder, lz, pl, sinks):
    # If you want to write to a file, use `lz.sink_format(lazy=True)` followed by `...collect_async()` or `pl.collect_all_async(...)`
    _ = await lz.sink_csv(folder / "data_from_async.csv", lazy=True).collect_async()
    _ = await pl.collect_all_async(sinks)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusão
    Como você viu, o Polars facilita o trabalho com uma variedade de formatos e diferentes fontes de dados.

    Desde formatos nativamente suportados, como arquivos Parquet e CSV, até o uso de outras bibliotecas como intermediárias para dados XML ou geoespaciais, e plugins para formatos emergentes ou proprietários, contanto que seus dados possam caber em uma tabela, é provável que você possa transformá-los em um DataFrame do Polars.

    Combinado com o carregamento direto de fontes remotas, incluindo plataformas de dados públicas como Hugging Face e Kaggle, bem como dados privados em sua nuvem, você pode importar conjuntos de dados para quase tudo que possa imaginar.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Utilitários
    Importações, funções utilitárias e afins usadas ao longo do Notebook
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(disabled=True)
def _():
    # You may need to install `fsspec ` and `adlfs ` beyond the dependencies included in the notebook
    import os
    import adlfs
    return adlfs, os


@app.cell
def _():
    import pathlib
    import tempfile

    folder = pathlib.Path(tempfile.mkdtemp())
    folder
    return (folder,)


@app.cell
def _():
    import math
    import string
    import itertools
    from typing import Iterator
    return Iterator, itertools, string


@app.cell
def _():
    import polars as pl
    import pandas as pd
    from polars.io.plugins import register_io_source
    import duckdb
    return duckdb, pd, pl, register_io_source


@app.cell
def _(itertools, string):
    def get_positional_names(count: int) -> list[str]:
        out = []
        size = 0
        while True:
            size += 1  # number of characters in each column name
            for column in itertools.product(*itertools.repeat(string.ascii_uppercase, size)):
                if len(out) >= count:
                    return out
                out.append("".join(column))
    return (get_positional_names,)


@app.cell
def _(duckdb):
    # Connect to an ephemeral in-memory DuckDB database
    duckdb_conn = duckdb.connect(":memory:")

    # Install and load the spatial extension for geometry support
    duckdb_conn.install_extension("spatial")
    duckdb_conn.load_extension("spatial")

    # Create a table with geometry column
    duckdb_conn.sql("""
        CREATE TABLE locations (
            id INTEGER,
            name VARCHAR,
            geometry GEOMETRY
        )
    """)

    # Insert some sample data with geometry points
    duckdb_conn.sql("""
        INSERT INTO locations VALUES
        (1, 'New York', ST_Point(-74.0059, 40.7128)),
        (2, 'Los Angeles', ST_Point(-118.2437, 34.0522)),
        (3, 'Chicago', ST_Point(-87.6298, 41.8781)),
        (4, 'Houston', ST_Point(-95.3698, 29.7604)),
        (5, 'Phoenix', ST_Point(-112.0740, 33.4484))
    """)
    return (duckdb_conn,)


if __name__ == "__main__":
    app.run()
