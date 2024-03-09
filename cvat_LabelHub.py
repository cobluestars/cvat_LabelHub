import pyautogui
import json
from tkinter import *

# 1. 라벨링 데이터 json 파일의 경로
data_file = "db.json"

# 2. 라벮 데이터 로드
try:
    with open(data_file, "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("db.json 파일을 찾을 수 없습니다.")
    exit()
except json.JSONDecodeError:
    print("db.json 파일 형식이 올바르지 않습니다.")
    exit()

# 3. 키보드 매크로 함수
def paste_label_data(label_name):
    """
    지정된 라벨 이름에 해당 데이터를 붙여넣음
    """

    if label_name not in data:
        return
    
    data_to_paste = data[label_name]

    # 클립보드에 데이터 복사 붙여넣기
    pyautogui.write(data_to_paste)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl', 'v')

# 4. 키 입력 이벤트 리스너 설정
def on_key_press(event):
    """
    키 입력 이벤트를 감지하고 처리

    1, on_key_press(event) 함수는 키 입력 이벤트를 감지하고 처리
    2. event.keysym 변수는 눌린 키의 이름을 나타냄
    3. 왼쪽 Alt 키를 누르고 A를 누르면 label_name 변수에 "Alt_L+A"가 저장
    4. "Alt_L+A"가 data dictionary에 존재하면 paste_label_data 함수가 호출되어 해당 라벨 데이터가 붙여넣기됨
    """

    pressed_keys = event.keysym

    if "Alt_L" in pressed_keys and len(pressed_keys) == 2:
        label_name = pressed_keys
        if label_name in data:
            paste_label_data(label_name)

# 5. 프로그램 UI 설정
root = Tk()
root.geometry("400x200")
root.title("CVAT_LabelHub")

# 6. 라벨 목록
label_list = Listbox(root)
for label in data.keys():
    label_list.insert(END, label) 
label_list.pack()

# 7. 종료 버튼
def close_program():
    for key in pyautogui.KEYBOARD_KEYS:
        pyautogui.hotkey('win', key, interval=0.01, unregister=True)
    root.quit()

close_button = Button(root, text="Close", command = close_program)
close_button.pack()

# 8. 프로그램 실행
root.mainloop()