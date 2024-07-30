Hashes sensitive information in RvTools and returns the vInfo and vPartition data in two separate files.

Requires:

pip install pandas openpyxl click

Example usage:

```
python rvtools_clean.py -p "C:\\Users\\user\\Downloads\\rvtools.xlsx" -v -d -c -pr -o

-p: Path to RVTools output
-v: Hash VM names
-d: Hash Datacenter names
-c: Hash Cluster names
-pr: Print output to console
-o: Output to Excel
```