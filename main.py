import argparse
import os, sys, datetime

from Workload import get_workloads, Workload
from runner import run


def cli():
    workloads = get_workloads()
    parser = argparse.ArgumentParser(
        description="Execute EnergiBridge experiments.",
        add_help=False,
        prog="EnergiBridge")
    parser.add_argument("--iterations",
                        help="Number of interations to run.",
                        dest="iterations",
                        type=int,
                        nargs='?',
                        default=30)
    parser.add_argument("--sleep",
                        help="sleep time between runs.",
                        dest="sleep",
                        type=int,
                        nargs='?',
                        default=5)
    parser.add_argument("-i", "--interval",
                        help="Interval between measurements.",
                        dest="interval",
                        type=int,
                        nargs='?',
                        default=100)
    parser.add_argument("--warmup",
                        help="Warmup time.",
                        dest="warmup",
                        type=int,
                        nargs='?',
                        default=0)
    parser.add_argument("-o", "--output",
                        help="Output directory.",
                        dest="output",
                        type=str,
                        nargs='?',
                        default="results")
    parser.add_argument("-w", "--workloads",
                        help="List of workloads to run.",
                        dest="workloads",
                        choices=["all"] + [w.name for w in workloads],
                        type=str,
                        nargs='*',
                        default="all")
    return parser.parse_args()


def main():
    args = cli()
    workloads = []
    for workload in args.workloads:
        if workload == "all":
            workloads = get_workloads()
            break
        w = Workload(workload)
        if w.enabled:
            workloads.append(w)

    if not os.path.isabs(args.output):
        args.output = os.path.join(os.getcwd(), args.output, sys.platform)
    args.output = os.path.join(args.output, datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
    run(workloads, args)


if __name__ == '__main__':
    main()