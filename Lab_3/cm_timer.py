# cm_timer.py

import time
from contextlib import contextmanager


class cm_timer_1:
    """Контекстный менеджер на основе класса."""

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.time() - self.start_time
        print(f"time: {elapsed_time:.4f}")


@contextmanager
def cm_timer_2():
    """Контекстный менеджер с использованием contextlib."""
    start_time = time.time()
    try:
        yield
    finally:
        elapsed_time = time.time() - start_time
        print(f"time: {elapsed_time:.4f}")


if __name__ == "__main__":
    print("--- Тестирование cm_timer_1 (класс) ---")
    with cm_timer_1():
        time.sleep(1.2)

    print("\n--- Тестирование cm_timer_2 (contextlib) ---")
    with cm_timer_2():
        time.sleep(1.8)
