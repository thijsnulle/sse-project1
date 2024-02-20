import os
import random
import signal
import subprocess
import sys
import time
from time import sleep
from EnergiBridge import EnergiBridge
from Experiment import run_tasks

from Workload import Workload
from subprocess import Popen

Current_Experiment_Process = None
Current_Energibridge_Process = None

class Task:
    def __init__(self, id, workload: Workload, settings, react_version):
        self.id = id
        self.workload = workload
        self.settings = settings
        self.Current_Experiment_Process = None
        self.Current_Energibridge_Process = None
        self.react_version = react_version

    @property
    def output_path(self):
        return os.path.join(self.settings.output, self.workload.name, str(self.id))

    def run(self):
        # 1. npm install
        self.install_server(str(self.react_version))
        # 2. npm start
        self.load_server(str(self.react_version))
        # 2.1. wait for load
        time.sleep(10)
        # 3. start energibridge
        EnergiBridge(self.settings).run(self)
        # 4. Selenium
        print("DO EXPERIMENT")
        run_tasks(self.workload)
        # 5. stop energibridge
        # self.stop_energibridge()
        # 6. stop server
        # self.stop_server()

    def install_server(self, react_version):
        print("INSTALL SERVER")
        p = subprocess.run("npm install", shell=True, cwd=react_version)

    def load_server(self, react_version):
        print("LOADING SERVER")
        self.Current_Experiment_Process = subprocess.Popen("npm run start", shell=True, cwd=react_version)

    def stop_server(self):
        print("STOPPING SERVER")
        self.Current_Experiment_Process.send_signal(signal.SIGINT)

    def start_energibridge(self, settings):
        print("START ENERGIBRIDGE")
        EnergiBridge(settings).run(self)

    def stop_energibridge(self):
        self.Current_Energibridge_Process.send_signal(signal.SIGINT) # Gives error, maybe ctrl+c not possible


def generate_tasks(workloads: [Workload], settings):
    tasks = []
    row = 0
    for workload in workloads:
        for react_version in [r".\react-latest"]: # , r".\react-legacy"
            for i in range(settings.iterations):
                tasks.append(Task(i + 1 + (row * settings.iterations), workload, settings, react_version))
            row += 1
    tasks.sort(key = lambda x: random.random())
    warmup_workload = Workload("warmup")
    if settings.warmup > 0:
        return [Task(-1, warmup_workload, settings, "")] + tasks
    else:
        return tasks

def run(workloads: [Workload], settings):
    tasks = generate_tasks(workloads, settings)
    for task in tasks:
        task.run()
        sleep(settings.sleep)

def main():
    return


if __name__ == '__main__':
    main()