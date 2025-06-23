import re
import os


def print_instructions():
    usr=os.environ['USER']
        
    textfile = open('jupyter_logbook.txt', 'r')
    matches = []
    reg = re.compile(r'^\s+http://127.0.0.1:([0-9]*)')
    #print(f"reg: {reg}")
    for line in textfile:
        match=reg.match(line)
        if match is not None:
            port=match.group(1)
            print("On your laptop open a new terminal and open an ssh tunnel by pasting this:")
            print('ssh -L {}:localhost:{} ML-TRISEP -N -f'.format(port, port))
            print("then in your browser address bar paste:")
            print(line.lstrip())
            
    textfile.close()




if __name__=='__main__':
    print_instructions()
