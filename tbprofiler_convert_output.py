#! /usr/bin/env python

# Load useful libraries
import json
import argparse
import pathogenprofiler as pp
import tbprofiler
from copy import copy


def main(args):
    conf = pp.get_db("tbprofiler", args.db)
    locus_tags2drug_dict = tbprofiler.get_lt2drugs(conf["bed"])
    data = json.load(open(args.input))
    for var in data["dr_variants"]:
        drugs_involved = set([x["drug"] for x in var["drugs"]])
        for drug in set(locus_tags2drug_dict[var["locus_tag"]]).difference(drugs_involved):
            var_copy = copy(var)
            var_copy["non-associated-drug"] = drug
            data["other_variants"].append(var_copy)

    json.dump(data, open(args.output, "w"))

# Set up the parser
parser = argparse.ArgumentParser(description='tbprofiler script',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--input',type=str,help='Input json file')
parser.add_argument('--output',type=str,help='Output json file')
parser.add_argument('--db',default="tbdb",type=str,help='Database name')
parser.set_defaults(func=main)

args = parser.parse_args()
args.func(args)
