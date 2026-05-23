from dsite.services.index import add_to_index, update_index

def add_service(service, is_list=False, is_third=False):

    if is_third:
        if is_list:
            for element in service:
                add_to_index(element, third=True)
        else:
            add_to_index(service, third=True)

    else:
        if is_list:
            for element in service:
                add_to_index(element)
        else:
            add_to_index(service)

    update_index()
