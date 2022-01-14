import os
import json
import dictdiffer

parent_dir = 'D:\\Root\\path\\dir'
ignore_list = ['py_cache', 'temp', '.git', 'bad_file.exe']

def save_dir_state(filename, dir_dict):
	fout = open(filename, 'w')
	fout.write(json.dumps(dir_dict, indent=4))
	fout.close()

def verify_dir_state(filename, dir_dict):
	fin = open(filename, 'r')
	prev_state = json.loads(fin.read())
	fin.close()
	if prev_state == dir_dict:
		return (True, None)
	else:
		return (False, list(dictdiffer.diff(prev_state, dir_dict)))

# file below can also be a directory
for file in os.listdir(parent_dir) if file not in ignore_list:
	cur_dict_struct[file] = os.listdir(parent_dir + '\\' + file)

# Shorthand
# cur_dict_struct = {fille: os.listdir(parent_dir + '\\' + file) for file in os.listdir(parent_dir) if file not in ignore_list}

# Run this before first run
# save_dir_state('initial_dir_state.txt', cur_dict_struct)

match, diff = verify_dir_state('initial_dir_state.txt', cur_dict_struct)
if match:
	print('directory is up-to-date.')
else:
	save_dir_state('new_state.txt', cur_dict_struct)
	print('update required:', diff)
