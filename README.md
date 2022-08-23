# Test

This repo shows how to convert the output from tb-profiler to represent variants which are associated with resistance for one drug but not for others for which the gene is associated. The default output only represents each variant once in either the "dr_variants" or the "other_variants". This `tbprofiler_convert_output.py` script will add extra entries into the "other_variants" list.

The repo uses a modified database which has rpoB/rifabutin added to the watchlist.

```
git clone git@github.com:jodyphelan/test.git
cd test/tbdb
tb-profiler create_db --prefix test --load
cd ../
python tbprofiler_convert_output.py --db test --input input.results.json --output output.results.json
```

You should now see the rpoB/p.Ser450Leu variant appear in the "other_variants" list in the output output file with an additional key value pair `{"non-associated-drug": "rifabutin"}`
