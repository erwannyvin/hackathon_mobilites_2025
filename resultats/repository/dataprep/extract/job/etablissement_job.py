from utils.job_runner import JobRunner
from utils.loader_local import LoaderLocal
from utils.writer_local import WriterLocal
from utils.transformation import Transformation
import pandas as pd


class EtablissementJob(JobRunner):
    def __init__(self):
        self.in_dico = {
            'Etablissements adultes handicapés':
                '/home/onyxia/work/hackathon_mobilites_2025/data/raw/etablissements_et_services_pour_adultes_handicapes.csv',
            'Etablissements enfants handicapés':
                '/home/onyxia/work/hackathon_mobilites_2025/data/raw/etablissements_et_services_pour_l_enfance_et_la_jeunesse_handicapee.csv',
            'Etablissements hospitaliers':
                '/home/onyxia/work/hackathon_mobilites_2025/data/raw/les_etablissements_hospitaliers_franciliens.csv'
        }

        self.out_path = "/home/onyxia/work/hackathon_mobilites_2025/data/interim/etablissements.gpq"

    def find_col(self, df_cols, candidates):
        for cand in candidates:
            if cand in df_cols:
                return cand
        return None

    def prepare_df(self, df, type_etablissement):

        # Sélectionner les colonnes utile
        col_map = {
            'lat': ['lat', 'LAT'],
            'lng': ['lng', 'LNG'],
            'RAISON_SOCIALE': ['RAISON_SOCIALE']
        }

        lat_col = self.find_col(df.columns, col_map['lat'])
        lng_col = self.find_col(df.columns, col_map['lng'])
        rs_col = self.find_col(df.columns, col_map['RAISON_SOCIALE'])

        if not all([lat_col, lng_col, rs_col]):
            print(f"Colonnes manquantes dans {type_etablissement}")
            return None

        # Extraire et renommer
        subset = df[[lat_col, lng_col, rs_col]].copy()
        subset.rename(columns={
            lat_col: 'lat',
            lng_col: 'lng',
            rs_col: 'raison_social'
        }, inplace=True)

        # Supprimer les lignes avec coordonnées manquantes
        subset.dropna(subset=['lat', 'lng'], inplace=True)

        # Ajouter la colonne de type
        subset['type_etablissement'] = type_etablissement

        return subset

    def process(self):

        dataframes = []
        for type_etablissement, filepath in self.in_dico.items():
            df = LoaderLocal.loader_csv(filepath)
            subset = self.prepare_df(df, type_etablissement)
            if subset is not None:
                dataframes.append(subset)
        
        if not dataframes:
            raise ValueError("Aucun DataFrame valide n'a été créé.")

        # Concaténation
        df_global = pd.concat(dataframes, ignore_index=True)

        # Conversion en GeoDataFrame
        final_gdf = Transformation.transform_geopandas(df_global, "lat", "lng")
        WriterLocal.write_geoparquet(final_gdf, self.out_path)
