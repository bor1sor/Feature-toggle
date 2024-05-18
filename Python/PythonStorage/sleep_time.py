import time

def test_sleep():
    start_time = time.time()
    time.sleep(2)
    end_time = time.time()
    elapsed_time = end_time - start_time
    assert elapsed_time >= 2, "Sleep time less than expected"
    print("Test passed: Slept for at least 2 seconds")

test_sleep()