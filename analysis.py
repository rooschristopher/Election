import pandas as pd


def biden_count(x):
    return x['biden'] * x['votes']
def trump_count(x):
    return x['trump'] * x['votes']

def independent_percentage(x):
    return 1 - (x['biden'] + x['trump'])

def independent_count(x):
    return x['votes'] * x['independent']


states = [
    "Alabama","Alaska","Arizona","Arkansas","California","Colorado",
    "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
    "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
    "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
    "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
    "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
    "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
    "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]


for state in states:
    print (state)
    state_url = state.replace(' ', '-').lower()

    df = pd.read_csv('counts/{}.csv'.format(state_url), index_col=[0])
    df['biden_count'] = df.apply(biden_count, axis=1)
    df['trump_count'] = df.apply(trump_count, axis=1)
    df['biden_change'] = df['biden_count'].diff()
    df['trump_change'] = df['trump_count'].diff()
    df['vote_change'] = df['votes'].diff()
    df['independent'] = df.apply(independent_percentage, axis=1)
    df['independent_count'] = df.apply(independent_count, axis=1)
    df['independent_change'] = df['independent_count'].diff()

    df.to_csv('counts_analyzed/{}.csv'.format(state_url))

print (df)



