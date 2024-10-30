import os

"""
创建项目结构
"""
def create_directory_structure(base_path):
    structure = {
        '01_introduction': ['hello_world.py'],
        '02_core_modules': ['qtcore_example.py', 'qtgui_example.py', 'qtwidgets_example.py', 'qtmultimedia_example.py'],
        '03_basics': ['qapplication_example.py', 'qwidget_example.py', 'main_window.py'],
        '04_layouts': ['box_layout.py', 'grid_layout.py', 'form_layout.py'],
        '05_widgets': ['basic_widgets.py', 'container_widgets.py', 'advanced_widgets.py'],
        '06_signals_and_slots': ['basic_signals.py', 'custom_signals.py', 'advanced_signals.py'],
        '07_dialogs': ['message_box.py', 'input_dialog.py', 'file_dialog.py', 'color_dialog.py', 'font_dialog.py'],
        '08_events': ['mouse_events.py', 'keyboard_events.py', 'drag_drop_events.py'],
        '09_graphics': ['qpainter_basics.py', 'drawing_shapes.py', 'text_rendering.py'],
        '10_threading': ['basic_threading.py', 'worker_thread.py'],
        '11_database': ['db_connection.py', 'sql_model.py'],
        '12_internationalization': {
            '': ['translator_example.py'],
            'resources': ['translations_en.ts', 'translations_zh.ts']
        },
        '13_styling': ['qss_example.py', 'custom_style.py'],
        '14_deployment': ['pyinstaller_script.py'],
        '15_advanced': ['custom_widget.py', 'model_view_example.py', 'graphics_view.py', 'animation.py'],
        '16_projects': ['calculator', 'text_editor', 'image_viewer', 'todo_app']
    }
