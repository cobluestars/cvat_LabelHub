# todo1: API를 이용해서 CVAT 작업 데이터를 DB.json으로 옮기는 작업 필요

from pynput import keyboard
import pyautogui
import json
import pyperclip
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

# todo2: 라벨링 데이터를 불러오는 로직 추가하기
data = {
    'a': "'a' 라벨에 해당하는 데이터 입력하기"
}

# 3. 키보드 매크로 함수
def paste_label_data(label_name):
    """
    지정된 라벨 이름에 해당 데이터를 붙여넣음
    """

    if label_name not in data:
        print(f"Label '{label_name}' not found.")
        return
    
    data_to_paste = data[label_name]

    # 클립보드에 데이터 복사
    pyperclip.copy(data_to_paste)

    #붙여넣기
    pyautogui.hotkey('ctrl', 'v')

# 4. 키 입력 관련 설정
# 현재 활성화된 조합키를 추적하기 위한 세트
current_keys = set()

def on_press(key):
    # 키가 눌렸을 때 실행되는 콜백 함수
    try:
        # key.char 속성을 사용해 일반 문자 키 확인
        if key.char == 'a' and keyboard.Key.alt_l in current_keys:
            #alt + a가 눌리면 실행할 함수
            paste_label_data('a')
        if key.char == 'b' and keyboard.Key.alt_l in current_keys:
            paste_label_data('b')
        if key.char == 'c' and keyboard.Key.alt_l in current_keys:
            paste_label_data('c')
        if key.char == 'd' and keyboard.Key.alt_l in current_keys:
            paste_label_data('d')
    except AttributeError:
        #특수 키(조합 키)는 char 속성이 없으므로 여기에서 처리함.
        if key == keyboard.Key.alt_l:
            current_keys.add(key)

def on_release(key):
    #키에서 손을 떼었을 때 실행되는 콜백 함수
    try:
        #눌려진 키를 추적하는 세트에서 제거
        current_keys.remove(key)
    except KeyError:
        pass

    if key == keyboard.Key.esc:
        #Esc 키를 누르면 리스너 중지
        return False
    
# 리스너 등록
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

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