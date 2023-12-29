from flask import Blueprint, Flask, jsonify, request
import os
import mysql.connector
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor

bot_blueprint = Blueprint('bot', __name__)


os.environ['OPENAI_API_KEY'] = "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"

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="welfare_management_system_dev"
)

# Create the agent executor
llm = OpenAI(temperature=0)
db = SQLDatabase.from_uri("mysql+mysqlconnector://root:@127.0.0.1/welfare_management_system_dev")
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)

# Defining API endpoint
@bot_blueprint.route('/bot', methods=['POST'])
def query():
    data = request.get_json()
    query = data.get('query')

    if not query:
        return jsonify({'error': 'Query parameter is missing'}), 400

    result = agent_executor.run(query)
    return jsonify({'result': result})