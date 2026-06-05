# gradebook v1.1 — 2주차 실습 시작
SUBJECTS = ["국어", "영어", "수학", "과학탐구"]

def input_grades():
    """점수를 입력받아 반환합니다."""
    return {"국어": 90, "영어": 85, "수학": 95, "과학탐구": 88}

def calc_average(grades):
    """평균 점수를 계산합니다."""
    total = sum(grades.values())
    return total / len(grades)

def print_stats(grades):
    """성적 통계를 출력합니다."""
    avg = calc_average(grades)
    max_subject = max(grades, key=grades.get)
    min_subject = min(grades, key=grades.get)

    print("=== 성적 결과 ===")
    print(f"평균: {avg}점")
    print(f"최고점 과목: {max_subject} ({grades[max_subject]}점)")
    print(f"최저점 과목: {min_subject} ({grades[min_subject]}점)")

if __name__ == "__main__":
    my_grades = input_grades()
    print_stats(my_grades)