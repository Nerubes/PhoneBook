from __future__ import annotations

import fileinput

MISS_SYMBOLS = ['', '-']

class PhoneBookInfo:
    name : str
    surname : str
    patronymic : str
    org : str
    work_phone : int
    private_phone : int
    
    def __init__(self, name, surname, patronymic, org, work_phone, private_phone):
        self.name = name or '-'
        self.surname = surname or '-'
        self.patronymic = patronymic or '-'
        self.org = org or '-'
        self.work_phone = int(work_phone) if not work_phone in MISS_SYMBOLS else 0
        self.private_phone = int(private_phone) if not private_phone in MISS_SYMBOLS else 0

    @staticmethod
    def FiledsAmount() -> int:
        return len(vars(PhoneBookInfo(*[''] * 6)))

    def __str__(self) -> str:
        return ' '.join([str(i) for i in vars(self).values()]) + '\n'
    
    def __eq__(self : PhoneBookInfo, other : PhoneBookInfo) -> bool :
        for self_field, other_field in zip(vars(self).values(), vars(other).values()) :
            if other_field and not other_field in MISS_SYMBOLS and not self_field == other_field:
                return False
        return True



class PhoneBookReader:
    db_path : str

    def __init__(self, path : str = 'db.db') -> None:
        self.db = path

    @staticmethod
    def Parse(info : str) -> PhoneBookInfo:
        if info[-1] == '\n':
            info = info[:-1]
        args = info.split(' ')
        assert len(args) <= PhoneBookInfo.FiledsAmount()
        return PhoneBookInfo(*args, *[''] * (PhoneBookInfo.FiledsAmount() - len(args)))

    def ListAllRecords(self : PhoneBookReader) -> None:
        with open(self.db, "r") as db:
            for line in db:
                print(line, end='')
    
    def AddRecord(self : PhoneBookReader, info : PhoneBookInfo) -> None:
        with open(self.db, 'a') as db:
            db.write(str(info))
    
    def ChangeRecord(self : PhoneBookReader, filter : PhoneBookInfo, new_info : PhoneBookInfo) -> None:
        lines = self.FindRecord(filter)
        assert len(lines) == 1, 'Faild: Ambigious replace call'
        for line in fileinput.input(self.db, inplace=True):
            if line in lines:
                line = str(new_info)

    def FindRecord(self : PhoneBookReader, filter : PhoneBookInfo) -> list[str]:
        result = []
        with open(self.db, 'r') as db:
            for line in db:
                if PhoneBookReader.Parse(line) == filter:
                    result.append(line)
        return result