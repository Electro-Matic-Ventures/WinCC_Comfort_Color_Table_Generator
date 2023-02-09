class StyleSheet:
    
    as_string = '''
MainWindow {
    background-color: #222831;
}


CentralWidget {
    background-color: #222831;
}


AreaPanel {
    background-color: #222831;
    color: #EEEEEE;
    font-size: 20pt;
    border: 2px solid #FFD369;
    margin-top: 10px;
}
AreaPanel::title {
    left: 10px;
    bottom: 20px;
}


ColorPanel {
    background-color: #222831;
    color: #EEEEEE;
    font-size: 14pt;
    border: 2px solid #FFD369;
    margin-top: 15px;
}
ColorPanel::title {
    left: 6px;
    bottom: 15px;
}


ColorEnable {
    background-color: #222831;
    color: #EEEEEE;
    font-size: 12pt;
    padding-left: 4px;
    padding-top: 16px;
}   


LabeledInputLabel {
    background-color: #222831;
    color: #EEEEEE;
    font-size: 10pt;
}   


LabeledInputInput {
    background-color: #EEEEEE;
    border: 2px solid #FFD369;
    color: #393E46;
    font-size: 10pt;
    font-weight: bold;
}


OutputPath {
    background-color: #222831;
    color: #EEEEEE;
    font-size: 14pt;
    border: 2px solid #FFD369;
    margin-top: 15px;
}
OutputPath::title {
    left: 6px;
    bottom: 15px;
}


OutputPathInput {
    background-color: #EEEEEE;
    border: 2px solid #FFD369;
    border-radius: 4px;
    color: #393E46;
    font-size: 10pt;
    font-weight: bold;
}


OutputPathBrowse {
    background-color: #393E46;
    color: #EEEEEE;
    font-size: 10px;
    font-weight: bold;
    border: 2px solid #FFD369;
    border-radius: 4px;
}


GenerateButton {
    background-color: #393E46;
    color: #EEEEEE;
    border: 2px solid #FFD369;
    border-radius: 4px;
    font-size: 24px;
    font-weight: bold;
}
    '''