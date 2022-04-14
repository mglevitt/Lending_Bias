import os
import nbformat
from nbconvert import HTMLExporter


def convert_notebook(report_in_path, report_out_path, **kwargs):
    print(1)
    curdir = os.path.abspath(os.getcwd())
    print(2)
    indir, _ = os.path.split(report_in_path)
    print(3)
    outdir, _ = os.path.split(report_out_path)
    print(4)
    print(outdir)
    os.makedirs(outdir, exist_ok=True)

    config = {
        "ExecutePreprocessor": {"enabled": True},
        "TemplateExporter": {"exclude_output_prompt": True, "exclude_input": True, "exclude_input_prompt": True},
    }

    nb = nbformat.read(open(report_in_path), as_version=4)
    html_exporter = HTMLExporter(config=config)

    # change dir to notebook dir, to execute notebook
    os.chdir(indir)
    body, resources = (
        html_exporter
        .from_notebook_node(nb)
    )

    # change back to original directory
    os.chdir(curdir)

    with open(report_out_path, 'w') as fh:
        fh.write(body)
    

convert_notebook('src/EDA.ipynb','src/scripts')