#!/usr/bin/env python3

'''
run against a directory of telemetry data (dir) to find files that are within mode == dt sec (float) or mode == count count threshold to files that match a pattern

USAGE(s)
./matching_file_neighbors.py --dir ~/data_dir --pattern .*exception
./matching_file_neighbors.py --dir ~/Desktop/ --pattern .*pdf --mode count
'''

import argparse
import os, sys, time, numpy as np
import datetime
import pprint

#port, archive
def all_files_matching_pattern(path, regex=r".*"):
    import re, os
    pattern = re.compile(regex)
    all_files = os.listdir(path)
    return all_files, list(filter(
        lambda f: pattern.match(f), all_files))

def insert_into_dict_of_arrays(d, k, v):
    if k in d.keys():
        d[k].append(v)
    else:
        d[k] = v

def epoch_time_sort(all_files):
    with_epoch_times = [[f, os.path.getmtime(f)] for f in all_files]
    # print("with_epoch_times\n", with_epoch_times)
    all_files_sorted = sorted(with_epoch_times, key=lambda x: x[1])
    return all_files_sorted

def find_neighbors(all_files, matching_file_epochtime_index,
    before, after,
    mode = "dt"):
    matching_epochtime = matching_file_epochtime_index[1]
    matching_idx = matching_file_epochtime_index[2]
    # print("matching_idx", matching_idx)

    # decrement
    neg_candidates = []
    candidate_idx = matching_idx
    while (candidate_idx > 0):
        candidate_idx = candidate_idx - 1
        if mode == "dt":
            dist = abs(all_files[candidate_idx][1] - matching_epochtime)
            if dist < before:
                neg_candidates.append(all_files[candidate_idx] + [candidate_idx])
            else:
                break
        elif mode == "count":
            if len(neg_candidates) < int(before):
                neg_candidates.append(all_files[candidate_idx] + [candidate_idx])
            else:
                break

    pos_candidates = []
    candidate_idx = matching_idx
    while (candidate_idx < len(all_files)-1):
        candidate_idx = candidate_idx + 1
        if mode == "dt":
            dist = abs(all_files[candidate_idx][1] - matching_epochtime)
            if dist < after:
                pos_candidates.append(all_files[candidate_idx] + [candidate_idx])
            else:
                break
        elif mode == "count":
            if len(pos_candidates) < int(after):
                pos_candidates.append(all_files[candidate_idx] + [candidate_idx])
            else:
                break

    return list(reversed(neg_candidates)) + pos_candidates

if __name__ == '__main__':
    blackboard = {}

    parser = argparse.ArgumentParser(description='hello')
    parser.add_argument("--dir", type=str, required=True)
    parser.add_argument("--pattern", type=str, default=".*")

    parser.add_argument("--before", type=float, default=1.0)
    parser.add_argument("--after", type=float, default=1.0)
    parser.add_argument("--mode", type=str, default="dt")

    blackboard["args"] = parser.parse_args()
    if not os.path.isdir(os.path.expanduser(
        blackboard["args"].dir)):
        print("dir dne")
        sys.exit(1)

    raw_pattern = r'{}'.format(blackboard["args"].pattern)

    all_files, matching_files = all_files_matching_pattern(
        blackboard["args"].dir,
        raw_pattern)

    all_files = list(map(
        lambda x: blackboard["args"].dir + x,
        all_files))

    matching_file_to_neighbors = {}

    # iterative approach :\
    all_files = epoch_time_sort(all_files)
    import re, os
    pattern = re.compile(raw_pattern)
    matching = []
    for i, f_and_epoch in enumerate(all_files):
        if pattern.match(f_and_epoch[0]):
            matching.append(f_and_epoch + [i])

    for m in matching:
        neighbors = find_neighbors(all_files, m,
            blackboard["args"].before,
            blackboard["args"].after,
            blackboard["args"].mode)
        insert_into_dict_of_arrays(
            matching_file_to_neighbors,
            m[0], neighbors)

    # pp = pprint.PrettyPrinter(indent=4, compact=True)
    # pp.pprint(matching_file_to_neighbors)

    for k in matching_file_to_neighbors:
        v = matching_file_to_neighbors[k]

        # do logic with matching file and neighbors
        filenames = [d[0] for d in v]
        filenames = list(reversed(sorted(filenames)))
        print("%s: " % k, filenames)
