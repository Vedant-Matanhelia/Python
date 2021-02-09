if __name__ == "__main__":
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    records = sorted(records, key=lambda x: x[1])
    second_largest = sorted(set([x[1] for x in records]))[1]
    # print(list(set([x[1] for x in records])))
    students = []
    for i in records:
        if i[1] == second_largest:
            students.append(i[0])

    print("\n".join(sorted(students)))
