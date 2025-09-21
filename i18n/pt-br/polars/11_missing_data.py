# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "plotly[express]==6.3.0",
#     "polars==1.33.1",
# ]
# ///

import marimo

__generated_with = "0.16.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Lidando com Dados Faltantes

    _original por [etrotta](https://github.com/etrotta) e [Felix Najera](https://github.com/folicks)_

    _traduzido por [etrotta](https://github.com/etrotta) e [gemini](https://github.com/google-gemini/gemini-cli)_

    Este notebook aborda problemas comuns ao lidar com dados do mundo real e as técnicas para resolvê-los, apresentando as funcionalidades do Polars para tratar de dados ausentes.

    Primeiro, fornecemos uma visão geral dos métodos do Polars. Em seguida, um exemplo prático demonstra seu uso. Por fim, a seção 'Conteúdo Bônus' traz informações adicionais.
    Você pode navegar para pular para cada cabeçalho usando o menu à direita.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Métodos para trabalhar com valores nulos

    Usaremos o seguinte DataFrame para mostrar os métodos mais importantes:
    """
    )
    return


@app.cell(hide_code=True)
def _(pl):
    df = pl.DataFrame(
        [
            {"animal": "Cão", "nome": "Millie", "altura": None, "idade": 4},
            {"animal": "Cão", "nome": "Wally", "altura": 60, "idade": None},
            {"animal": "Cão", "nome": None, "altura": 50, "idade": 12},
            {"animal": "Gato", "nome": "Mini", "altura": 15, "idade": None},
            {"animal": "Gato", "nome": None, "altura": 25, "idade": 6},
            {"animal": "Gato", "nome": "Kazusa", "altura": None, "idade": 16},
        ]
    )
    df
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Contando nulos

    Uma agregação simples, porém conveniente
    """
    )
    return


@app.cell
def _(df):
    df.null_count()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Removendo Nulos

    A maneira mais simples de lidar com valores nulos é descartá-los, mas nem sempre é uma boa ideia.
    """
    )
    return


@app.cell
def _(df):
    df.drop_nulls()
    return


@app.cell
def _(df):
    df.drop_nulls(subset="nome")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Filtrando valores nulos

    Para filtrar no Polars, você normalmente usará os métodos `df.filter(expression)` ou `df.remove(expression)`.

    Usando `filter` ele manterá apenas as linhas em que a expressão for avaliada como Verdadeira.
    Ele removerá não somente as linhas em que for avaliada como Falsa, mas também aquelas em que a expressão for avaliada como Nula.

    Usando `remove` ele removerá apenas as linhas em que a expressão for avaliada como Verdadeira.
    Manterá as linhas em que for avaliada como Nula.
    """
    )
    return


@app.cell
def _(df, pl):
    df.filter(pl.col("idade") > 10)
    return


@app.cell
def _(df, pl):
    df.remove(pl.col("idade") < 10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Também é comum pensar em usar `== None` ou `!= None`, porém os operadores no Polars geralmente propagam valores nulos, logo o resultado se torna nulo para todas as linhas.

    Você pode usar os métodos `.eq_missing()` no lugar de `==`, ou `.ne_missing()` no lugar de `!=`, para que essa operação sempre compare ao invés de propagar, mas também existem os métodos `.is_null()` e `.is_not_null()` que você pode usar no lugar da comparação.
    """
    )
    return


@app.cell
def _(df, pl):
    df.select(
        "nome",
        (pl.col("nome") == None).alias("Nome equals None"),
        (pl.col("nome") == "Mini").alias("Nome equals Mini"),
        (pl.col("nome").eq_missing("Mini")).alias("Nome eq_missing Mini"),
        (pl.col("nome").is_null()).alias("Nome is null"),
        (pl.col("nome").is_not_null()).alias("Nome is not null"),
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Preenchendo valores nulos

    Você pode os preencher com constantes, valores cálculados ou consultando fontes de dados externas.

    Tenha cuidado para não tratar valores estimados como se fossem reais e precisos, caso contrário, você pode acabar tirando conclusões falsas.

    Como exercício, vamos criar alguns valores cálculados para preencher os nulos e, em seguida, tente dar nomes aos animais com `null` editando as células manualmente.
    """
    )
    return


@app.cell
def _(df, mo, pl):
    guesstimates = df.with_columns(
        pl.col("altura").fill_null(pl.col("altura").mean().over("animal")),
        pl.col("idade").fill_null(0),
    )
    guesstimates = mo.ui.data_editor(
        guesstimates,
        editable_columns=["nome"],
    )
    guesstimates
    return (guesstimates,)


@app.cell
def _(guesstimates):
    guesstimates.value
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### TL;DR

    Antes de partirmos pro exemplo prático, uma breve revisão do que cobrimos:

    - use `df.null_counts()` ou `expr.is_null()` para contar e identificar valores ausentes
    - você poderia simplesmente remover linhas com valores ausentes em qualquer coluna, ou em um subconjunto delas por meio de `df.drop_nulls()`, mas na maioria dos casos você vai querer dar mais atenção a essas linhas do que só as eliminar
    - leve em consideração se deseja preservar valores nulos ou removê-los ao escolher entre `df.filter()` ou `df.remove()`
    - se você não quiser propagar valores nulos, use variações `_missing` de métodos como `eq` vs `eq_missing`
    - você pode querer preencher valores ausentes com base em cálculos via `fill_null`, combinar com outros conjuntos de dados, ou editar manualmente os dados com base em documentos externos

    Você também pode consultar o [Guia do Usuário](https://docs.pola.rs/user-guide/expressions/missing-data/) do Polars para mais informações.

    Qualquer que seja a abordagem que você adotar, lembre-se de documentar ela!
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Exemplo Prático

    Usaremos um conjunto de dados do `alertario` sobre o clima no Rio de Janeiro, originalmente disponível no Google Big Query em `datario.clima_pluviometro`. O que você precisa saber sobre ele:

    - Contém várias estações que cobrem o Município do Rio de Janeiro
    - Mede a precipitação em milímetros, com uma granularidade de 15 minutos
    - Filtramos para incluir apenas dados sobre 2020, 2021 e 2022
    """
    )
    return


@app.cell
def _(estacoes, px):
    px.scatter_map(estacoes, lat="latitude", lon="longitude", text="estacao")
    return


@app.cell(disabled=True, hide_code=True)
def _(estacoes, pl, px):
    # Caso `scatter_map` não funcione para você:
    _fig = px.scatter_geo(estacoes, lat="latitude", lon="longitude", hover_name="estacao")

    _min_lat = estacoes.select(pl.col("latitude").min()).item()
    _max_lat = estacoes.select(pl.col("latitude").max()).item()
    _min_lon = estacoes.select(pl.col("longitude").min()).item()
    _max_lon = estacoes.select(pl.col("longitude").max()).item()

    _fig.update_geos(
        lataxis_range=[_min_lat - 0.2, _max_lat + 0.2],
        lonaxis_range=[_min_lon - 0.2, _max_lon + 0.2],
        resolution=50,
        showocean=True,
        oceancolor="Lightblue",
    )
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Estações

    Primeiro, vamos dar uma olhada em algumas das estações. Observe como

    - Algumas estações foram desativadas, então não haverá dados sobre elas (nesse caso, nem sabemos suas coordenadas)
    - Existem algumas colunas que nem sequer contêm dados!

    Removeremos as colunas vazias e as linhas sem coordenadas
    """
    )
    return


@app.cell(hide_code=True)
def _(estacoes_sujo, mo, pl):
    # Se você estivesse trabalhando nisso sozinho, talvez quisesse dar uma olhada em *todas* elas, mas para fins práticos, estou pegando uma fatia para a saída exibida, pois de outra forma ocuparia muito espaço na tela.
    # mo.ui.table(estacoes_sujo, pagination=False)

    mo.vstack(
        [
            mo.md("Antes (amostra do início e do fim):"),
            pl.concat([estacoes_sujo.head(3), estacoes_sujo.tail(3)], how="vertical"),
        ]
    )
    return


@app.cell
def _(estacoes_sujo, mo, pl):
    estacoes = estacoes_sujo.drop_nulls(subset=("latitude", "longitude")).drop(pl.col(r"^data_(inicio|fim)_operacao$"))
    mo.vstack([mo.md("Depois (dataframe completo):"), estacoes])
    return (estacoes,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Precipitação
    Agora, vamos passar para os dados de Precipitação.

    ## Parte 1 - Valores Nulos

    Primeiro de tudo, vamos verificar se há valores nulos:
    """
    )
    return


@app.cell
def _(clima_sujo, pl):
    rain = pl.col("acumulado_chuva_15_min")  # Criando um alias porque vamos usar muito essa coluna

    clima_sujo.filter(rain.is_null())
    return (rain,)


@app.cell(hide_code=True)
def _(clima_sujo, mo, rain):
    _missing_count = clima_sujo.select(rain.is_null().sum()).item()

    #

    mo.md(
        f"Como você pode ver, há {_missing_count:,} linhas sem a chuva acumulada por um período.\n\nIsso pode ser causado por mau funcionamento do sensor, manutenção, corrupção de dados ou inúmeras outras razões. Embora seja uma pequena porcentagem dos dados ({_missing_count / len(clima_sujo):.3%}), é importante tratar essas linhas de alguma forma."
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Primeira opção para tratarlas: Descartar dados.

    Poderíamos simplesmente remover essas linhas como fizemos para as estações, o que pode ser uma solução aceitável para alguns problemas, mas nem sempre é a melhor ideia.
    ```py
    clima_sujo.drop_nulls()
    ```

    ### Segunda opção para tratarlas: Interpolação

    Em vez de remover essas linhas, podemos usar algumas heurísticas para adivinhar valores que façam sentido para elas. Lembre-se de que isso adiciona um grau de incerteza aos resultados finais, então você deve divulgar como está tratando os valores ausentes se tirar alguma conclusão com base em tais suposições.
    ```py
    clima_sujo.with_columns(rain.fill_null(strategy="forward")),
    ```

    Ao preencher com valores cálculados, quais estratégias que podem fazer sentido para os seus dados variam de caso a caso. Em alguns casos, você vai querer usar a média para mantê-la centrada em torno da mesma distribuição, enquanto em outros casos você vai querer zerá-la para evitar modificar o total, ou preencher para frente/trás para manter a continuidade da série.

    ### Última opção para tratarlas: Adquirir os valores corretos de outro lugar.

    Similarmente a como adicionamos manualmente nomes aos animais na introdução, você poderia tentar encontrar valores aproximados de outro conjunto de dados ou, em alguns casos, inserir manualmente os valores corretos.

    ### No entanto

    Vamos investigar um pouco mais antes de decidir seguir com qualquer uma das abordagens.
    Por exemplo, vamos conferir se nossos dados atuais estão completos ou se faltam algumas linhas além daquelas presentes com valores nulos.
    """
    )
    return


@app.cell
def _(clima_sujo, pl):
    seen_counts = clima_sujo.group_by(pl.col("datetime").dt.time().alias("hora"), "id_estacao").len()

    # Curiosidade: uma única linha tem seu tempo definido como `23:55`.
    # Ela não deveria estar presente neste conjunto de dados, mas de alguma forma entrou na tabela oficial do Google Big Query.
    seen_counts = seen_counts.filter(pl.col("len") > 1)
    # Você pode querer tratá-lo como um bug ou outlier e removê-lo do clima_sujo, mas não vamos nos aprofundar na limpeza disso neste notebook

    # seen_counts.sort("id_estacao", "hora").select("id_estacao", "hora", "len")
    seen_counts.sort("len").select("id_estacao", "hora", "len")
    return


@app.cell
def _(pl):
    expected_range = pl.datetime_range(
        pl.lit("2020-01-01T00:00:00").str.to_datetime(time_zone="America/Sao_Paulo"),
        pl.lit("2022-12-31T23:45:00").str.to_datetime(time_zone="America/Sao_Paulo"),
        "15m",
    )

    pl.select(expected_range.alias("hora")).group_by(pl.col.hora.dt.time()).len().sort("hora")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Parte 2 - Linhas Faltantes

    Podemos ver que esperávamos que houvesse 1096 linhas para cada hora para cada estação (do início de 2020 ao final de 2022), mas na realidade vemos entre 1077 e 1096 linhas.

    Essa diferença pode ser causada pelos mesmos fatores dos valores nulos, ou até mesmo por alguém descartar valores nulos ao longo do caminho, mas para os propósitos deste notebook, digamos que queremos ter valores para cada momento para cada estação, então teremos que usar os dados existentes para estimar os valores faltantes.

    ### Upsampling

    Dado que estamos trabalhando com dados de séries temporais, faremos o [upsample](https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.upsample.html) dos dados, mas você também poderia criar um DataFrame contendo todas as linhas esperadas e usar `join(how="...")`

    No entanto, isso nos dará _ainda mais_ valores nulos, então vamos querer preenchê-los depois. Para este caso, usaremos apenas um preenchimento para frente `fill_null(strategy="forward")`, seguido por um preenchimento para trás para caso tenham linhas sem ningúem atrás.
    """
    )
    return


@app.cell
def _(clima_sujo, mo, pl, rain):
    _hollow_weather = clima_sujo.sort("id_estacao", "datetime").upsample("datetime", every="15m", group_by="id_estacao")
    clima = _hollow_weather.fill_null(strategy="forward").fill_null(strategy="backward")

    mo.vstack(
        [
            mo.ui.table(
                label="Contagem de nulos em cada etapa",
                data=pl.concat(
                    [
                        clima_sujo.null_count().select(
                            pl.lit("Antes do upsampling").alias("label"), rain, "id_estacao", "datetime"
                        ),
                        _hollow_weather.null_count().select(
                            pl.lit("Depois do upsampling").alias("label"), rain, "id_estacao", "datetime"
                        ),
                        clima.null_count().select(
                            pl.lit("Depois de preencher").alias("label"), rain, "id_estacao", "datetime"
                        ),
                    ]
                ),
            ),
            mo.md("Dados após upsampling e preenchimento de nulos:"),
            clima,
        ]
    )
    return (clima,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Agora que finalmente temos um conjunto de dados limpo, vamos brincar um pouco com ele.

    ### Aplicativo de Exemplo

    Vamos exibir a quantidade de precipitação que cada estação mediu dentro de um período de tempo, agregada a uma granularidade menor.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    filters = (
        mo.md(
            """Filtros para o exemplo

        Ano: {year}
        Dias do ano: {day}
        Horas de cada dia: {hour}
        Granularidade da agregação: {interval}
        """
        )
        .batch(
            year=mo.ui.dropdown([2020, 2021, 2022], value=2022),
            day=mo.ui.range_slider(1, 365, show_value=True, full_width=True, value=[87, 94]),
            hour=mo.ui.range_slider(0, 24, 0.25, show_value=True, full_width=True),
            interval=mo.ui.dropdown(["15m", "30m", "1h", "2h", "4h", "6h", "1d", "7d", "30d"], value="4h"),
        )
        .form(submit_button_label="Rodar")
    )

    # Nota: Você poderia usar `mo.ui.date_range` em vez disso, mas eu pessoalmente não gosto dele
    # mo.ui.date_range(start="2020-01-01", stop="2022-12-31", value=["2022-03-28", "2022-04-03"], label="Intervalo de exibição")

    filters
    return (filters,)


@app.cell
def _(clima, estacoes, filters, mo, pl, rain):
    mo.stop(filters.value is None)

    _range_seconds = map(lambda hour: hour * 3600, filters.value["hour"])
    _df_seconds = pl.col("datetime").dt.hour().cast(pl.Float64()).mul(3600) + pl.col("datetime").dt.minute().cast(
        pl.Float64()
    ).mul(60)

    animation_data = (
        clima.lazy()
        .filter(
            pl.col("datetime").dt.year() == filters.value["year"],
            pl.col("datetime").dt.ordinal_day().is_between(*filters.value["day"]),
            _df_seconds.is_between(*_range_seconds),
        )
        .group_by_dynamic("datetime", group_by="id_estacao", every=filters.value["interval"])
        .agg(rain.sum().alias("precipitation"))
        .remove(pl.col("precipitation").eq(0).all().over("id_estacao"))
        .join(estacoes.lazy(), on="id_estacao")
        .select("estacao", "latitude", "longitude", "precipitation", "datetime")
        .collect()
    )
    return (animation_data,)


@app.cell
def _(animation_data, pl, px):
    _fig = px.scatter_geo(
        animation_data.with_columns(avg_precipitation=pl.col("precipitation").mean().over("estacao")),
        lat="latitude",
        lon="longitude",
        hover_name="estacao",
        animation_group="estacao",
        animation_frame="datetime",
        size="avg_precipitation",
        color="precipitation",
        color_continuous_scale="PuBu",
        range_color=[0, animation_data.select(pl.col("precipitation").max()).item()],
    )

    _min_lat = animation_data.select(pl.col("latitude").min()).item()
    _max_lat = animation_data.select(pl.col("latitude").max()).item()
    _min_lon = animation_data.select(pl.col("longitude").min()).item()
    _max_lon = animation_data.select(pl.col("longitude").max()).item()

    _fig.update_geos(
        lataxis_range=[_min_lat - 0.2, _max_lat + 0.2],
        lonaxis_range=[_min_lon - 0.2, _max_lon + 0.2],
        resolution=50,
        showocean=True,
        oceancolor="Lightblue",
    )
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Se estivéssemos com algumas linhas faltando, teríamos círculos aparecendo e desaparecendo em vez de uma animação continua!

    Em muitos cenários, dados ausentes também podem levar a resultados errados, por exemplo, se estimarmos a quantidade total de chuva durante o período observado:
    """
    )
    return


@app.cell
def _(clima, clima_sujo, mo, rain):
    old_estimate = clima_sujo.select(rain.sum()).item()
    new_estimate = clima.select(rain.sum()).item()
    # Nota: A agregação usada para calcular essas variáveis (somar todas as estações) não é muito significativa, mas a diferença relativa entre elas se aplica a muitas agregações potencialmente úteis

    mo.md(f"Nossas estimativas podem mudar em aproximadamente {(new_estimate - old_estimate) / old_estimate:.2%}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    O que ainda é uma diferença relativamente pequena, mas cada gota conta quando se trata do clima.

    Para conjuntos de dados com uma parcela maior de valores ausentes, essa diferença pode ser muito maior.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Conteúdo Bônus

    ## Apêndice A: Fusos Horários Ausentes

    O conjunto de dados original continha datetimes sem informação de fuso horário (naive), em vez de datetimes com fuso horário definido (aware), mas podemos inferir se dizem respeito ao tempo UTC ou ao tempo local (neste caso, -03:00 UTC) com base nas medições.

    Por exemplo, podemos selecionar um intervalo específico em que sabemos que choveu muito, ou traçar um gráfico da precipitação média para cada hora do dia e, em seguida, comparar as datas e horas dos nossos dados com uma fonte de referência externa.
    """
    )
    return


@app.cell(hide_code=True)
def _(clima_sujo_sem_fuso, mo):
    mo.vstack(
        [
            mo.md("Exemplo de dados originais:"),
            clima_sujo_sem_fuso.head(3),
        ]
    )
    return


@app.cell
def _(clima_sujo_sem_fuso, pl, px, rain):
    naive_downfall_per_hour = (
        clima_sujo_sem_fuso.group_by(pl.col("datetime").dt.hour().alias("hour"))
        .agg(rain.sum().alias("accumulated_rain"))
        .with_columns(pl.col("accumulated_rain").truediv(pl.col("accumulated_rain").sum()).mul(100))
    )
    px.bar(
        naive_downfall_per_hour.sort("hour"),
        x="hour",
        y="accumulated_rain",
        title="Distribuição da precipitação por hora (%), usando o datetime ingênuo",
    )
    return


@app.cell
def _(clima_sujo_sem_fuso, estacoes, pl, rain):
    naive_top_rain_events = (
        clima_sujo_sem_fuso.lazy()
        # Se você quisesse filtrar as datas e localizar um evento específico:
        # .filter(pl.col("datetime").is_between(pl.lit("2022-03-01").str.to_datetime(), pl.lit("2022-05-01").str.to_datetime()))
        .sort("id_estacao", "datetime")
        .group_by_dynamic("datetime", every="1h", offset="30m", group_by="id_estacao")
        .agg(rain.sum())
        .join(estacoes.lazy(), on="id_estacao")
        .sort(rain, descending=True)
        .select(
            "estacao",
            pl.col("datetime").alias("inicio_da_janela"),
            (pl.col("datetime") + pl.duration(hours=1)).alias("fim_da_janela"),
            rain.alias("precipitação acumulada"),
        )
        .head(50)
        .collect()
    )
    naive_top_rain_events
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Pesquisando externamente a distribuição esperada e procurando alguns dos periodos de chuva extrema, podemos chegar a uma conclusão sobre se ela está alinhada com a hora local ou com o UTC.

    Neste caso, a distribuição corresponde ao clima normal para esta região e podemos ver que as horas com mais precipitação correspondem às de eventos históricos, então é seguro dizer que está usando a hora local (equivalente ao fuso horário `Americas/São_Paulo`).
    """
    )
    return


@app.cell
def _(clima_sujo_sem_fuso, pl):
    clima_sujo = clima_sujo_sem_fuso.with_columns(pl.col("datetime").dt.replace_time_zone("America/Sao_Paulo"))

    clima_sujo.head(3)
    return (clima_sujo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Apêndice B: 'Not a Number' (NaN)

    Enquanto algumas outras ferramentas sem suporte adequado para valores ausentes podem usar `NaN` para indicar que um valor está ausente, no Polars ele é tratado exclusivamente como uma _float_, da mesma forma que `0.0`, `1.0` ou `inf` (infinito) são _floats_.

    Você pode usar `.fill_null(float('nan'))` se precisar converter floats para um formato que tais ferramentas aceitem, ou usar `.fill_nan(None)` se estiver importando dados delas, assumindo que não há valores que realmente deveriam ser o float NaN.

    Lembre-se de que certas operações podem resultar em NaN, por exemplo, dividir por zero:
    """
    )
    return


@app.cell
def _(clima_sujo, pl, rain):
    day_perc = clima_sujo.select(
        "datetime",
        (rain / rain.sum().over("id_estacao", pl.col("datetime").dt.date())).alias("percentage_of_day_precipitation"),
    )
    perc_col = pl.col("percentage_of_day_precipitation")

    day_perc
    return day_perc, perc_col


@app.cell(hide_code=True)
def _(day_perc, mo, perc_col):
    mo.md(
        f"""
    É nulo para {day_perc.select(perc_col.is_null().mean()).item():.4%} das linhas, mas é NaN para {day_perc.select(perc_col.is_nan().mean()).item():.4%} delas.
    Se usarmos o dataframe limpo para calculá-lo em vez do original não teremos nulos, mas observe como para este cálculo podemos acabar com tanto `null`s como `NaN` no mesmo dataframe, com um significado diferente para cada.

    Neste caso, faz sentido preencher NaNs como 0 para indicar que não houve chuva durante esse período, mas tratar os nulos da mesma forma poderia levar a uma interpretação diferente dos dados, então lembre-se de lidar com NaNs e nulos separadamente.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Apêndice C: Todo o resto

    Por mais longo que seja este Notebook, ele não pode razoavelmente cobrir ***tudo*** o que pode tem de lidar com dados ausentes, pois isso é literalmente tudo que tem de lidar com dados.

    Esta seção aborda muito brevemente alguns outros recursos importantes não mencionados acima
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Valores ausentes em Agregações

    Muitos métodos de agregação descartam valores ausentes, enquanto outros os levam em consideração.

    Sempre verifique a documentação do método que você está usando, muitas das vezes docstrings explicarão seu comportamento.
    """
    )
    return


@app.cell
def _(df, pl):
    df.group_by("animal").agg(
        pl.col("altura").len().alias("len"),
        pl.col("altura").count().alias("count"),
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Valores nulos em Joins

    Por padrão, valores nulos nunca produzirão correspondências usando [join](https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.join.html), mas você pode especificar `nulls_equal=True` para juntar valores nulos uns com os outros.
    """
    )
    return


@app.cell(hide_code=True)
def _(pl):
    age_groups = pl.DataFrame(
        [
            {"idade": None, "fase": "Desconheçido"},
            {"idade": [0, 1], "fase": "Bebe"},
            {"idade": [2, 3, 4, 5, 6, 7, 8, 9, 10], "fase": "Adulto"},
            {"idade": [11, 12, 13, 14], "fase": "Sênior"},
            {"idade": [15, 16, 17, 18, 19, 20], "fase": "Geriátrico"},
        ]
    )
    age_groups
    return (age_groups,)


@app.cell
def _(age_groups, df):
    df.join(age_groups.explode("idade"), on="idade")
    return


@app.cell
def _(age_groups, df):
    df.join(age_groups.explode("idade"), on="idade", nulls_equal=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Utilitários

    Carregando dados e importações
    """
    )
    return


@app.cell
def _(pl):
    estacoes_bruto = pl.scan_csv("hf://datasets/etrotta/weather-alertario/datario_alertario_stations.csv")
    clima_bruto = pl.scan_csv("hf://datasets/etrotta/weather-alertario/datario_alertario_weather_2020_to_2022.csv")
    return clima_bruto, estacoes_bruto


@app.cell
def _(estacoes_bruto):
    estacoes_sujo = estacoes_bruto.select(
        "id_estacao",
        "estacao",
        "latitude",
        "longitude",
        "cota",
        "situacao",
        "endereco",
        "data_inicio_operacao",
        "data_fim_operacao",
    ).collect()
    return (estacoes_sujo,)


@app.cell
def _(clima_bruto, pl):
    clima_sujo_sem_fuso = clima_bruto.select(
        pl.col("id_estacao").alias("id_estacao"),
        pl.col("acumulado_chuva_15_min").alias("acumulado_chuva_15_min"),
        pl.concat_str("data_particao", pl.lit("T"), "horario").str.to_datetime(time_zone=None).alias("datetime"),
    ).collect()
    return (clima_sujo_sem_fuso,)


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
    import plotly.express as px
    return (px,)


if __name__ == "__main__":
    app.run()
