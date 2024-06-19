import mindsdb_sdk

# connects to the specified host and port
server = mindsdb_sdk.connect('http://127.0.0.1:47334')


gmail_access = server.create_database(
    engine = "gmail",
    name = "gmail_access",
    connection_args = {
        "credentials_file": "<YOUR CREDENTIALS FILE DIRECTORY>",
        "scopes": ['https://.../gmail.compose', 'https://.../gmail.readonly']
    }
)

server.ml_engines.create(
       'openai_engine',
       'openai',
       connection_data={'openai_api_key': '<YOUR API KEY>'}
   )

project = server.create_project('summariser_bot')


text_summarization_model = project.models.create (
      name='text_summarization_model',
      engine='openai_engine', # alternatively: engine=server.ml_engines.openai
      predict='snippet',
      prompt_template='provide an informative summary of the text text:{{body}} using full sentences in 100 words or less, the information should be presented in bulletpoints, there should be 7 or less bulletpoints, ignore talking about promotional material, be very selective about only mentioning critical information',
      #model_name='gpt3.5'
)

text_summarization_model = project.models.get('text_summarization_model')

query = project.query('SELECT input.body, output.snippet FROM gmail_access.emails AS input JOIN text_summarization_model AS output LIMIT 1;')
snippets = query.fetch()


slack_conn = server.create_database(
    engine = "slack",
    name = "slack_conn",
    connection_args = {
      "token": "<YOUR SLACKBOT API TOKEN>"
    }
)

query2 = slack_conn.query('INSERT INTO slack_conn.channels (channel, text) SELECT "mindsdb-test" AS channel, output.snippet AS text FROM gmail_access.emails AS input JOIN summariser_bot.text_summarization_model AS output LIMIT 5')
query2.fetch()

gmail_refresh = project.create_job(
    'gmail_refresh',
    'SELECT input.body, output.snippet FROM gmail_access.emails AS input JOIN text_summarization_model AS output LIMIT 5;',
    repeat_str = '1 hour'
)

slack_refresh = project.create_job(
    'slack_refresh',
    'INSERT INTO slack_conn.channels (channel, text) SELECT "mindsdb-test" AS channel, output.snippet AS text FROM gmail_access.emails AS input JOIN summariser_bot.text_summarization_model AS output LIMIT 5;',
    repeat_str = '1 hour'
)
