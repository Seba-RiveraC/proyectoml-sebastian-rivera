from typing import Dict
from kedro.pipeline import Pipeline
from proyectoml_sebastian_rivera.pipelines import data_processing

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines."""
    data_processing_pipeline = data_processing.create_pipeline()

    return {
        "__default__": data_processing_pipeline,
        "dp": data_processing_pipeline,
    }