#coding: utf-8
import logging
import datetime

import tornado.escape

from config import BaseController
from config.dmls_api import SIMULATIONS, CHAPTERS


class SimulationPlotsController(BaseController):
    """/v1/simulation_plots/([0-9]+)"""
    def get(self, type_id):
        type_id = int(type_id)
        params = {"type_id": type_id}
        simulations = self.select_all(SIMULATIONS["SIMULATION_PLOTS"], params)
        self.write(dict(simulations=simulations))


class ChapterPlotsController(BaseController):
    """/v1/chapter_plots/([0-9]+)"""
    def get(self, type_id):
        type_id = int(type_id)
        params = {"type_id": type_id}
        chapters = self.select_all(CHAPTERS["CHAPTER_PLOTS"], params)
        self.write(dict(chapters=chapters))


class SimulationPlotController(BaseController):
    """/v1/simulation_plot/([0-9]+)"""
    def get(self, plot_id):
        plot_id = int(plot_id)
        params = {"plot_id": plot_id}
        simulation = self.select_all(SIMULATIONS["SIMULATION_PLOT"], params)
        simulation = simulation[0]
        self.write(dict(simulation=simulation))


class ChapterPlotController(BaseController):
    """/v1/chapter_plot/([0-9]+)"""
    def get(self, plot_id):
        plot_id = int(plot_id)
        params = {"plot_id": plot_id}
        chapter = self.select_all(CHAPTERS["CHAPTER_PLOT"], params))
        chapter = chapter[0]
        self.write(dict(chapter=chapter))