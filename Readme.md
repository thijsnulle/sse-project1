# Energibridge-React experiment

To run you need to have energibridge in the `[sse-project1_PARENT_DIRECTORY]\energibridge` folder.

Also depending on which browser you use you have to download the specific webdriver and edit the path in the `Experiment.py` file.
For example the [Chrome drivers](https://googlechromelabs.github.io/chrome-for-testing/#stable).

Finally run `main.py` with the settings such as `--iterations 10 -i 200 -o experiment -w [chrome, firefox, ...]`

The runner will install and run the servers for each iteration.

# Bugs/TODOS:
- [ ] Warmup workload is not working as it will run the full task including running servers instead of the command.
- [ ] `npm install` only works in react-latest
- [ ] stop react-scripts from opening the browser
- [ ] download webdrivers
- [ ] fix arguments given to energibridge after `--` since we don't open the browser from there.
- [ ] issues with `timeout` via subprocess, might be windows

# Errors with Energibridge
Make sure rapl is running

Error when creating output files is possibly due to not existing folders.
