# #####>>>>>----- REQUIRED/IMPORTANT SETTINGS -----<<<<<#####

# Default maximum time (in seconds) to wait for page elements to appear.
# Different methods/actions in base_case.py use different timeouts.
# If the element to be acted on does not appear in time, the test fails.
MINI_TIMEOUT = 2
SMALL_TIMEOUT = 6
LARGE_TIMEOUT = 10
EXTREME_TIMEOUT = 30

# If True, existing logs from past test runs will be saved and take up space.
# If False, only the logs from the most recent test run will be saved locally.
# You can also archive existing logs on the command line with: "--archive_logs"
ARCHIVE_EXISTING_LOGS = False

# If True, existing downloads from past runs will be saved and take up space.
# If False, only the downloads from the most recent run will be saved locally.
ARCHIVE_EXISTING_DOWNLOADS = False

# If True, the Content Security Policy will be disabled on Chrome.
# If False, each website's default Content Security Policy will be used.
# (A website's CSP may prevent SeleniumBase from loading custom JavaScript.)
# You can also disable the CSP on the command line by using "--disable_csp".
DISABLE_CSP_ON_CHROME = False