import subprocess
import sys

def run_command(command):
    print(command)
    try:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            shell=True
        )

        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())
        rc = process.poll()
        if rc != 0:
            raise subprocess.CalledProcessError(rc, command)

    except subprocess.CalledProcessError as e:
        print(f"Jest test command '{command}' failed with return code {e.returncode}", file=sys.stderr)
        sys.exit(1)

def get_test_command(root, file_path, test_case):
    return f'cd {root} && node "node_modules/.bin/jest" --color "{file_path}" -t "{test_case}"'
