def get_authorized_user(connection):
    return connection.make_request('!authuser')["User"];

def get_specific_user(connection, user):
    return connection.make_request("/user/" + user)["User"];
