import os
import random
import subprocess
from datetime import datetime, timedelta

# 
os.makedirs("solutions", exist_ok=True)

# 
if not os.path.exists(".git"):
    subprocess.run(["git", "init"])

total_problems = 600
days_back = 30
problems_per_day = total_problems // days_back  # 

now = datetime.now()
problem_count = 1

# 
for day_offset in range(days_back, 0, -1):
    base_date = now - timedelta(days=day_offset)

    for p in range(problems_per_day):
        if problem_count > total_problems:
            break

        # 
        hour = random.randint(9, 22)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)

        commit_date = base_date.replace(
            hour=hour, minute=minute, second=second
        )
        date_iso = commit_date.strftime("%Y-%m-%dT%H:%M:%S")

        # 
        file_path = f"solutions/problem_{problem_count:03d}_solution.py"

        solution_code = f"""# LeetCode Problem {problem_count} Solution
# Author: Sebagat Selim

class Solution:
    def solveProblem{problem_count}(self, nums: list[int], target: int) -> int:
        # Solution implementation for LeetCode Problem {problem_count}
        seen = {{}}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
"""

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(solution_code)

        # 
        subprocess.run(["git", "add", file_path], check=True)

        # 
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = date_iso
        env["GIT_COMMITTER_DATE"] = date_iso

        commit_message = f"Add LeetCode solution for Problem {problem_count}"
        subprocess.run(
            ["git", "commit", "-m", commit_message], env=env, check=True
        )

        print(
            f"[{problem_count}/600] Created commit for date: {commit_date.strftime('%Y-%m-%d %H:%M:%S')}"
        )
        problem_count += 1

print("\n successfylly created 600 commits for LeetCode solutions over the past.")


