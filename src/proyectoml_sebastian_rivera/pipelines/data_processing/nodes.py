import pandas as pd
import logging

log = logging.getLogger(__name__)

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Normaliza los nombres de las columnas a minúsculas y con guiones bajos."""
    df = df.rename(columns=lambda x: x.strip().lower().replace(" ", "_"))
    return df

def create_normalized_entities(
    life: pd.DataFrame, countries_gdp: pd.DataFrame, orgs_gdp: pd.DataFrame
) -> tuple:
    """Crea columnas normalizadas para los nombres de países/entidades."""
    life['entity_norm'] = life['entity'].str.strip().str.lower()
    countries_gdp['country_name_norm'] = countries_gdp['country_name'].str.strip().str.lower()
    orgs_gdp['country_name_norm'] = orgs_gdp['organization_name'].fillna('').str.strip().str.lower()
    return life, countries_gdp, orgs_gdp

def create_master_table(
    life: pd.DataFrame, countries_gdp: pd.DataFrame, orgs_gdp: pd.DataFrame
) -> pd.DataFrame:
    """
    Combina los datasets de GDP, los une con el de esperanza de vida
    y selecciona las columnas finales.
    """
    gdp_all = pd.concat([countries_gdp, orgs_gdp], ignore_index=True, sort=False)
    merged = pd.merge(
        gdp_all.dropna(subset=['year']),
        life.dropna(subset=['year']),
        left_on=['country_name_norm', 'year'],
        right_on=['entity_norm', 'year'],
        how='inner'
    )
    final_df = merged[[
        'country_name', 'year', 'total_gdp_million',
        'gdp_variation', 'period_life_expectancy_at_birth', 'region_name'
    ]].copy()

    log.info(f"Tabla maestra creada con {final_df.shape[0]} filas.")
    return final_df