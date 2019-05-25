# A script for assembling the script.
# Some notes:
# - 0_0.md is the title page. Use it for title page things!
# - The .md files are ordered by act_scene.md (You can have 99 scenes in an act before this gets screwy with the sorting.)

# This script is licensed under the Unlicense. Do whatever you want with this shitty fountain assembler script.
import os, re, time, sys

FILENAME = re.compile(r"(\d+)_(\d+)")
DRAFT_DATE = time.strftime("%m/%d/%Y")

def filenamekey(filename):
	m = FILENAME.search(filename)
	if not m:
		return 100000
	act, scene = m.groups()
	act = int(act)
	scene = int(scene)
	return (act*100)+scene

def filegetcontents(filename):
	with open(filename) as f:
		return f.read().strip().replace("[draft_date]",DRAFT_DATE)

def list_scenes():
	files = [os.path.join("scenes",x) for x in os.listdir("scenes")]
	files.sort(key=filenamekey)
	return files

def assemble():
	files = list_scenes()
	files = [filegetcontents(x) for x in files]
	return "\n\n".join(files)

if __name__=="__main__":
	with open(sys.argv[1],"w") as f:
		f.write(assemble())
