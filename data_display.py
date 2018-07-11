# -*- coding: utf-8 -*-
# @Time    : 2018/7/11 17:26
# @Author  : MengnanChen
# @FileName: consumer_data.py
# @Software: PyCharm Community Edition

# display on website

from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
import random
import time
import pandas as pd
from bokeh.models import HoverTool
from bokeh.models import glyphs
from mongo_utils import mongo_utils
from bokeh.layouts import column
import global_vals

# the style of tooltips
# refer to official tutorial, A1 Models and Primitives
tooltips_steps = """
<div>
    <span style="font-size: 17px; font-weight: bold;">@y</span>&nbsp;
</div>
"""
tooltips_heart = """
<div>
    <span style="font-size: 17px; font-weight: bold;">@heart_rate</span>&nbsp;
</div>
"""
### steps figure
fig_steps = figure(plot_width=1000, plot_height=300, x_axis_type='datetime',
                   title='steps per {} second'.format(global_vals.data_produce_duration))
fig_steps.xaxis.axis_label = 'steps'  # axis label
fig_steps.yaxis.axis_label = 'time'
fig_steps.background_fill_color = 'beige'  # the color of background is 'beige'
fig_steps.background_fill_alpha = 0.5
source_steps = ColumnDataSource(data=dict(x=[pd.to_datetime(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))],
                                    y=[0])) # data source
# line figure, the data of x axis come from key x of dict 'source_steps'
fig_steps.line(x='x', y='y', alpha=0.5, legend='steps', source=source_steps)
steps_glyph = glyphs.Circle(x='x', y='y', size=3, fill_color='white')
steps_add = fig_steps.add_glyph(source_or_glyph=source_steps, glyph=steps_glyph)
hover = HoverTool(tooltips=tooltips_steps, renderers=[steps_add])
fig_steps.legend.location = 'bottom_left'
fig_steps.add_tools(hover)

# heart rate figure
fig_heart = figure(plot_width=1000, plot_height=300, x_axis_type='datetime',
                   title='heart rate per {} second'.format(global_vals.data_produce_duration))
fig_heart.xaxis.axis_label = 'heart rate'  # axis label
fig_heart.yaxis.axis_label = 'time'
fig_heart.background_fill_color = 'beige'  # the color of background is 'beige'
fig_heart.background_fill_alpha = 0.5
source_heart = ColumnDataSource(data=dict(time=[pd.to_datetime(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))],
                                    heart_rate=[0]))
fig_heart.line(x='time', y='heart_rate', alpha=0.5, legend='heart rate', color='blue',source=source_heart)
heart_glyph = glyphs.Circle(x='time', y='heart_rate', size=3, fill_color='white')
heart_add = fig_heart.add_glyph(source_or_glyph=source_heart, glyph=heart_glyph)
hover = HoverTool(tooltips=tooltips_heart, renderers=[heart_add])
fig_heart.legend.location = 'bottom_left'
fig_heart.add_tools(hover)

def update():
    data_dict = mongo_utils.query_last_row(global_vals.uid)
    new_data_steps = dict(x=[pd.to_datetime(data_dict['timestamp'])],
                          y=[int(data_dict['steps'])]) # name variable as x,y in order to be easy to understand
    source_steps.stream(new_data=new_data_steps, rollover=200)

    new_data_heart=dict(time=[pd.to_datetime(data_dict['timestamp'])],heart_rate=[int(data_dict['heart_rate'])])
    source_heart.stream(new_data=new_data_heart,rollover=200)

curdoc().add_periodic_callback(update, global_vals.data_produce_duration*1000)
curdoc().add_root(column(fig_steps,fig_heart))