#coding: utf-8
import logging
import datetime

import tornado.escape

from config import BaseController


class SimulationPlotsController(BaseController):
    """/v1/simulation_plots"""
    def get(self):
        return


class ChapterPlotsController(BaseController):
    """/v1/chapter_plots"""
    def get(self):
        return


class SimulationPlotController(BaseController):
    """/v1/simulation_plot/[(0-9)]+"""
    def get(self, plot_id):
        return


class ChapterPlotController(BaseController):
    """/v1/chapter_plot/[0-9]+"""
    def get(self, plot_id):