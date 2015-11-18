
import simplejson

file=open("test.json", "r")

for line in file:
    if line.strip()!='':
        response_dict = simplejson.loads(line)
        for info in response_dict:
            print "\n"
            for key in info.keys():
                print key, ':', info[key]
file.close()
