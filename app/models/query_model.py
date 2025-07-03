# import os
# from dotenv import load_dotenv
# from langchain.agents import create_sql_agent
# from langchain.agents.agent_toolkits import SQLDatabaseToolkit
# from langchain.sql_database import SQLDatabase
# from langchain.llms import Together
# import ast
# import re
# from app.db import db  # Import SQLAlchemy instance

# class QueryModel:
#     @staticmethod
#     def initialize_agent():
#         """Initialize the LangChain SQL agent."""
#         load_dotenv()
#         TOGETHER_API_KEY = os.getenv('TOGETHER_API_KEY')
#         if not TOGETHER_API_KEY:
#             raise ValueError("Missing TOGETHER_API_KEY environment variable")

#         os.environ['TOGETHER_API_KEY'] = TOGETHER_API_KEY

#         # Use SQLAlchemy's database URI
#         db_uri = 'postgresql://postgres:postgres@localhost/cims_dev'
#         db = SQLDatabase.from_uri(db_uri)
#         llm = Together(model="meta-llama/Llama-3-8b-chat-hf", temperature=0)
#         toolkit = SQLDatabaseToolkit(db=db, llm=llm)

#         custom_prompt = """
#         You are a SQL query assistant for a PostgreSQL database. Given a natural language query, execute the appropriate SQL query and return only the final result in a concise JSON-compatible format (list, dictionary, or number). Do not include explanations, commentary, or additional text.

#         Guidelines:
#         - Use the database schema to identify relevant tables and columns dynamically.
#         - For joins, match columns with compatible data types (e.g., VARCHAR with VARCHAR, not BIGINT with VARCHAR).
#         - For date-based queries (e.g., 'this year'), use the current year ({current_year}) and filter with appropriate date ranges (e.g., 'YYYY-01-01' to 'YYYY-12-31').
#         - If a query involves payments or dues, check for tables with names like 'payments' or 'payment_amounts' and columns like 'amount' or 'date'.
#         - Ensure all SQL queries are valid and avoid type mismatch errors.
#         """
#         return create_sql_agent(
#             llm=llm,
#             toolkit=toolkit,
#             verbose=True,
#             extra_prompt=custom_prompt.format(current_year=2025)
#         )

#     @staticmethod
#     def execute_query(query: str) -> any:
#         """Execute a natural language query and return the result."""
#         agent_executor = QueryModel.initialize_agent()
#         result = agent_executor.run(query)

#         # Clean and parse the result
#         result = re.sub(r'```.*?\n|This is a very basic example.*$', '', result, flags=re.DOTALL)
#         result = result.strip()

#         try:
#             parsed_result = ast.literal_eval(result) if isinstance(result, str) else result
#         except (ValueError, SyntaxError):
#             match = re.match(r'^\d+$', result)
#             if match:
#                 parsed_result = int(result)
#             else:
#                 # Handle conversational text by extracting structured data if possible
#                 # Example: "The members are NL001, NL002" -> ["NL001", "NL002"]
#                 match = re.search(r'(NL\d{3}(?:,\s*NL\d{3})*)', result)
#                 if match:
#                     parsed_result = [id.strip() for id in match.group(1).split(',')]
#                 else:
#                     parsed_result = result

#         return parsed_result
import os
import time
from dotenv import load_dotenv
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms import Together
import ast
import re
from app.db import db  # Import SQLAlchemy instance

class QueryModel:
    # Cache for database schema to reduce API calls
    _schema_cache = None
    _tables_cache = None

    @staticmethod
    def initialize_agent(visualize: bool = False):
        """Initialize the LangChain SQL agent."""
        load_dotenv()
        TOGETHER_API_KEY = os.getenv('TOGETHER_API_KEY')
        if not TOGETHER_API_KEY:
            raise ValueError("Missing TOGETHER_API_KEY environment variable")

        os.environ['TOGETHER_API_KEY'] = TOGETHER_API_KEY

        # Use SQLAlchemy's database URI
        db_uri = 'postgresql://postgres:postgres@localhost/cims_dev'
        db = SQLDatabase.from_uri(db_uri)
        llm = Together(model="meta-llama/Llama-3-8b-chat-hf", temperature=0)
        toolkit = SQLDatabaseToolkit(db=db, llm=llm)

        # Cache tables and schema if not already cached
        if QueryModel._tables_cache is None:
            QueryModel._tables_cache = db.get_table_names()
        if QueryModel._schema_cache is None:
            QueryModel._schema_cache = {table: db.get_table_info([table]) for table in QueryModel._tables_cache}

        if visualize:
            custom_prompt = """
            You are a SQL query assistant for a PostgreSQL database. Given a natural language query, execute the appropriate SQL query and return ONLY the final result in a JSON-compatible format (list, dictionary, or number). Do NOT include explanations, commentary, SQL code, or any additional text beyond the result.

            Guidelines:
            - For queries asking 'how many tables' or about the number of tables in the database, return the count of tables from the cached table list as a number.
            - For queries asking 'how many' about profiles, accounts, or users, use `SELECT COUNT(*) FROM profiles` directly and return the count as a number.
            - For queries mentioning 'member' or related terms, check tables with 'members' in their names (e.g., 'members', 'members_profile_detail', 'members_contact_details', 'members_family_and_marriage_details', 'members_special_notes') and prioritize columns like 'member_identification_id'.
            - For queries mentioning 'case' or related terms, check tables with 'cases' in their names (e.g., 'cases', 'case_categories') and prioritize relevant columns.
            - For joins, match columns with compatible data types (e.g., VARCHAR with VARCHAR, not BIGINT with VARCHAR).
            - For date-based queries (e.g., 'this year'), use the current year ({current_year}) and filter with appropriate date ranges (e.g., 'YYYY-01-01' to 'YYYY-12-31').
            - If a query involves payments or dues, check tables like 'payments', 'payment_amounts', or 'payment_types' and columns like 'amount' or 'date'.
            - Return results as JSON-compatible lists (e.g., ["NL001", "NL002"]), dictionaries, or numbers.
            - For member queries, return a list of member_identification_id values.
            - If the query is unrelated to the database, return "I don't know".
            """
        else:
            custom_prompt = """
            You are a SQL query assistant for a PostgreSQL database. Given a natural language query, execute the appropriate SQL query and return ONLY a single, concise conversational sentence summarizing the result (e.g., 'The members who haven't paid welfare dues this year are NL001, NL002, NL003.'). Do NOT include explanations, commentary, SQL code, or any additional text beyond the sentence.

            Guidelines:
            - For queries asking 'how many tables' or about the number of tables in the database, return a sentence like 'There are X tables in the database.' using the cached table list.
            - For queries asking 'how many' about profiles, accounts, or users, use `SELECT COUNT(*) FROM profiles` directly and return a sentence like 'There are X profile accounts.'
            - For queries mentioning 'member' or related terms, check tables with 'members' in their names (e.g., 'members', 'members_profile_detail', 'members_contact_details', 'members_family_and_marriage_details', 'members_special_notes') and prioritize columns like 'member_identification_id'.
            - For queries mentioning 'case' or related terms, check tables with 'cases' in their names (e.g., 'cases', 'case_categories') and prioritize relevant columns.
            - For joins, match columns with compatible data types (e.g., VARCHAR with VARCHAR, not BIGINT with VARCHAR).
            - For date-based queries (e.g., 'this year'), use the current year ({current_year}) and filter with appropriate date ranges (e.g., 'YYYY-01-01' to 'YYYY-12-31').
            - If a query involves payments or dues, check tables like 'payments', 'payment_amounts', or 'payment_types' and columns like 'amount' or 'date'.
            - Ensure all SQL queries are valid and avoid type mismatch errors.
            - Format the result as a single sentence with no extra lines or commentary.
            - If the query is unrelated to the database, return "I don't know".
            """
        return create_sql_agent(
            llm=llm,
            toolkit=toolkit,
            verbose=False,  # Disable verbose mode to avoid agent thought process
            extra_prompt=custom_prompt.format(current_year=2025)
        )

    @staticmethod
    def execute_query(query: str, visualize: bool = False) -> any:
        """Execute a natural language query and return the result."""
        # Handle table count query directly
        if "how many tables" in query.lower():
            if QueryModel._tables_cache is None:
                db = SQLDatabase.from_uri('postgresql://postgres:postgres@localhost/cims_dev')
                QueryModel._tables_cache = db.get_table_names()
            result = len(QueryModel._tables_cache)
            return result if visualize else f"There are {result} tables in the database."

        agent_executor = QueryModel.initialize_agent(visualize)
        max_retries = 6
        retry_delay = 10  # Increased delay to avoid rate limits

        for attempt in range(max_retries):
            try:
                result = agent_executor.run(query)
                break
            except Exception as e:
                error_str = str(e).lower()
                if "rate limit" in error_str and attempt < max_retries - 1:
                    print(f"Rate limit hit, retrying in {retry_delay} seconds... (Attempt {attempt + 1}/{max_retries})")
                    time.sleep(retry_delay)
                else:
                    raise Exception(f"Query failed after {max_retries} attempts: {error_str}")

        # Clean the result aggressively to remove LangChain verbosity
        result = re.sub(
            r'(?s)(Thought:.*?Final Answer:|\[.*?\]|\{.*?\}|Action:.*?\n|Observation:.*?\n|I now know.*?\n|If I.*?\n|Question:.*?\n)',
            '', result, flags=re.DOTALL
        )
        result = re.sub(r'```.*?\n|This is a very simple example.*$|The query can be improved.*$|\n.*$', '', result, flags=re.DOTALL)
        result = result.strip()

        if not visualize:
            # Return conversational sentence as-is
            return result

        # Parse for visualization
        try:
            parsed_result = ast.literal_eval(result) if isinstance(result, str) else result
        except (ValueError, SyntaxError):
            # Try to extract a single number
            match = re.match(r'^\d+$', result)
            if match:
                parsed_result = int(result)
            else:
                # Extract comma-separated numbers (e.g., "10, 25, 30 GHS" -> [10.0, 25.0, 30.0])
                num_match = re.search(r'(\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*)\s*(?:GHS)?', result)
                if num_match:
                    parsed_result = [float(n.strip()) for n in num_match.group(1).split(',')]
                else:
                    # Extract member IDs (e.g., "NL001, NL002, ..." -> ["NL001", "NL002", ...])
                    id_match = re.search(r'((?:NL\d{3}(?:,\s*NL\d{3})*))', result)
                    if id_match:
                        parsed_result = [id.strip() for id in id_match.group(1).split(',')]
                    else:
                        parsed_result = result

        return parsed_result