import unittest
import os

from ssh import RunProcess

dir_path = os.path.dirname(os.path.realpath(__file__))


class TestTelnet(unittest.TestCase):
    def setUp(self):
        self.actual_stdin = 'telnet google.com 443'
        self.actual_stdout = (b"Trying 216.58.215.110...\nConnected to google.com.\nEscape character is '^"
                              b"]'.\n")
        self. actual_filedata = r'''{"stdin": "telnet google.com 443", "stdout": "Trying 216.58.215.110...\nConnected to google.com.\nEscape character is '^]'.\n", "stderr": null}'''
        self.ssh = RunProcess(self.actual_stdin)
        self.ssh.run()
        self.ssh.create_report('telnet')

    def test_create_object(self):
        self.assertEqual(self.ssh.stdin, self.actual_stdin)
        self.assertEqual(self.ssh.stdout, self.actual_stdout)
        self.assertEqual(self.ssh.return_code, 1)

    def test_file_exist(self):
        for file_name in os.listdir(dir_path):
            if file_name == 'telnet.json':
                self.count = True

        self.assertTrue(self.count)

    def test_validate_file_data(self):
        with open('telnet.json') as json_data:
            data = json_data.read()
        self.assertEqual(data, self. actual_filedata)


class TestSSH(unittest.TestCase):
    def setUp(self):
        self.actual_stdin = 'ssh -T localhost'
        self.actual_stdout = b''
        self.actual_filedata = r'''{"stdin": "ssh -T localhost", "stdout": null, "stderr": null}'''
        self.ssh = RunProcess(self.actual_stdin)
        self.ssh.run()
        self.ssh.create_report('ssh')

    def test_create_object(self):
        self.assertEqual(self.ssh.stdin, self.actual_stdin)
        self.assertEqual(self.ssh.stdout, self.actual_stdout)
        self.assertEqual(self.ssh.return_code, 255)

    def test_file_exist(self):
        try:
            for file_name in os.listdir(dir_path):
                if file_name == 'ssh.json':
                    self.count = True
        except FileNotFoundError:
            print('file doesnt exist')

        self.assertTrue(self.count)

    def test_validate_file_data(self):
        try:
            with open('ssh.json') as json_data:
                data = json_data.read()
        except FileNotFoundError:
            print('file doesnt exist')

        self.assertEqual(data, self.actual_filedata)


class TestShell(unittest.TestCase):
    def setUp(self):
        self.actual_stdin = '/bin/bash -c hostname'
        self.actual_stdout = b'antl-VirtualBox\n'
        self.actual_filedata = r'''{"stdin": "/bin/bash -c hostname", "stdout": "antl-VirtualBox\n", "stderr": null}'''
        self.ssh = RunProcess(self.actual_stdin)
        self.ssh.run()
        self.ssh.create_report('shell')

    def test_create_object(self):
        self.assertEqual(self.ssh.stdin, self.actual_stdin)
        self.assertEqual(self.ssh.stdout, self.actual_stdout)
        self.assertEqual(self.ssh.return_code, 0)

    def test_file_exist(self):
        try:
            for file_name in os.listdir(dir_path):
                if file_name == 'shell.json':
                    self.count = True
        except FileNotFoundError:
            print('file doesnt exist')

        self.assertTrue(self.count)

    def test_validate_file_data(self):
        try:
            with open('shell.json') as json_data:
                data = json_data.read()
        except FileNotFoundError:
            print('file doesnt exist')

        self.assertEqual(data, self.actual_filedata)

