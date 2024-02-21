from __future__ import annotations

import subprocess, os, sys, datetime, json

import runner

class EnergiBridge:
    def __init__(self, settings) -> None:
        self.settings = settings
        pass

    def cmd(self, task: runner.Task):
        program_path = os.path.join(os.path.dirname(__file__), "..", "energibridge", "energibridge")
        if sys.platform == "win32":
            program_path += ".exe"
        # print(program_path)
        # print(['"'+program_path+'"', "-i", str(self.settings.interval), "--max-execution", str(task.workload.max_execution), "-o", '"'+f"{task.output_path}.csv"+'"'])
        return ['"'+program_path+'"', "-i", str(self.settings.interval), "--max-execution", str(task.workload.max_execution), "-o", '"'+f"{task.output_path}.csv"+'"']

    def run(self, task: runner.Task):
        os.makedirs(os.path.dirname(task.output_path), exist_ok=True)

        # BUG/TODO:  Add sleep/timeout after --. Just running `--` will not run the energibridge. Because we open the website via the webdriver it does not make sense to open here again.
        # ERROR: `Input redirection is not supported, exiting the process immediately.` -> using timeout in subprocess
        task.Current_Energibridge_Process = subprocess.Popen(" ".join(self.cmd(task) + ['--', task.workload.command]), shell=False) # , task.workload.command
