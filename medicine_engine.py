import pandas as pd

db = pd.read_csv("medicine_db.csv")

def get_medicine_info(name):
    row = db[db['name'] == name]
    if not row.empty:
        return row.iloc[0].to_dict()
    return None

def simplify_text(info):
    return f"""
    This medicine is used for {info['use']}.
    Take it {info['dosage']}.
    Warning: {info['warning']}.
    """