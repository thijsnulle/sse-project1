import argparse

from Experiment import run_tasks

def main():
    parser = argparse.ArgumentParser(description="Selenium script argument parser")
    parser.add_argument("name")
    parser.add_argument("ip")
    args = parser.parse_args()

    run_tasks(args)

if __name__ == '__main__':
    main()