# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.shortcuts import render
import altair as alt
import pandas as pd
from vega_datasets import data

class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = locals()

        # Chart 1
        data3 = pd.DataFrame({
            'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
            'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
        })

        context['chart1'] = alt.Chart(data3).mark_bar().encode(
            x='a',
            y='b'
        ).interactive()


        # Chart 2
        source = data.cars()

        context['chart2'] = alt.Chart(source).mark_circle().encode(
            x='Horsepower',
            y='Miles_per_Gallon',
            color='Origin'
        ).interactive()


        # Chart 3
        df = data.movies.url
        pts = alt.selection(type="single", encodings=['x'])
        brush = alt.selection(type="interval")

        rect = alt.Chart(df).mark_bar().encode(
            alt.X('IMDB_Rating:Q', bin=True),
            alt.Y('Rotten_Tomatoes_Rating:Q', bin=True),
            color=alt.condition(pts, 'Rotten_Tomatoes_Rating:Q', alt.value('lightgray'))
        ).add_selection(
            pts
        )

        circ = alt.Chart(df).mark_point().encode(
            alt.ColorValue('lightgray'),
            alt.Size(
                'count()',
                legend = alt.Legend(title="Number of Movies Selected")
            )
        ).transform_filter(
            pts
        )

        context['chart3'] = rect | circ

        # text = alt.Chart(df).mark_text().encode(
        #     y=alt.Y('row_number:0', axis=None)
        # ).transform_window(
        #     row_number='row_number()'
        # ).transform_filter(
        #     pts
        # ).transform_window(
        #     rank='rank(row_number)'
        # ).transform_filter(
        #     alt.datum.rank < 20
        # )

        # context['chart0'] = text
        
        # ratings = text.encode(
        #     text = 'Rotten_Tomatoes_Rating:Q'
        # )

        # moviename = text.encode(
        #     text = 'Title:N'
        # )

        # line = alt.Chart(df).mark_line().encode(
        #     x="Majro_Genre:N",
        #     y="count()"
        # )

        # bar = alt.Chart(df).mark_bar().encode(
        #     x="Majro_Genre:N",
        #     y="count()"
        # ).properties(
        #     width=700,
        #     height=250
        # ).add_selection(
        #     pts
        # )

        # context['chart3'] = ( rect | text | circ | line ) & bar
        # # <!-- (rect | ratings | moviename | line ) & bar -->
        
        # context['chart3'] = alt.vconcat(
        #     (rect + circ | line ),
        #     bar
        # ).resolve_legend(
        #     color='independent',
        #     size='independent'
        # )

        return render(request, self.template_name, context)