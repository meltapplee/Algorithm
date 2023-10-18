import random
import time

def make_problem():
    n1 = random.randint(1, 9)
    n2 = random.randint(1, 9)
    question = f"{n1} x {n2} = "
    answer = n1 * n2
    return question, answer

def main():
    correct = 0
    start_time = time.time()
    for _ in range(10):
        question, correct_answer = make_problem()
        user_answer = int(input(question))
        if user_answer == correct_answer:
            correct += 1
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total Time: {total_time:.2f} 초")
    print(f"맞은 문제 수: {correct}/{10}")

if __name__ == "__main__":
    main()