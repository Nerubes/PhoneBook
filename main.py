import sys

from PhoneBook import PhoneBookReader

def main():
    path = 'db'
    if len(sys.argv) > 1:
        path = sys.argv[1]
    reader = PhoneBookReader(path)
    while True:
        command = input()

        try:
            match command:
                case 'add':
                    reader.AddRecord(PhoneBookReader.Parse(input()))
                case 'find':
                    filter = PhoneBookReader.Parse(input())
                    found = reader.FindRecord(filter)
                    print(found)
                    print(f'=========\nFound {len(found)} matches :\n', *found, '=========', sep='')
                case 'list':
                    reader.ListAllRecords()
                case 'replace':
                    filter = PhoneBookReader.Parse(input())
                    new_info = PhoneBookReader.Parse(input())
                    try:
                        reader.ChangeRecord(filter, new_info)
                    except AssertionError as e:
                        print(e)
                case 'exit':
                    return 0
        except Exception as e:
            print(f'Unknown exeption : {e}')



if __name__ == '__main__':
    main()