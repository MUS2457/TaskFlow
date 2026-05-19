def get_ratio(total, counter_parameter, parameter):
    if total == 0:
        return 0
    return round(counter_parameter.get(parameter, 0) / total, 1)

def completed_ratio(total, counter_status, x="Completed"):
    return get_ratio(total, counter_status, x)

def pending_ratio(total, counter_status, x="Pending"):
    return get_ratio(total, counter_status, x)

def in_progress_ratio(total, counter_status, x="In progress"):
    return get_ratio(total, counter_status, x)
