# CONFIGEDGE payload marker R9TB-tb (obviously-fake test marker, never a real secret)
DEMO_API_TOKEN = "configedge_FAKE_TOKEN_not_a_secret"
def q(uid):
    return "SELECT * FROM t WHERE id = " + uid  # configedge_sql_demo
