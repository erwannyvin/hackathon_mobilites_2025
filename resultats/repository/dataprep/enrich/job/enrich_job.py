from utils.job_runner import JobRunner
from utils.loader_local import LoaderLocal
from utils.writer_local import WriterLocal
import pandas as pd


class EnrichJob(JobRunner):
    def __init__(self):
        self.ref_gare_path = "/home/onyxia/work/hackathon_mobilites_2025/data/interim/ref_gares.gpq"
        self.carte_pmr_path = "/home/onyxia/work/hackathon_mobilites_2025/data/interim/carte_pmr.parquet"
        self.validation_path = "/home/onyxia/work/hackathon_mobilites_2025/data/interim/validation_pourcentage.parquet"
        self.etablissements_path = "/home/onyxia/work/hackathon_mobilites_2025/data/interim/etablissements.gpq"
        self.out_path = "/home/onyxia/work/hackathon_mobilites_2025/data/enrich/final_table.gpq"

    def process(self):
        df_ref_gare = LoaderLocal.loader_geoparquet(self.ref_gare_path)
        df_carte_pmr = LoaderLocal.loader_parquet(self.carte_pmr_path)
        df_validation = LoaderLocal.loader_parquet(self.validation_path)
        df_etablissement = LoaderLocal.loader_geoparquet(self.etablissements_path)

        # Calcul des établissement a coté des stations


        # Jointure avec la carte PMR
        df_join_carte = pd.merge(df_ref_gare, df_carte_pmr, on='station_clean', how='right')
        df_filter_carte = df_join_carte[
            df_join_carte['ligne'].isna() |
            (df_join_carte['ligne'] == '') |
            (df_join_carte['ligne'] == df_join_carte['res_com'])
        ].copy()
        # Jointure avec les validations
        df_filter_carte['id_ref_zdc'] = df_filter_carte['id_ref_zdc'].astype(str)
        df_validation['id_zdc'] = df_validation['id_zdc'].astype(str)
        df_final = pd.merge(df_filter_carte, df_validation, left_on="id_ref_zdc", right_on="id_zdc", how='left')

        # Ecriture en GeoParquet
        WriterLocal.write_geoparquet(df_final, self.out_path)
