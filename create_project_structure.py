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

    def create_structure(current_path, structure):
        for key, value in structure.items():
            path = os.path.join(current_path, key)
            if not os.path.exists(path):
                os.makedirs(path)
                print(f"创建目录：{path}")
            else:
                print(f"目录已存在：{path}")
            
            if isinstance(value, list):
                for file in value:
                    file_path = os.path.join(path, file)
                    if not os.path.exists(file_path):
                        open(file_path, 'w').close()
                        print(f"创建文件：{file_path}")
                    else:
                        print(f"文件已存在：{file_path}")
            elif isinstance(value, dict):
                create_structure(path, value)

    create_structure(base_path, structure)

if __name__ == "__main__":
    base_path = "pyqt5_examples"
    create_directory_structure(base_path)
    print("项目结构创建完成。")
