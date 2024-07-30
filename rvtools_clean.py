import pandas as pd
import hashlib
import click

# pip install pandas openpyxl click

"""
Example usage:

python rvtools_clean.py -p "C:\\Users\\user\\Downloads\\rvtools.xlsx" -v -d -c -pr -o

-p: Path to RVTools output
-v: Hash VM names
-d: Hash Datacenter names
-c: Hash Cluster names
-pr: Print output to console
-o: Output to Excel

"""


def hash_col(df, col):
    col = df[col].apply(lambda x: hashlib.sha256(str(x).encode()).hexdigest())
    return col


@click.command()
@click.option("--path", "-p", required=True, help="Path to RVTools output")
@click.option("--all", "-v", is_flag=True, help="Hash everything")
@click.option("--vm", "-v", is_flag=True, help="Hash VM names")
@click.option("--dc", "-d", is_flag=True, help="Hash Datacenter names")
@click.option("--cluster", "-c", is_flag=True, help="Hash Cluster names")
@click.option("--print_data", "-pr", is_flag=True, help="Print output to console")
@click.option("--output", "-o", is_flag=True, help="Output to Excel")
def main(path, all, vm, dc, cluster, print_data, output):
    rvtools_path = path

    df_vinfo = pd.read_excel(rvtools_path, sheet_name="vInfo")
    df_vpart = pd.read_excel(rvtools_path, sheet_name="vPartition")
    df_vinfo = df_vinfo[["VM", "Powerstate", "In Use MiB", "Datacenter", "Cluster"]]
    df_vpart = df_vpart[["VM", "Powerstate", "Capacity MiB", "Consumed MiB"]]

    if vm or all:
        df_vinfo["VM"] = hash_col(df_vinfo, "VM")
        df_vpart["VM"] = hash_col(df_vpart, "VM")

    if dc or all:
        df_vinfo["Datacenter"] = hash_col(df_vinfo, "Datacenter")

    if cluster or all:
        df_vinfo["Cluster"] = hash_col(df_vinfo, "Cluster")

    if print_data:
        print(df_vinfo)
        print(df_vpart)

    if output:
        df_vinfo.to_excel("vinfo.xlsx", index=False)
        df_vpart.to_excel("vpart.xlsx", index=False)


if __name__ == "__main__":
    main()
