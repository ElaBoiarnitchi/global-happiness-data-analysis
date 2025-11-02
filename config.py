DATA_FILE = 'data/global_happiness.xlsx'

COLUMNS = {
    'Country',
    'Purchasing power index',
    'Safety index',
    'Health care index',
    'Cost of living index',
    'Property price to income ratio',
    'Traffic commute time index',
    'Pollution index',
    'Climate index',
    'WorldHappinessScore_2024'
}

NUMERIC_COLUMNS = [col for col in COLUMNS if col != 'Country']

OUTPUTS = {
    'plots': 'outputs/plots',
    'reports': 'outputs/reports',
    'data': 'outputs/data'
}

CORRELATION_THRESHOLD = 0.7
N_CLUSTERS = 4
RANDOM_STATE = 42
