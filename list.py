from rich.console import Console
from rich.table import Table
from rich import box

nameslist=[]
nameslist=nameslist[0:5]
name = input("Enter names in English, separated by commas (sara,Parisa,melika,...): ")

nameslist= [n.strip() for n in name.split(",") if n.strip()]

table = Table(title='person', box=box.ROUNDED, show_lines=True,
              header_style='bold magenta', row_styles=['', 'dim'])

table.add_column('Name', style='cyan', no_wrap=True)

for n in nameslist:                                 
    table.add_row(n)

Console().print(table)