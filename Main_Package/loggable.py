class Loggable:
    def __init__(self):
        self._logs = []

    # Define a method to add a log to the list
    def log(self, message):
        if isinstance(message, str):
            self._logs.append(message)

    # Define a property to get the logs
    @property
    def logs(self):
        return self._logs

    def save_logs_to_file(self, filename):
        with open(filename, 'w') as file:
            for log_entry in self.logs:
                file.write(log_entry + '\n')