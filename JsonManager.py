from pyperclip import copy, paste
from json import JSONDecodeError, dumps, loads

class JsonManager:
    #json 데이터 관리 기능 제공 클래스

    def __init__(self, db_file="db.json"):
        """
        초기화
        db_file: db.json 파일 경로 (기본값: "db.json")
        """
        self._data = {}
        self.db_file = db_file
    
    def copy_json(self, data):
        """
        json 데이터를 클립보드에 복사하고 db.json에 저장 (쓰기: "w")
        data: json 형식으로 저장할 데이터
        """
        import json
        copy(json.dumps(data))
        with open(self.db_file, "w") as f:
            json.dump(data, f)

    def paste_json(self):
        """
        클립보드에서 json 데이터를 가져오고 db.json에서 데이터를 읽음 (읽기: "r")
        """
        import json
        try:
            data = json.loads(paste())
        except JSONDecodeError:
            data = None
        with open(self.db_file, "r") as f:
            return data.get(f)

    def set_data(self, key, data):
        """
        key-value를 클립보드 데이터에 저장하고 db.json에 저장

        key: 저장할 데이터 키
        data: 저장할 데이터
        """
        import json
        self._data[key] = data
        with open(self.db_file, "w") as f:
            json.dump(self._data, f)

    def get_data(self, key):
        """
        key에 해당하는 value를 db.json에서 가져옴

        key: 가져올 데이터 키

        Returns: key에 해당하는 value
        """
        import json
        with open(self.db_file, "r") as f:
            data = json.load(f)
        return data.get(key)
