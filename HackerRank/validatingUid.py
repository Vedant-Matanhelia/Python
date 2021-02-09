from re import search

uid = []
for _ in range(int(input())):
    i = ''.join(sorted(input()))
    try :
        assert search(r'[A-Z]{2}', i)
        assert search(r'\d\d\d', i)
        assert not search(r'(.)\1', i)
        assert i.isalnum()
        assert len(i) == 10
    except Exception:
        print('Invalid')
    else:
        print('Valid')
