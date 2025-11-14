from utils.job_runner import JobRunner
from utils.loader_local import LoaderLocal
from utils.writer_local import WriterLocal
import pandas as pd


class ValidationJob(JobRunner):
    def __init__(self):
        self.in_path_list = [
            "/home/onyxia/work/hackathon_mobilites_2025/data/raw/validations-reseau-ferre-nombre-validations-par-jour-2eme-trimestre.parquet",
            "/home/onyxia/work/hackathon_mobilites_2025/data/raw/validations-reseau-ferre-nombre-validations-par-jour-3eme-trimestre.parquet",
            "/home/onyxia/work/hackathon_mobilites_2025/data/raw/validations-reseau-ferre-nombre-validations-par-jour-2eme-trimestre.parquet"
        ]
        self.out_path = "/home/onyxia/work/hackathon_mobilites_2025/data/interim/validation_pourcentage.parquet"

    def process(self):
        dataframes = []
        for file_path in self.in_path_list:
            df = LoaderLocal.loader_parquet(file_path)
            dataframes.append(df)
        df_concat = pd.concat(dataframes, ignore_index=True)
        df_concat['id_zdc'] = pd.to_numeric(df_concat['id_zdc'], errors='coerce')
        df_concat['nb_vald'] = pd.to_numeric(df_concat['nb_vald'].apply(lambda x: x.replace(' ', '') if type(x) is str else x), errors='coerce')

        # Total par id_zdc
        df_total = df_concat.groupby('id_zdc', as_index=False).agg(
            total_validation=('nb_vald', 'sum')
        )

        # Total pour la catégorie "Amethyste"
        df_amethyste = df_concat[df_concat['categorie_titre'] == 'Amethyste'].groupby('id_zdc', as_index=False).agg(
            total_validation_amethyste=('nb_vald', 'sum')
            )

        # Merge
        df_final = pd.merge(df_total, df_amethyste, on='id_zdc', how='inner')

        # Calculer le pourcentage de validation de type amethyste
        df_final['total_validation_amethyste'] = df_final['total_validation_amethyste'].fillna(0)
        df_final['pct_amethyste'] = (df_final['total_validation_amethyste'] / df_final['total_validation']) * 100
        df_final['pct_amethyste'] = df_final['pct_amethyste'].round(4)

        # Ecriture en parquet
        WriterLocal.write_parquet(df_final, self.out_path)
