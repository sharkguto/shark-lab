from dercypy import app
import psutil

app.run(
    host="0.0.0.0",
    port=5000,
    workers=1, #psutil.cpu_count(),
    debug=None,
    access_log=False,
)
