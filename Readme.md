# Energibridge-React experiment

To run you need to have energibridge in the `[sse-project1_PARENT_DIRECTORY]\energibridge` folder.

Also depending on which browser you use you have to download the specific webdriver and edit the path in the `Experiment.py` file.
For example the [Chrome drivers](https://googlechromelabs.github.io/chrome-for-testing/#stable).

Make sure rapl is running

Finally run `main.py` with the settings such as `--sleep 50 --iterations 32 -i 200 -o experiment -w [chrome, firefox, ...]`

The runner will install and run the servers for each iteration.

# Bugs/TODOS:
- [ ] Warmup workload is not working as it will run the full task including running servers instead of the command.
- [ ] Configure for linux and macOS
