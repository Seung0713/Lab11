def parse_student(student_data):
    student_id = int(student_data[:8])
    name = student_data[8:-4]
    birth_month = student_data[-4:-2]
    birth_year = student_data[-2:]

    return {
        'id': student_id,
        'name': name,
        'birthdate': f'{birth_month}/{birth_year}'
    }

def count_items(lst):
    result = {}
    for item in lst:
        result[item] = result.get(item, 0) + 1
    return result

def list_fighters(battle_data):
    participants = set(battle_data.keys())
    for fighter in battle_data.values():
        participants.update(fighter["loss"])
        participants.update(fighter["win"])
    return sorted(participants)
