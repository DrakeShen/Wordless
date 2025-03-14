# ----------------------------------------------------------------------
# Wordless: Figures - Frequencies
# Copyright (C) 2018-2022  Ye Lei (叶磊)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------

import matplotlib
import matplotlib.pyplot
import networkx
import numpy
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QDesktopWidget
import wordcloud

from wl_utils import wl_misc, wl_sorting

_tr = QCoreApplication.translate

def wl_fig_freq(main, tokens_freq_files, settings, label_x):
    file_names_selected = [*main.wl_file_area.get_selected_file_names(), _tr('wl_fig_freq', 'Total')]
    col_sort_by_file = file_names_selected.index(settings['sort_by_file'])

    tokens_freq_files = wl_sorting.sorted_tokens_freq_files(
        tokens_freq_files,
        sort_by_col = col_sort_by_file
    )

    if settings['rank_min_no_limit']:
        rank_min = 1
    else:
        rank_min = settings['rank_min']

    if settings['rank_max_no_limit']:
        rank_max = None
    else:
        rank_max = settings['rank_max']

    # Line Chart
    if settings['graph_type'] == _tr('wl_fig_freq', 'Line Chart'):
        total_freqs = numpy.array(list(zip(*tokens_freq_files))[1]).sum(axis = 0)

        tokens = [item[0] for item in tokens_freq_files[rank_min - 1 : rank_max]]
        freqs = [item[1] for item in tokens_freq_files if item[0] in tokens]

        if settings['use_pct']:
            if settings['use_cumulative']:
                matplotlib.pyplot.ylabel(_tr('wl_fig_freq', 'Cumulative Percentage Frequency'))
            else:
                matplotlib.pyplot.ylabel(_tr('wl_fig_freq', 'Percentage Frequency'))
        else:
            if settings['use_cumulative']:
                matplotlib.pyplot.ylabel(_tr('wl_fig_freq', 'Cumulative Frequency'))
            else:
                matplotlib.pyplot.ylabel(_tr('wl_fig_freq', 'Frequency'))

        if settings['use_cumulative']:
            for i, freq_files in enumerate(freqs):
                if i >= 1:
                    freqs[i] = [
                        freq_cumulative + freq
                        for freq_cumulative, freq in zip(freqs[i - 1], freq_files)
                    ]

        if settings['use_pct']:
            for i, file_name in enumerate(file_names_selected):
                matplotlib.pyplot.plot(
                    [freq_files[i] / total_freqs[i] * 100 for freq_files in freqs],
                    label = file_name
                )
        else:
            for i, file_name in enumerate(file_names_selected):
                matplotlib.pyplot.plot(
                    [freq_files[i] for freq_files in freqs],
                    label = file_name
                )

        matplotlib.pyplot.xlabel(label_x)
        matplotlib.pyplot.xticks(
            range(len(tokens)),
            labels = tokens,
            fontproperties = main.settings_custom['figs']['line_chart']['font'],
            rotation = 90
        )

        matplotlib.pyplot.grid(True)
        matplotlib.pyplot.legend()
    # Word Cloud
    elif settings['graph_type'] == _tr('wl_fig_freq', 'Word Cloud'):
        if rank_max is None:
            max_words = len(tokens_freq_files) - rank_min + 1
        else:
            max_words = rank_max - rank_min + 1

        word_cloud = wordcloud.WordCloud(
            width = QDesktopWidget().width(),
            height = QDesktopWidget().height(),
            background_color = main.settings_custom['figs']['word_cloud']['bg_color'],
            max_words = max_words
        )

        tokens_freq_file = {
            token: freqs[col_sort_by_file]
            for token, freqs in tokens_freq_files[rank_min - 1 : rank_max]
        }

        # Fix zero frequencies
        for token, freq in tokens_freq_file.items():
            if freq == 0:
                tokens_freq_file[token] += 0.000000000000001

        word_cloud.generate_from_frequencies(tokens_freq_file)

        matplotlib.pyplot.imshow(word_cloud, interpolation = 'bilinear')
        matplotlib.pyplot.axis('off')
    # Network Graph
    elif settings['graph_type'] == _tr('wl_fig_freq', 'Network Graph'):
        tokens_freq_file = {
            token: freqs[col_sort_by_file]
            for token, freqs in tokens_freq_files[rank_min - 1 : rank_max]
        }

        graph = networkx.MultiDiGraph()
        graph.add_edges_from(tokens_freq_file)

        if main.settings_custom['figs']['network_graph']['layout'] == _tr('wl_fig_freq', 'Circular'):
            layout = networkx.circular_layout(graph)
        elif main.settings_custom['figs']['network_graph']['layout'] == _tr('wl_fig_freq', 'Kamada-Kawai'):
            layout = networkx.kamada_kawai_layout(graph)
        elif main.settings_custom['figs']['network_graph']['layout'] == _tr('wl_fig_freq', 'Planar'):
            layout = networkx.planar_layout(graph)
        elif main.settings_custom['figs']['network_graph']['layout'] == _tr('wl_fig_freq', 'Random'):
            layout = networkx.random_layout(graph)
        elif main.settings_custom['figs']['network_graph']['layout'] == _tr('wl_fig_freq', 'Shell'):
            layout = networkx.shell_layout(graph)
        elif main.settings_custom['figs']['network_graph']['layout'] == _tr('wl_fig_freq', 'Spring'):
            layout = networkx.spring_layout(graph)
        elif main.settings_custom['figs']['network_graph']['layout'] == _tr('wl_fig_freq', 'Spectral'):
            layout = networkx.spectral_layout(graph)

        networkx.draw_networkx_nodes(
            graph,
            pos = layout,
            node_size = 800,
            node_color = '#FFFFFF',
            alpha = 0.4
        )
        networkx.draw_networkx_edges(
            graph,
            pos = layout,
            edgelist = tokens_freq_file,
            edge_color = main.settings_custom['figs']['network_graph']['edge_color'],
            width = wl_misc.normalize_nums(
                tokens_freq_file.values(),
                normalized_min = 1,
                normalized_max = 5
            )
        )
        networkx.draw_networkx_labels(
            graph,
            pos = layout,
            font_family = main.settings_custom['figs']['network_graph']['node_font'],
            font_size = main.settings_custom['figs']['network_graph']['node_font_size']
        )
        networkx.draw_networkx_edge_labels(
            graph,
            pos = layout,
            edge_labels = tokens_freq_file,
            font_family = main.settings_custom['figs']['network_graph']['edge_font'],
            font_size = main.settings_custom['figs']['network_graph']['edge_font_size'],
            label_pos = 0.2
        )

def wl_fig_freq_keyword_extractor(main, tokens_freq_files, files_ref, settings, label_x):
    file_names_selected = [_tr('wl_fig_freq_keyword_extractor', 'Reference Files'), *main.wl_file_area.get_selected_file_names(), _tr('wl_fig_freq_keyword_extractor', 'Total')]
    file_names_selected = [
        file_name
        for file_name in file_names_selected
        if file_name not in files_ref
    ]
    col_sort_by_file = file_names_selected.index(settings['sort_by_file'])

    tokens_freq_files = wl_sorting.sorted_tokens_freq_files_ref(
        tokens_freq_files,
        sort_by_col = col_sort_by_file
    )

    if settings['rank_min_no_limit']:
        rank_min = 1
    else:
        rank_min = settings['rank_min']

    if settings['rank_max_no_limit']:
        rank_max = None
    else:
        rank_max = settings['rank_max']

    # Line Chart
    if settings['graph_type'] == _tr('wl_fig_freq_keyword_extractor', 'Line Chart'):
        total_freqs = numpy.array([item[1] for item in tokens_freq_files]).sum(axis = 0)

        tokens = [item[0] for item in tokens_freq_files[rank_min - 1 : rank_max]]
        freqs = [item[1] for item in tokens_freq_files if item[0] in tokens]

        if settings['use_pct']:
            if settings['use_cumulative']:
                matplotlib.pyplot.ylabel(_tr('wl_fig_freq_keyword_extractor', 'Cumulative Percentage Frequency'))
            else:
                matplotlib.pyplot.ylabel(_tr('wl_fig_freq_keyword_extractor', 'Percentage Frequency'))
        else:
            if settings['use_cumulative']:
                matplotlib.pyplot.ylabel(_tr('wl_fig_freq_keyword_extractor', 'Cumulative Frequency'))
            else:
                matplotlib.pyplot.ylabel(_tr('wl_fig_freq_keyword_extractor', 'Frequency'))

        if settings['use_cumulative']:
            for i, freq_files in enumerate(freqs):
                if i >= 1:
                    freqs[i] = [
                        freq_cumulative + freq
                        for freq_cumulative, freq in zip(freqs[i - 1], freq_files)
                    ]

        if settings['use_pct']:
            for i, file_name in enumerate(file_names_selected):
                matplotlib.pyplot.plot(
                    [freq_files[i] / total_freqs[i] * 100 for freq_files in freqs],
                    label = file_name
                )
        else:
            for i, file_name in enumerate(file_names_selected):
                matplotlib.pyplot.plot(
                    [freq_files[i] for freq_files in freqs],
                    label = file_name
                )

        matplotlib.pyplot.xlabel(label_x)
        matplotlib.pyplot.xticks(
            range(len(tokens)),
            labels = tokens,
            fontproperties = main.settings_custom['figs']['line_chart']['font'],
            rotation = 90
        )

        matplotlib.pyplot.grid(True, color = 'silver')
        matplotlib.pyplot.legend()
    # Word Cloud
    elif settings['graph_type'] == _tr('wl_fig_freq_keyword_extractor', 'Word Cloud'):
        if rank_max is None:
            max_words = len(tokens_freq_files) - rank_min + 1
        else:
            max_words = rank_max - rank_min + 1

        word_cloud = wordcloud.WordCloud(
            width = QDesktopWidget().width(),
            height = QDesktopWidget().height(),
            background_color = main.settings_custom['figs']['word_cloud']['bg_color'],
            max_words = max_words
        )

        tokens_freq_file = {
            token: freq_files[col_sort_by_file]
            for token, freq_files in tokens_freq_files[rank_min - 1 : rank_max]
        }

        # Fix zero frequencies
        for token, freq in tokens_freq_file.items():
            if freq == 0:
                tokens_freq_file[token] += 0.000000000000001

        word_cloud.generate_from_frequencies(tokens_freq_file)

        matplotlib.pyplot.imshow(word_cloud, interpolation = 'bilinear')
        matplotlib.pyplot.axis('off')
