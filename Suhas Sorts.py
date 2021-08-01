import os
import glob
import re

# can be changed to whatever folder the files are in
# "." just means the current directory
WORKING_DIRECTORY = "."

# what to write in place of missing data
# change it to whatever you want
# this just writes nothing but keeps the spacing right
BLANK = ''

RGX = re.compile(r'(.+).txt')



def main():
	os.chdir(WORKING_DIRECTORY)
	basenames = [os.path.basename(p) for p in glob.glob("*.txt")]
		
	matches = [RGX.match(f) for f in basenames]
	matches = [m for m in matches if m]
				
	basenames = [m.group() for m in matches]
	files = [open(b, 'rU') for b in basenames]
		
	data = [f.read().split('\n')[:-1] for f in files]
	realdata = [[l for l in d if '#' not in l] for d in data]
	rows = [[l.split('\t') for l in d] for d in data]
	realrows = [[l.split('\t') for l in d] for d in realdata]
		
	n = len(data)
	m = len(rows[0][0])
	l = max(len(realrows[i])for i in range(n))
	
	for i in range(0, m):
		name = rows[0][0][i]
		if name[0] == '#':
			name = name[1:]
			name = name.strip()
		
		with open('%s.txt' % name, 'w') as fout:
			fout.write(' \t' + '\t'.join(basenames) + os.linesep)
			
			for j in range(l):
				fout.write('%d' % j)
				for k in range(n):
					try:
						if '#' in realrows[k][j][i]:
							print (basenames[k], j, i)
						
						fout.write('\t' + realrows[k][j][i])
					except:
						fout.write('\t' + BLANK)
				fout.write(os.linesep)
					
		
	for f in files:
		f.close()
			
if __name__ == "__main__":
	main()
