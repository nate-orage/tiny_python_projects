#!/home/nate/python/python_env/bin/python3
#Purpose : Say Hello
#print('Hello, World!')
import argparse

parser = argparse.ArgumentParser(description='Say Hello')
parser.add_argument('name', help='Name to Greet')
args=parser.parse_args()
print('Hello, '+ args.name + '!')