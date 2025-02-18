def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
    for phone_number in phone_book:
        start = ""
        for number in phone_number:
            start += number
            if start in hash_map and start != phone_number:
                return False
    return True