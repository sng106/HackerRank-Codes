'''Sample Input :
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output :
Berry
Harry'''
if __name__ == '__main__':
    records = [(input(), float(input())) for _ in range(int(input()))]
    second_lowest_score = sorted(set(score for name, score in records))[1]
    for name, score in sorted([(name, score) for name, score in records if score == second_lowest_score]):
        print(name)
