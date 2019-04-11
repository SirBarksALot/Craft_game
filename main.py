import os
import sys
from panda3d.core import load_prc_file_data
from direct.showbase.ShowBase import ShowBase

# Switch into the current directory
os.chdir(os.path.realpath(os.path.dirname(__file__)))

# Insert the pipeline path to the system path, this is required to be
# able to import the pipeline classes
pipeline_path = "C:\\Users\\filip.lezuch\\PycharmProjects\\RenderPipeline/"
sys.path.insert(0, pipeline_path)
from rpcore import RenderPipeline


class MainApp(ShowBase):
    def __init__(self):
        # game version
        game_version = 'version 0.1.3'
        # Setup window size and title
        load_prc_file_data("", """
        win-size 1600 900
        window-title Craft game {}
        """.format(game_version))

        # ------ Begin of render pipeline code ------

        self.render_pipeline = RenderPipeline()
        self.render_pipeline.create(self)

        # ------ End of render pipeline code, that is it! ------

        # Set time of day
        self.render_pipeline.daytime_mgr.time = "5:20"

        # Configuration variables
        self.half_energy = 5000
        self.lamp_fov = 70
        self.lamp_radius = 10


MainApp().run()
