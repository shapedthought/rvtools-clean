Hashes sensitive information in RvTools and returns the vInfo and vPartition data in two separate files.

Requires:

pip install pandas openpyxl click

Example usage:

```
Usage: rvtools_clean.py [OPTIONS]

Options:
  -p, --path TEXT    Path to RVTools output  [required]
  -v, --all          Hash everything
  -v, --vm           Hash VM names
  -d, --dc           Hash Datacenter names
  -c, --cluster      Hash Cluster names
  -pr, --print_data  Print output to console
  -o, --output       Output to Excel
  --help             Show this message and exit.
```