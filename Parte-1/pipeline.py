import papermill as pm

from console_logging.console import Console
console = Console()

console.log("RUNNING Analise Exploratoria ")
pm.execute_notebook(
   'Analise Exploratoria.ipynb',
    "out1.ipynb"
)

console.log("RUNNING NOTEBOOK 02")
pm.execute_notebook(
   'Machine Learning Pipeline - 02.ipynb',
    "out2.ipynb"
)

console.info("RUNNING NOTEBOOK 03")
pm.execute_notebook(
   'Machine Learning Pipeline - 03.ipynb',
    "out3.ipynb"
)


console.success("DONe! ")