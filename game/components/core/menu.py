from utils.i18n.menu import MainMenuOptions, ConfigMenuOptions


class MainMenu:
    def __init__(self):
        self.active = True
        self.options = [
            MainMenuOptions.START_GAME,
            MainMenuOptions.SETTINGS,
            MainMenuOptions.QUIT,
        ]
        self.selected = 0


class SettingsMenu:
    def __init__(self):
        self.active = True
        self.options = [ConfigMenuOptions.CHANGE_RES, ConfigMenuOptions.BACK]
        self.selected = 0
        self.res_options = []
        self.res_selected = 0
        self.display_res_list = False
