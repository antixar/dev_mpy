# add a minimal pool of tests for the next code:
# rewrite this code if you have a better variant
 
ADMIN_USER = "vasja.pupkin"
ADMIN_PASSWD = "passsecret"

def valid_admin_user(username, password):
  return username.lower() == ADMIN_USER and password == ADMIN_PASSWD