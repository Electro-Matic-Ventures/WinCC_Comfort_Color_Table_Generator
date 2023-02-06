from PyQt6.QtWidgets import QMainWindow, QFileDialog
from PyQt6.QtGui import QIcon
from CentralWidget import CentralWidget
from ApplicationData import ApplicationData
from Generate import Generate

class MainWindow(QMainWindow):
    
    widget: CentralWidget
    data: ApplicationData
    
    def __init__(self):
        super().__init__()
        self.widget = CentralWidget()
        self.data = ApplicationData()
        self.__set_appearance()
        self.setCentralWidget(self.widget)
        self.__connect_actions()
        return
    
    def __set_appearance(self)-> None:
        self.setWindowTitle("WinCC Comofort Color Table Generator")
        self.setWindowIcon(QIcon('icon.png'))
        self.setContentsMargins(10,10,10,10)
        self.setStyleSheet(self.__generate_style_sheet())        
        return
        
    def __generate_style_sheet(self)-> str:
        return '''
            MainWindow {
                background-color: #222831;
            }
        '''
        
    def __connect_actions(self)-> None:
        self.__connect_background_actions()
        self.__connect_foreground_actions()
        self.__connect_output_path_actions()
        self.__connect_generate_button_actions()
        return
    
    def __connect_background_actions(self)-> None:
        self.__connect_background_white_actions()
        self.__connect_background_black_actions()
        self.__connect_background_red_actions()
        self.__connect_background_yellow_actions()
        self.__connect_background_green_actions()
        self.__connect_background_teal_actions()
        self.__connect_background_blue_actions()
        self.__connect_background_purple_actions()
        return
    
    def __connect_background_white_actions(self)-> None:
        self.widget.background.white.color_enable.stateChanged.connect(self.__background_white_enabled_action)
        self.widget.background.white.color_min.input_.textChanged.connect(self.__background_white_min_action)
        self.widget.background.white.color_max.input_.textChanged.connect(self.__background_white_max_action)
        self.widget.background.white.color_steps.input_.textChanged.connect(self.__background_white_steps_action)
        return
        
    def __connect_background_black_actions(self)-> None:
        self.widget.background.black.color_enable.stateChanged.connect(self.__background_black_enabled_action)
        self.widget.background.black.color_min.input_.textChanged.connect(self.__background_black_min_action)
        self.widget.background.black.color_max.input_.textChanged.connect(self.__background_black_max_action)
        self.widget.background.black.color_steps.input_.textChanged.connect(self.__background_black_steps_action)
        return
        
    def __connect_background_red_actions(self)-> None:
        self.widget.background.red.color_enable.stateChanged.connect(self.__background_red_enabled_action)
        self.widget.background.red.color_min.input_.textChanged.connect(self.__background_red_min_action)
        self.widget.background.red.color_max.input_.textChanged.connect(self.__background_red_max_action)
        self.widget.background.red.color_steps.input_.textChanged.connect(self.__background_red_steps_action)
        return
        
    def __connect_background_yellow_actions(self)-> None:
        self.widget.background.yellow.color_enable.stateChanged.connect(self.__background_yellow_enabled_action)
        self.widget.background.yellow.color_min.input_.textChanged.connect(self.__background_yellow_min_action)
        self.widget.background.yellow.color_max.input_.textChanged.connect(self.__background_yellow_max_action)
        self.widget.background.yellow.color_steps.input_.textChanged.connect(self.__background_yellow_steps_action)
        return
        
    def __connect_background_green_actions(self)-> None:
        self.widget.background.green.color_enable.stateChanged.connect(self.__background_green_enabled_action)
        self.widget.background.green.color_min.input_.textChanged.connect(self.__background_green_min_action)
        self.widget.background.green.color_max.input_.textChanged.connect(self.__background_green_max_action)
        self.widget.background.green.color_steps.input_.textChanged.connect(self.__background_green_steps_action)
        return
        
    def __connect_background_teal_actions(self)-> None:
        self.widget.background.teal.color_enable.stateChanged.connect(self.__background_teal_enabled_action)
        self.widget.background.teal.color_min.input_.textChanged.connect(self.__background_teal_min_action)
        self.widget.background.teal.color_max.input_.textChanged.connect(self.__background_teal_max_action)
        self.widget.background.teal.color_steps.input_.textChanged.connect(self.__background_teal_steps_action)
        return
        
    def __connect_background_blue_actions(self)-> None:
        self.widget.background.blue.color_enable.stateChanged.connect(self.__background_blue_enabled_action)
        self.widget.background.blue.color_min.input_.textChanged.connect(self.__background_blue_min_action)
        self.widget.background.blue.color_max.input_.textChanged.connect(self.__background_blue_max_action)
        self.widget.background.blue.color_steps.input_.textChanged.connect(self.__background_blue_steps_action)
        return
        
    def __connect_background_purple_actions(self)-> None:
        self.widget.background.purple.color_enable.stateChanged.connect(self.__background_purple_enabled_action)
        self.widget.background.purple.color_min.input_.textChanged.connect(self.__background_purple_min_action)
        self.widget.background.purple.color_max.input_.textChanged.connect(self.__background_purple_max_action)
        self.widget.background.purple.color_steps.input_.textChanged.connect(self.__background_purple_steps_action)
        return
    
    def __connect_foreground_actions(self) -> None:        
        self.__connect_foreground_white_actions()
        self.__connect_foreground_black_actions()
        self.__connect_foreground_red_actions()
        self.__connect_foreground_yellow_actions()
        self.__connect_foreground_green_actions()
        self.__connect_foreground_teal_actions()
        self.__connect_foreground_blue_actions()
        self.__connect_foreground_purple_actions()
        return
    
    def __connect_foreground_white_actions(self)-> None:
        self.widget.foreground.white.color_enable.stateChanged.connect(self.__foreground_white_enabled_action)
        self.widget.foreground.white.color_min.input_.textChanged.connect(self.__foreground_white_min_action)
        self.widget.foreground.white.color_max.input_.textChanged.connect(self.__foreground_white_max_action)
        self.widget.foreground.white.color_steps.input_.textChanged.connect(self.__foreground_white_steps_action)
        return
        
    def __connect_foreground_black_actions(self)-> None:
        self.widget.foreground.black.color_enable.stateChanged.connect(self.__foreground_black_enabled_action)
        self.widget.foreground.black.color_min.input_.textChanged.connect(self.__foreground_black_min_action)
        self.widget.foreground.black.color_max.input_.textChanged.connect(self.__foreground_black_max_action)
        self.widget.foreground.black.color_steps.input_.textChanged.connect(self.__foreground_black_steps_action)
        return
        
    def __connect_foreground_red_actions(self)-> None:
        self.widget.foreground.red.color_enable.stateChanged.connect(self.__foreground_red_enabled_action)
        self.widget.foreground.red.color_min.input_.textChanged.connect(self.__foreground_red_min_action)
        self.widget.foreground.red.color_max.input_.textChanged.connect(self.__foreground_red_max_action)
        self.widget.foreground.red.color_steps.input_.textChanged.connect(self.__foreground_red_steps_action)
        return
        
    def __connect_foreground_yellow_actions(self)-> None:
        self.widget.foreground.yellow.color_enable.stateChanged.connect(self.__foreground_yellow_enabled_action)
        self.widget.foreground.yellow.color_min.input_.textChanged.connect(self.__foreground_yellow_min_action)
        self.widget.foreground.yellow.color_max.input_.textChanged.connect(self.__foreground_yellow_max_action)
        self.widget.foreground.yellow.color_steps.input_.textChanged.connect(self.__foreground_yellow_steps_action)
        return
        
    def __connect_foreground_green_actions(self)-> None:
        self.widget.foreground.green.color_enable.stateChanged.connect(self.__foreground_green_enabled_action)
        self.widget.foreground.green.color_min.input_.textChanged.connect(self.__foreground_green_min_action)
        self.widget.foreground.green.color_max.input_.textChanged.connect(self.__foreground_green_max_action)
        self.widget.foreground.green.color_steps.input_.textChanged.connect(self.__foreground_green_steps_action)
        return
        
    def __connect_foreground_teal_actions(self)-> None:
        self.widget.foreground.teal.color_enable.stateChanged.connect(self.__foreground_teal_enabled_action)
        self.widget.foreground.teal.color_min.input_.textChanged.connect(self.__foreground_teal_min_action)
        self.widget.foreground.teal.color_max.input_.textChanged.connect(self.__foreground_teal_max_action)
        self.widget.foreground.teal.color_steps.input_.textChanged.connect(self.__foreground_teal_steps_action)
        return
        
    def __connect_foreground_blue_actions(self)-> None:
        self.widget.foreground.blue.color_enable.stateChanged.connect(self.__foreground_blue_enabled_action)
        self.widget.foreground.blue.color_min.input_.textChanged.connect(self.__foreground_blue_min_action)
        self.widget.foreground.blue.color_max.input_.textChanged.connect(self.__foreground_blue_max_action)
        self.widget.foreground.blue.color_steps.input_.textChanged.connect(self.__foreground_blue_steps_action)
        return
        
    def __connect_foreground_purple_actions(self)-> None:
        self.widget.foreground.purple.color_enable.stateChanged.connect(self.__foreground_purple_enabled_action)
        self.widget.foreground.purple.color_min.input_.textChanged.connect(self.__foreground_purple_min_action)
        self.widget.foreground.purple.color_max.input_.textChanged.connect(self.__foreground_purple_max_action)
        self.widget.foreground.purple.color_steps.input_.textChanged.connect(self.__foreground_purple_steps_action)
        return
    
    def __background_white_enabled_action(self)-> None:
        self.data.background.white.enabled = self.widget.background.white.is_checked()
        return
  
    def __background_white_min_action(self)-> None:
        self.data.background.white.min_ = self.widget.background.white.min_value()
        return
  
    def __background_white_max_action(self)-> None:
        self.data.background.white.max_ = self.widget.background.white.max_value()
        return
  
    def __background_white_steps_action(self)-> None:
        self.data.background.white.steps = self.widget.background.white.steps_value()
        return
  
    def __background_black_enabled_action(self)-> None:
        self.data.background.black.enabled = self.widget.background.black.is_checked()
        return
  
    def __background_black_min_action(self)-> None:
        self.data.background.black.min_ = self.widget.background.black.min_value()
        return
  
    def __background_black_max_action(self)-> None:
        self.data.background.black.max_ = self.widget.background.black.max_value()
        return
  
    def __background_black_steps_action(self)-> None:
        self.data.background.black.steps = self.widget.background.black.steps_value()
        return
  
    def __background_red_enabled_action(self)-> None:
        self.data.background.red.enabled = self.widget.background.red.is_checked()
        return
  
    def __background_red_min_action(self)-> None:
        self.data.background.red.min_ = self.widget.background.red.min_value()
        return
  
    def __background_red_max_action(self)-> None:
        self.data.background.red.max_ = self.widget.background.red.max_value()
        return
  
    def __background_red_steps_action(self)-> None:
        self.data.background.red.steps = self.widget.background.red.steps_value()
        return
  
    def __background_yellow_enabled_action(self)-> None:
        self.data.background.yellow.enabled = self.widget.background.yellow.is_checked()
        return
  
    def __background_yellow_min_action(self)-> None:
        self.data.background.yellow.min_ = self.widget.background.yellow.min_value()
        return
  
    def __background_yellow_max_action(self)-> None:
        self.data.background.yellow.max_ = self.widget.background.yellow.max_value()
        return
  
    def __background_yellow_steps_action(self)-> None:
        self.data.background.yellow.steps = self.widget.background.yellow.steps_value()
        return
  
    def __background_green_enabled_action(self)-> None:
        self.data.background.green.enabled = self.widget.background.green.is_checked()
        return
  
    def __background_green_min_action(self)-> None:
        self.data.background.green.min_ = self.widget.background.green.min_value()
        return
  
    def __background_green_max_action(self)-> None:
        self.data.background.green.max_ = self.widget.background.green.max_value()
        return
  
    def __background_green_steps_action(self)-> None:
        self.data.background.green.steps = self.widget.background.green.steps_value()
        return
  
    def __background_teal_enabled_action(self)-> None:
        self.data.background.teal.enabled = self.widget.background.teal.is_checked()
        return
  
    def __background_teal_min_action(self)-> None:
        self.data.background.teal.min_ = self.widget.background.teal.min_value()
        return
  
    def __background_teal_max_action(self)-> None:
        self.data.background.teal.max_ = self.widget.background.teal.max_value()
        return
  
    def __background_teal_steps_action(self)-> None:
        self.data.background.teal.steps = self.widget.background.teal.steps_value()
        return
  
    def __background_blue_enabled_action(self)-> None:
        self.data.background.blue.enabled = self.widget.background.blue.is_checked()
        return
  
    def __background_blue_min_action(self)-> None:
        self.data.background.blue.min_ = self.widget.background.blue.min_value()
        return
  
    def __background_blue_max_action(self)-> None:
        self.data.background.blue.max_ = self.widget.background.blue.max_value()
        return
  
    def __background_blue_steps_action(self)-> None:
        self.data.background.blue.steps = self.widget.background.blue.steps_value()
        return
  
    def __background_purple_enabled_action(self)-> None:
        self.data.background.purple.enabled = self.widget.background.purple.is_checked()
        return
  
    def __background_purple_min_action(self)-> None:
        self.data.background.purple.min_ = self.widget.background.purple.min_value()
        return
  
    def __background_purple_max_action(self)-> None:
        self.data.background.purple.max_ = self.widget.background.purple.max_value()
        return
  
    def __background_purple_steps_action(self)-> None:
        self.data.background.purple.steps = self.widget.background.purple.steps_value()
        return
  
    def __foreground_white_enabled_action(self)-> None:
        self.data.foreground.white.enabled = self.widget.foreground.white.is_checked()
        return
  
    def __foreground_white_min_action(self)-> None:
        self.data.foreground.white.min_ = self.widget.foreground.white.min_value()
        return
  
    def __foreground_white_max_action(self)-> None:
        self.data.foreground.white.max_ = self.widget.foreground.white.max_value()
        return
  
    def __foreground_white_steps_action(self)-> None:
        self.data.foreground.white.steps = self.widget.foreground.white.steps_value()
        return
  
    def __foreground_black_enabled_action(self)-> None:
        self.data.foreground.black.enabled = self.widget.foreground.black.is_checked()
        return
  
    def __foreground_black_min_action(self)-> None:
        self.data.foreground.black.min_ = self.widget.foreground.black.min_value()
        return
  
    def __foreground_black_max_action(self)-> None:
        self.data.foreground.black.max_ = self.widget.foreground.black.max_value()
        return
  
    def __foreground_black_steps_action(self)-> None:
        self.data.foreground.black.steps = self.widget.foreground.black.steps_value()
        return
  
    def __foreground_red_enabled_action(self)-> None:
        self.data.foreground.red.enabled = self.widget.foreground.red.is_checked()
        return
  
    def __foreground_red_min_action(self)-> None:
        self.data.foreground.red.min_ = self.widget.foreground.red.min_value()
        return
  
    def __foreground_red_max_action(self)-> None:
        self.data.foreground.red.max_ = self.widget.foreground.red.max_value()
        return
  
    def __foreground_red_steps_action(self)-> None:
        self.data.foreground.red.steps = self.widget.foreground.red.steps_value()
        return
  
    def __foreground_yellow_enabled_action(self)-> None:
        self.data.foreground.yellow.enabled = self.widget.foreground.yellow.is_checked()
        return
  
    def __foreground_yellow_min_action(self)-> None:
        self.data.foreground.yellow.min_ = self.widget.foreground.yellow.min_value()
        return
  
    def __foreground_yellow_max_action(self)-> None:
        self.data.foreground.yellow.max_ = self.widget.foreground.yellow.max_value()
        return
  
    def __foreground_yellow_steps_action(self)-> None:
        self.data.foreground.yellow.steps = self.widget.foreground.yellow.steps_value()
        return
  
    def __foreground_green_enabled_action(self)-> None:
        self.data.foreground.green.enabled = self.widget.foreground.green.is_checked()
        return
  
    def __foreground_green_min_action(self)-> None:
        self.data.foreground.green.min_ = self.widget.foreground.green.min_value()
        return
  
    def __foreground_green_max_action(self)-> None:
        self.data.foreground.green.max_ = self.widget.foreground.green.max_value()
        return
  
    def __foreground_green_steps_action(self)-> None:
        self.data.foreground.green.steps = self.widget.foreground.green.steps_value()
        return
  
    def __foreground_teal_enabled_action(self)-> None:
        self.data.foreground.teal.enabled = self.widget.foreground.teal.is_checked()
        return
  
    def __foreground_teal_min_action(self)-> None:
        self.data.foreground.teal.min_ = self.widget.foreground.teal.min_value()
        return
  
    def __foreground_teal_max_action(self)-> None:
        self.data.foreground.teal.max_ = self.widget.foreground.teal.max_value()
        return
  
    def __foreground_teal_steps_action(self)-> None:
        self.data.foreground.teal.steps = self.widget.foreground.teal.steps_value()
        return
  
    def __foreground_blue_enabled_action(self)-> None:
        self.data.foreground.blue.enabled = self.widget.foreground.blue.is_checked()
        return
  
    def __foreground_blue_min_action(self)-> None:
        self.data.foreground.blue.min_ = self.widget.foreground.blue.min_value()
        return
  
    def __foreground_blue_max_action(self)-> None:
        self.data.foreground.blue.max_ = self.widget.foreground.blue.max_value()
        return
  
    def __foreground_blue_steps_action(self)-> None:
        self.data.foreground.blue.steps = self.widget.foreground.blue.steps_value()
        return
  
    def __foreground_purple_enabled_action(self)-> None:
        self.data.foreground.purple.enabled = self.widget.foreground.purple.is_checked()
        return
  
    def __foreground_purple_min_action(self)-> None:
        self.data.foreground.purple.min_ = self.widget.foreground.purple.min_value()
        return
  
    def __foreground_purple_max_action(self)-> None:
        self.data.foreground.purple.max_ = self.widget.foreground.purple.max_value()
        return
  
    def __foreground_purple_steps_action(self)-> None:
        self.data.foreground.purple.steps = self.widget.foreground.purple.steps_value()
        return
    
    def __connect_output_path_actions(self)-> None:
        self.widget.output_path.browse.clicked.connect(self.__browse_button_action)
        return 
    
    def __connect_generate_button_actions(self)-> None:
        self.widget.generate_button.clicked.connect(self.__generate_button_action)
        return    

    def __browse_button_action(self)-> None:
        caption = 'Select Output Path...'
        path = QFileDialog.getExistingDirectory(
            parent = self, 
            caption = caption
        )
        self.data.path.path = path
        self.widget.output_path.input_.setText(path)
        
    def __generate_button_action(self)-> None:
        generator = Generate()
        generator.generate(self.data)
        return