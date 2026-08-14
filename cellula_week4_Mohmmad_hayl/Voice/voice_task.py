from Voice.stt import SpeechToText
from Voice.db_handler import DBHandler
from Voice.sql_generator import SQLGenerator


class VoiceTask:
    def __init__(self, stt: SpeechToText, db: DBHandler, sql_gen: SQLGenerator):
        self.stt = stt
        self.db = db
        self.sql_gen = sql_gen

    def process(self, audio_path: str, csv_path: str):
        columns = self.db.load_csv(csv_path)

        stt_result = self.stt.transcribe(audio_path)
        question = stt_result["text"]

        sql_query = self.sql_gen.generate_sql(question, columns)

        query_result = self.db.execute_query(sql_query)

        return {
            "transcription": question,
            "language": stt_result["language"],
            "generated_sql": sql_query,
            "result": query_result
        }