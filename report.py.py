# report.py
# 성적 리포트를 파일로 저장하는 모듈

def save_report(scores, average):
    """성적 리포트를 마크다운 파일로 저장한다."""
    with open("report.md", "w", encoding="utf-8") as f:
        f.write("# 성적 리포트\n\n")
        f.write("## 과목별 점수\n\n")
        for subject, score in scores.items():
            f.write(f"- {subject}: {score:.1f}점\n")
        f.write(f"\n## 평균\n\n{average:.1f}점\n")
    print("report.md가 저장되었습니다.")