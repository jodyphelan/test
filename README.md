# test

```
git clone git@github.com:jodyphelan/test.git
cd test/tbdb
tb-profiler create_db --prefix test --load
cd ../
python tbprofiler_convert_output.py --db test --input input.results.json --output output.results.json
```

You should now see the variant appear in the "other_variants" list in the output output file with an additional key value pair `{"non-associated-drug": "rifabutin"}`