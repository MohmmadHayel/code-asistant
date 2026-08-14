from llm.llm_engine import LLMEngine  # استدعاء المحرك الموجود عندك


class SQLGenerator:
    def __init__(self, llm_engine: LLMEngine):
        self.llm = llm_engine

    def generate_sql(self, question: str, columns: list[str], table_name: str = "data_table") -> str:
        prompt = f"""You are a SQLite expert. Given the table '{table_name}' with columns: {columns}.
Convert the following user question into a valid, executable SQL query ONLY. 
Do NOT wrap it in markdown block quotes (e.g. no ```sql). Return only the raw SQL query string.

Question: {question}
SQL Query:"""
        
        response = self.llm.generate(prompt)
        # تنظيف بسيط للنص
        return response.strip().replace("```sql", "").replace("```", "").strip()