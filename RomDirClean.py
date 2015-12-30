# ROM Directory Cleaner!
# Ver 1.0 - Hastily Coded at 3 AM, 12/30/2015
# Gets rid of dupe roms in your directory

import os
import sys

# Hey, if you give me a bogus path I'll crash and burn.
# Also this assumes duplicate roms are successive in the directory listing
# (Meaning it won't catch dupe roms that are named completely differently,
# And your directory must be sorted.)
def main():
    if len(sys.argv) != 2:
        print("Usage: Python RomDirClean.py [Path to rom directory]")
        print("NOTE: This script is not recursive, it only looks in the provided directory.")
        return
    
    current_dir = sys.argv[1]
    f = []
    for(dirpath, dirnames, filenames) in os.walk(current_dir):
        f.extend(filenames)
        break

    last_name = None
    filename_list = []
    for filename in f :
        # Hacky way of comparing successive roms to see if they're for the same game
        # Logic is: If you take a filename, split on whitespace, then get rid of all elements with [ and (,
        # and then smoosh those elements back together, you get the name of the game this rom is for
        # IE: 688 Attack Sub (U) [!].zip -> 688 Attack Sub
        stripped_name = " ".join([n for n in filename.split(" ") if '[' not in n and '(' not in n])
        if last_name == None:
            last_name = stripped_name
            filename_list.append(filename)
        else:
            if stripped_name == last_name:
                filename_list.append(filename)
            else:
                # Make decision on which roms to keep
                # Delete all others
                # Reset
                if(len(filename_list)) > 1:
                    print("Cleaning excess ROMs for: "+ last_name)
                    indexes = make_decision(filename_list)
                    for ix in range(len(filename_list)):
                        if ix not in indexes:
                            os.remove(filename_list[ix])
                last_name = stripped_name
                filename_list = [filename]
        
# Decides which file to keep out of the list of filenames
# Returns indexes in a list, pertaining to which files to keep
def make_decision(filenames):
    # If there is only 1 name in the list, suck it up pansy
    if(len(filenames) < 2):
        return 0
    
    # If any of the filenames has a !, it's a perfect dump
        # If given multiple, take either U or E
        # Else, figure out another way to make a decision
    perf = [f for f in filenames if '[!]' in f]
    if len(perf) > 0:
        if len(perf) == 1:
            return [filenames.index(perf[0])]
        else:
            U = [f for f in perf if '(U)' in f]
            E = [f for f in perf if '(E)' in f]
            if len(U) > 0:
                return [filenames.index(U[-1])]
            if len(E) > 0:
                return [filenames.index(E[-1])]
            
    # No decision made, return all indexes
    print("No decision made for this file...")
    return [x for x in range(len(filenames))]
            
main()
