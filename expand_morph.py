import sys
import json

def handle_stream(stream, mapping):
    for line in map(str.strip, stream):
        if line == "":
            print() 
            continue
        handle_line(line, mapping)

def handle_line(line, mapping):
    line = line.split("\t")
    line[5] = line[5].replace("=", ":")
    feat_dict = {
            feature: value for feature, value in 
                    map(lambda x: (x[0], ":".join(x[1:])),
                    map(lambda x: x.split(":"), line[5].split("|")))
            }
    m = feat_dict.get("Morph","")
    expanded = mapping.get(m,"")
    feat_string = "|".join([k+":"+v for k,v in feat_dict.items()])
    if expanded != "":
        feat_string += "|" + expanded
    line[5] = feat_string
    return print("\t".join(line))
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide mapping file")
    with open(sys.argv[1]) as mapping:
        mapping = json.load(mapping)
    handle_stream(sys.stdin, mapping = mapping)
