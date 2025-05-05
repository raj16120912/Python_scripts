import os

class Run():
    def first_run(self,cmd):
        self.cmd = os.system(cmd)

    def second_run(self):
        print(f'Output : {self.cmd}')


def main():
    op = Run()
    op.first_run('df -h')
    op.first_run('free -m')
    print(op.second_run())
    print(op.second_run())

if __name__ == "__main__":
    main()