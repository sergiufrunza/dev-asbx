from uszipcode import SearchEngine
engine = SearchEngine()


def get_state(zipcode):
    state_by_zip = engine.by_zipcode(int(zipcode))
    if state_by_zip:
        return state_by_zip.state, state_by_zip.major_city
    else:
        return '', ''