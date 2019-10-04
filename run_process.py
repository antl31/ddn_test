import subprocess
import json


class RunProcess:
    def __init__(self, params):
        self.stdin = params
        self.stderr = b''
        self.stdout = b''
        self.return_code = ''

    def run(self):
        #run ssh through subporcess
        with subprocess.Popen(self.stdin, stdout=subprocess.PIPE, shell=True) as p:
            self.stdout, self.stderr = p.communicate()
            self.return_code = p.wait()

    def create_report(self, filename):
        stdout = self.stdout.decode("utf-8") if self.stdout else None
        stderr = self.stderr.decode("utf-8") if self.stderr else None
        report_dict = {"stdin": self.stdin,
                       "stdout": stdout,
                       "stderr": stderr
                       }
        with open(f'{filename}.json', 'w+') as fp:
            json.dump(report_dict, fp)


if __name__ == "__main__":
    a = RunProcess(params='/bin/bash -c hostname')
    a.run()
    print(a.stdout)
    print(a.stderr)
    print(a.return_code)
    a.create_report('shell')




