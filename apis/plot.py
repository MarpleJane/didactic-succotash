#coding: utf-8
import logging
import datetime

import tornado.escape

from config import BaseController
from config.dmls_api import SIMULATIONS, CHAPTERS, USERS


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
        chapter = self.select_all(CHAPTERS["CHAPTER_PLOT"], params)
        chapter = chapter[0]
        self.write(dict(chapter=chapter))


class ChapterInfoController(BaseController):
    """/v1/chapter_info"""
    def post(self):
        w_id = self.get_argument("w_id")
        type_id = self.get_argument("type_id")
        params_user = {"w_id": w_id}
        user_data = self.find_data(USERS["FIND_USER"], params_user)
        user_chapter = []
        if user_data:
            params = {"user_id": user_data["id"], "type_id": type_id}
            user_chapter = self.select_all(CHAPTERS["CHAPTER_TO_USER"], params)
            
        self.write(dict(user_chapter=user_chapter))  # if user_chapter=[] 
                                                     # then user not exist or error occurred


class ChapterChallengeController(BaseController):
    """/v1/add_update/chapter_challenge"""
    def post(self):
        w_id = self.get_argument("w_id")
        plot_id = self.get_argument("plot_id")
        score = self.get_argument("score")
        params_user = {"w_id": w_id}
        user_data = self.find_data(USERS["FIND_USER"], params_user)
        ret = 0
        if user_data:
            params = {
                "user_id": user_data["id"],
                "plot_id": plot_id,
                "score": score
            }
            challenge_data = self.find_data(CHAPTERS["CHAPTER_CHALLENGE_FIND"], params)
            if challenge_data:
                logging.warn("Update data: in <ChapterChallengeController>")
                if score < challenge_data["score"]:
                    score = challenge_data["score"]
                chapter_params = {
                    "user_id": user_data["id"],
                    "plot_id": plot_id,
                    "score": score,
                    "update_time": self.current_time()
                }
                ret = self.update_data(CHAPTERS["CHAPTER_CHALLENGE_UPDATE"], chapter_params)
            else:
                logging.warn("Insert data: in <ChapterChallengeController>")
                ret = self.insert_data(CHAPTERS["CHAPTER_CHALLENGE_INSERT"], params)
                if ret == 0:
                    ret = self.update_data(CHAPTERS["CHAPTER_ADD_CHALLENGER"], params)
        else:
            ret = 1
            logging.warn("No user data: in <ChapterChallengeController>")
        self.write(dict(ret=ret))


class SimulationChallengeController(BaseController):
    """/v1/add_update/simulation_challenge"""
    def post(self):
        w_id = self.get_argument("w_id")
        plot_id = self.get_argument("plot_id")
        score = self.get_argument("score")
        score = int(score)
        params_user = {"w_id": w_id}
        user_data = self.find_data(USERS["FIND_USER"], params_user)
        ret = 0
        if user_data:
            params = {
                "user_id": user_data["id"],
                "plot_id": plot_id,
                "score": int(score)
            }
            challenge_data = self.find_data(SIMULATIONS["SIMULATION_CHALLENGE_FIND"], params)
            if challenge_data:
                logging.warn("Update data: in <SimulationChallengeController>")
                if score < challenge_data["score"]:
                    score = challenge_data["score"]
                simulation_params = {
                    "user_id": user_data["id"],
                    "plot_id": plot_id,
                    "score": score,
                    "update_time": self.current_time()
                }
                ret = self.update_data(SIMULATIONS["SIMULATION_CHALLENGE_UPDATE"], simulation_params)
            else:
                logging.warn("Insert data: in <SimulationChallengeController>")
                ret = self.insert_data(SIMULATIONS["SIMULATION_CHALLENGE_INSERT"], params)
                if ret == 0:
                    ret = self.update_data(SIMULATIONS["SIMULATION_ADD_CHALLENGER"], params)
        else:
            ret = 1
            logging.warn("No user data: in <SimulationChallengeController>")
        self.write(dict(ret=ret))

