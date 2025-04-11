from collections.abc import Container
from tkinter import Text
from tkinter.constants import CENTER
import flet as ft
from flet import AppBar, ElevatedButton, Text, Colors, View, Page, Container, Column
from flet.core.dropdown import Option
from datetime import datetime
from dateutil.relativedelta import relativedelta



def main(page: Page):
    # Configuração da página
    page.title = 'Minha aplicação Flet'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667


    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Regras"),
            ft.NavigationBarDestination(icon=ft.Icons.REPORT, label="Simulação"),
            ft.NavigationBarDestination(
                icon=ft.Icons.ACCOUNT_BOX,
                selected_icon=ft.Icons.BOOKMARK,
                label="Explore",

            ),
        ]
    )

    pagelet = ft.Pagelet(
        navigation_bar=ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Inicio",  ),
                ft.NavigationBarDestination(icon=ft.Icons.REPORT, label="Regras"),
                ft.NavigationBarDestination(
                    icon=ft.Icons.ACCOUNT_BOX,
                    selected_icon=ft.Icons.ACCOUNT_BOX,
                    label="Simulação",


                ),
            ],
            on_change=lambda e: page.go(["/", "/segunda_tela_regras" ,"/primeira_tela_aposentadoria", "/terceira_tela_aposentadoria_resultado" ][e.control.selected_index])
        ), content=ft.Container(),
        height=500, expand=True, )

    # def voltar(e):
    #     page.views.pop()
    #     top_view = page.views[-1]
    #     page.go(top_view.route)

    def calcular_aposentadoria(e):
        # if media_salarial.error = "" :
        #     media_salarial.error_text = "Preencha o campo corretamente"
        #
        # else:
        #     media_salarial.error = False
        #     media_salarial.error_text = ""

        if not all([input_idade.value, menu_genero.value, tempo_contribuicao.value, media_salarial.value, categoria_aposentadoria.value]):
            text_resultad_erro.value = "Por favor, preencha todos os campos."
            page.update()
            return
        try:
            valor_contri = int(tempo_contribuicao.value)
            salario = float(media_salarial.value)

            if menu_genero.value == 'masculino':
                if categoria_aposentadoria.value == 'idade':
                    if int(tempo_contribuicao.value) >= 15 and int(input_idade.value) >= 65:
                        text_resultad.value = 'Você poderá se aposentar devido à sua alta idade.'
                        text_resultad_salario.value = f'Seu salário será de {conta_salario():.3f}'
                    else:
                        data_aposentadoria = calcular_data_aposentadoria(int(input_idade.value),
                                                                         int(tempo_contribuicao.value), 'idade',
                                                                         menu_genero.value)
                        text_resultad.value = f'Você não poderá se aposentar ainda. Apenas em {data_aposentadoria.strftime("%d/%m/%Y")}.'
                        text_resultad_salario.value = f'Sem salário sobre a aposentadoria!!!'
                else:  # Para tempo de contribuição
                    if int(tempo_contribuicao.value) >= 35:
                        text_resultad.value = 'Você poderá se aposentar por tempo de contribuição.'
                        text_resultad_salario.value = f'Seu salário será de {conta_salario():.3f}'
                    else:
                        data_aposentadoria = calcular_data_aposentadoria(int(input_idade.value),
                                                                         int(tempo_contribuicao.value), 'tempo',
                                                                         menu_genero.value)
                        text_resultad.value = f'Você não poderá se aposentar ainda. Apenas em {data_aposentadoria.strftime("%d/%m/%Y")}.'
                        text_resultad_salario.value = f'Sem salário sobre a aposentadoria!!!'

            else:  # Para o gênero feminino
                if categoria_aposentadoria.value == 'idade':
                    if int(tempo_contribuicao.value) >= 15 and int(input_idade.value) >= 62:
                        text_resultad.value = 'Você poderá se aposentar devido à sua alta idade.'
                        text_resultad_salario.value = f'Seu salário será de {conta_salario():.3f}'
                    else:
                        data_aposentadoria = calcular_data_aposentadoria(int(input_idade.value),
                                                                         int(tempo_contribuicao.value), 'idade',
                                                                         menu_genero.value)
                        text_resultad.value = f'Você não poderá se aposentar ainda. Apenas em {data_aposentadoria.strftime("%d/%m/%Y")}.'
                        text_resultad_salario.value = f'Sem salário sobre a aposentadoria!!!'

                else:  # Para tempo de contribuição
                    if int(tempo_contribuicao.value) >= 30:
                        text_resultad.value = 'Você poderá se aposentar por tempo de contribuição.'
                        text_resultad_salario.value = f'Seu salário será de {conta_salario():.3f}'
                    else:
                        data_aposentadoria = calcular_data_aposentadoria(int(input_idade.value),
                                                                         int(tempo_contribuicao.value), 'tempo',
                                                                         menu_genero.value)
                        text_resultad.value = f'Você não poderá se aposentar ainda. Apenas em {data_aposentadoria.strftime("%d/%m/%Y")}.'
                        text_resultad_salario.value = f'Sem salário sobre a aposentadoria!!!'

            page.go('/terceira_tela_aposentadoria_resultado')

        except ValueError:
            text_resultad_erro.value = 'Valor inserido inválido'
            # media_salarial.error = True
            # media_salarial.error_text = "Preencha o campo corretamente"
            print('valor inválidooo')
            page.update()
            return


    def calcular_data_aposentadoria(idade_atual, tempo_contribuicao_atual, categoria, genero):
        data_atual = datetime.now()

        if genero == 'masculino':
            if categoria == 'idade':
                anos_ate_aposentadoria = max(0, 65 - idade_atual)
            else:  # Para tempo de contribuição
                anos_ate_aposentadoria = max(0, 35 - tempo_contribuicao_atual)
        else:  # Para o gênero feminino
            if categoria == 'idade':
                anos_ate_aposentadoria = max(0, 62 - idade_atual)
            else:  # Para tempo de contribuição
                anos_ate_aposentadoria = max(0, 30 - tempo_contribuicao_atual)

        # Retorna a data atual acrescida dos anos calculados até a aposentadoria
        return data_atual + relativedelta(years=anos_ate_aposentadoria)

    # É utilizado o max para calcular quantos anos faltam para atingir a idade mínima de aposentadoria para homens
    # (65 anos) sem ir para o negativo

    def conta_salario():
        # try:
            valor_contri = int(tempo_contribuicao.value)
            salario = float(media_salarial.value)

            # Cálculo inicial de 60% da média salarial
            aposentadoria = salario * 60 / 100

            # Verifica se o tempo de contribuição excede 15 anos
            if valor_contri > 15:
                anos_excedentes = valor_contri - 15
                acrescimo = anos_excedentes * 2 / 100 * salario
                aposentadoria += acrescimo
                return aposentadoria
        # except ValueError:
        #     text_resultad_erro.value = ' Valor inserido inválido'
        #     page.update()
        #     return

            # += é um utilizado para somar um valor a uma variável existente e atribui o resultado novamente à mesma variável
            # no caso, aposentadoria += acrescimo e retorna na (aposentadoria)

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                '/',
                [

                    AppBar(title=Text('Simulador de Aposentadoria', font_family="Arial"), bgcolor=Colors.BLACK,
                           color=Colors.WHITE, center_title=True),

                    Container(
                        Column(
                            [
                                imagem,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                        ),
                        alignment=ft.alignment.center,
                        padding=ft.padding.only(top=140)

                    ),

                    Container(
                        Column(
                            [
                                # ElevatedButton(text='Simulador aposentadoria',
                                #                on_click=lambda _: page.go('/primeira_tela_aposentadoria')),
                                #
                                # ElevatedButton(text='Regras aposentadoria',
                                #                on_click=lambda _: page.go('/segunda_tela_regras')
                                #                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                        ),
                        alignment=ft.alignment.center,
                        padding=ft.padding.only(top=100)

                    ),

                    pagelet

                ]

            )
        )

        if page.route == '/primeira_tela_aposentadoria':
            page.views.append(

                View(
                    "/",

                    [

                       AppBar(title=Text('Formulário aposentadoria', font_family='Arial' ), bgcolor=Colors.BLUE_ACCENT,
                              center_title=CENTER ,leading=ft.Icon(ft.Icons.VERTICAL_ALIGN_CENTER)),


                        input_idade,
                        menu_genero,
                        tempo_contribuicao,
                        media_salarial,
                        categoria_aposentadoria,
                        ElevatedButton(text='Resultado aposentadoria',
                                       on_click=calcular_aposentadoria, bgcolor=Colors.BLUE_ACCENT, color=Colors.WHITE,),
                        text_resultad_erro,

                        pagelet

                    ],
                )
            )

        elif page.route == '/segunda_tela_regras':
            # page.views.theme_mode = ft.ThemeMode.DARK
            (page.views.append
                (
                View(
                    "/",
                    [
                        AppBar(title=Text('REGRAS', font_family="Arial"), bgcolor=Colors.BLUE_ACCENT, leading=ft.Icon(ft.Icons.VERTICAL_ALIGN_CENTER) ),

                        Container(
                            Column(
                                [
                                    input_regras,
                                    imagem_regras,
                                ],
                                alignment=ft.MainAxisAlignment.START,
                                horizontal_alignment=ft.CrossAxisAlignment.START,
                            ),

                        ),
                        pagelet
                    ],
                    # bgcolor=Colors.BLUE_ACCENT #Mudar cor do fundo de cada view
                )
            ))

        elif page.route == '/terceira_tela_aposentadoria_resultado':
            page.views.append(
                View(
                    "/",
                    [
                        AppBar(title=Text('RESULTADO', font_family="Arial"), bgcolor=Colors.BLUE_ACCENT, ),

                        text_resultad,
                        text_resultad_salario,

                        pagelet

                    ],

                )
            )
        page.update()

    input_idade = ft.TextField(label='Digite sua idade', hover_color=Colors.BLUE)
    menu_genero = ft.Dropdown(
        label='Menu Gênero',
        width=page.window.width,
        fill_color=Colors.RED,
        options=[Option(key='masculino', text='Masculino'), Option(key='feminino', text='Feminino')],

    )
    tempo_contribuicao = ft.TextField(label='Tempo de contribuição', hover_color=Colors.BLUE)
    media_salarial = ft.TextField(label='Média salarial', hover_color=Colors.BLUE)

    categoria_aposentadoria = ft.Dropdown(
        label='Categoria aposentadoria',
        width=page.window.width,
        fill_color=Colors.RED,
        options=[Option(key='tempo de contribuição', text='tempo de contribuição'), Option(key='idade', text='idade')],
    )

    text_resultad = ft.TextField(label='Resultado aposentadoria', value='', width=page.window.width, multiline=True)
    text_resultad_salario = ft.TextField(label='Resultado salário', value='', width=page.window.width, multiline=True)
    text_resultad_erro = ft.Text(value='', size=20, color=Colors.RED)

    imagem = ft.Image(
        src='assets/inss.png',
        width=300,
        fit=ft.ImageFit.CONTAIN,
        border_radius=10,  # Bordas arredondadas
    )

    imagem_regras = ft.Image(
        src='assets/regras.png',
        width=200,
        fit=ft.ImageFit.CONTAIN,
        border_radius=20

    )

    input_regras = Container(
        Column(
            [
                ft.Text("Titulo: Aposentadoria por idade\n"
                        "Mulheres: Idade mínima de 62 anos e mínimo de 15 anos de contribuição\n"
                        "Homens: Idade mínima de 65 anos e mínimo de 20 anos de contribuição\n\n"
                        "Aposentadoria por Tempo de Contribuição:\n"
                        "Homens: 35 anos de contribuição\n"
                        "Mulheres: 30 anos de contribuição", size=17, color=Colors.WHITE, font_family="Arial", )
            ],
            alignment=ft.MainAxisAlignment.START,
        ),
        padding=ft.padding.all(20),  # Padding ao redor do Container
        bgcolor=Colors.BLUE_GREY,  # Cor de fundo do Container
        border_radius=10,  # Bordas arredondadas

    )

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar
    page.on_route_change = gerencia_rotas
    page.go(page.route)

    # Criação de componentes


ft.app(main)