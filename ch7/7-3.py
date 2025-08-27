# iterator_class.py
import time

def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"

class JobIterator:
    def __init__(self, num_jobs):
        self.num_jobs = num_jobs
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.num_jobs:
            raise StopIteration
        
        # 실제 작업 수행
        self.count += 1
        return longtime_job()

if __name__ == "__main__":
    job_iterator = JobIterator(5)
    print(next(job_iterator))