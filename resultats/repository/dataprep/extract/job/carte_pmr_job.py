from utils.job_runner import JobRunner
from utils.loader_local import LoaderLocal
from utils.transformation import Transformation
from utils.writer_local import WriterLocal


class CartePmrJob(JobRunner):
    def __init__(self):
        self.in_path = "/home/onyxia/work/hackathon_mobilites_2025/data/raw/carte_pmr.csv"
        self.out_path = "/home/onyxia/work/hackathon_mobilites_2025/data/interim/carte_pmr.parquet"

    def process(self):
        # Lecture des données à partir d'un fichier csv
        df = LoaderLocal.loader_csv(self.in_path)
       
        # Transformation des données et sélection des colonnes utiles
        df["station_clean"] = df["station"].apply(Transformation.clean_name)
        cols = ["ligne", "station", "facilite_acces_code",
                "facilite_acces", "nombre_facilite_acces_station", "station_clean"]
        df_final = df[cols]

        # Ecriture des données en format parquet
        WriterLocal.write_parquet(df_final, self.out_path)
