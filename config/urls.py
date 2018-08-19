#coding: utf-8
from apis import *
from backend import *

urls = [
    ("/v1/simulation/love_experience", LoveController),
    ("/v1/simulation/dregs_experience", DregController),
    ("/v1/add_new/simulation", SimulationAddNewController),
    ("/v1/del/simulation", SimulationDelController),

    ("/v1/chapter/kira_campus", KiraCampusController),
    ("/v1/chapter/kamisama", KamisamaController),
    ("/v1/add_new/chapter",ChapterAddNewController),
    ("/v1/del/chapter", ChapterDelController),

    ("/upload/picture", UploadPictureController),
    
    ("/v1/admin", AdminController),
    ("/v1/admin/add", AdminAddController),

    ("/v1/user_rank", UserRankController),
    ("/v1/user_signup", UserSignupController),
    ("/v1/user_info/([0-9]+)", UserInfo),
    ("/v1/get_coins/([0-9]+)", GetCoinsController),

    ("/v1/simulation_plots/([0-9])+", SimulationPlotsController),
    ("/v1/chapter_plots/([0-9])+", ChapterPlotsController),
    ("/v1/simulation_plot/[(0-9)]+", SimulationPlotController),
    ("/v1/chapter_plot/[0-9]+", ChapterPlotController),
]