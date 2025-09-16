from kedro.pipeline import Pipeline, node, pipeline
from .nodes import preprocess_data, create_normalized_entities, create_master_table

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_data,
                inputs="countries_gdp",
                outputs="preprocessed_countries_gdp",
                name="preprocess_countries_gdp_node",
            ),
            node(
                func=preprocess_data,
                inputs="life_expectancy",
                outputs="preprocessed_life_expectancy",
                name="preprocess_life_expectancy_node",
            ),
            node(
                func=preprocess_data,
                inputs="organizations_gdp",
                outputs="preprocessed_organizations_gdp",
                name="preprocess_organizations_gdp_node",
            ),
            node(
                func=create_normalized_entities,
                inputs=["preprocessed_life_expectancy", "preprocessed_countries_gdp", "preprocessed_organizations_gdp"],
                outputs=["normalized_life", "normalized_countries_gdp", "normalized_orgs_gdp"],
                name="create_normalized_entities_node",
            ),
            node(
                func=create_master_table,
                inputs=["normalized_life", "normalized_countries_gdp", "normalized_orgs_gdp"],
                outputs="master_table",
                name="create_master_table_node",
            ),
        ]
    )